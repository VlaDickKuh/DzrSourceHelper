import upload_files


class DummyResponse:
    def __init__(self):
        self.text = "#message.upload_ok"
        self.cookies = {"c": "1"}


class DummySession:
    def __init__(self):
        self.posts = []
        self.get_calls = []

    def get(self, url):
        self.get_calls.append(url)
        return DummyResponse()

    def post(self, url, cookies=None, data=None, files=None):
        self.posts.append({"url": url, "cookies": cookies, "data": data, "files": files})
        return DummyResponse()


def test_upload_files_to_source_sends_files(monkeypatch):
    monkeypatch.setattr(upload_files, "authenticate", lambda: "service")
    monkeypatch.setattr(upload_files, "get_files_from_drive", lambda service, folder: {"img.png": b"binary"})

    fake_session = DummySession()
    monkeypatch.setattr(upload_files, "get_session", lambda: fake_session)
    monkeypatch.setattr(upload_files, "GAME_ID", "gid")
    monkeypatch.setattr(upload_files, "S_URL", "https://example.test/login")
    monkeypatch.setattr(upload_files, "FILES_UPLOAD_URL", "https://example.test/upload")

    upload_files.upload_files_to_source()

    assert fake_session.get_calls == ["https://example.test/login"]
    assert fake_session.posts
    post = fake_session.posts[0]
    assert post["url"] == "https://example.test/upload"
    assert post["data"]["path"].endswith("/games/gid")
    assert post["files"]["file0"][0] == "img.png"
