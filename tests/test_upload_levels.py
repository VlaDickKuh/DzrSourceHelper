import builtins
from types import SimpleNamespace

import upload_levels


class DummyResponse:
    def __init__(self, status_code=200, text=""):
        self.status_code = status_code
        self.text = text
        self.cookies = {"session": "cookie"}


class DummySession:
    def __init__(self):
        self.posts = []
        self.gets = []

    def post(self, url, headers=None, data=None, cookies=None):
        self.posts.append({"url": url, "headers": headers, "data": data, "cookies": cookies})
        return DummyResponse()

    def get(self, url):
        self.gets.append(url)
        return DummyResponse()


def _build_level(skvoz=True, level_id="1"):
    common_fields = {
        "content": "text",
    }
    return {
        "ID Уровня:": {"content": level_id},
        "Сквозной:": {"content": "да" if skvoz else "нет"},
        "Текст уровня:": {
            "Текст:": {"content": "question"},
            "Примечания:": {"content": "note"},
        },
        "Подсказка 1:": {
            "Текст:": {"content": "clue1"},
            "Выдавать по запросу:": common_fields.copy(),
            "Штраф за использование:": common_fields.copy(),
            "Время до подсказки:": common_fields.copy(),
        },
        "Подсказка 2:": {
            "Текст:": {"content": "clue2"},
            "Выдавать по запросу:": common_fields.copy(),
            "Штраф за использование:": common_fields.copy(),
            "Время до подсказки:": common_fields.copy(),
        },
        "Комментарий и фото кодов:": {"content": "comment"},
        "Основные коды уровня:": {
            "tables": [[
                ["№", "Код", "КС", "Сектор"],
                ["1", "CODE1", "1", "A"],
            ]]
        },
        "Сектора на уровне:": {"tables": [[
            ["№", "Название"],
            ["1", "Sector 1"],
        ]]},
        "Количество кодов для взятия:": {
            "Вышка:": {"content": "2"},
        },
        "Время до окончания уровня:": {"content": "15"},
        "Спойлеры:": {
            "Спойлер 1:": {
                "Текст:": {"content": "spoiler"},
                "Ответы на спойлер:": {"content": "spoiler_code"},
            }
        },
        "Бонусные коды уровня:": {
            "tables": [[
                ["№", "Код", "КС", "Бонус"],
                ["1", "BONUS", "1", "10"],
            ]]
        },
        "Бонус за полное взятие:": {"content": "5"},
        "Штрафные коды уровня:": {
            "tables": [[
                ["№", "Код", "Штраф"],
                ["1", "FAKE", "2"],
            ]]
        },
        "Штраф за слив:": {"content": "3"},
        "Бонусный:": {"content": "нет", "Время бонуса:": {"content": ""}},
    }


def test_upload_levels_add_posts_built_data(monkeypatch):
    fake_session = DummySession()
    monkeypatch.setattr(upload_levels, "get_session", lambda: fake_session)
    monkeypatch.setattr(upload_levels, "upload_files_to_source", lambda: (_ for _ in ()).throw(AssertionError("should not upload files")))

    uploaded_levels = []
    monkeypatch.setattr(upload_levels, "upload_tech_level", lambda: uploaded_levels.append("tech"))

    sample_data = [{"Level 1": _build_level(skvoz=True)}]
    monkeypatch.setattr(upload_levels, "get_gdoc", lambda: sample_data)
    monkeypatch.setattr(upload_levels, "test_doc", lambda data, add: False)

    monkeypatch.setattr(upload_levels, "GAME_ID", "game")
    monkeypatch.setattr(upload_levels, "S_URL", "https://example.test")

    inputs = iter(["2", "1", ""])
    monkeypatch.setattr(builtins, "input", lambda *args, **kwargs: next(inputs))

    upload_levels.upload_levels(add=True)

    assert len(fake_session.posts) == 1
    post_call = fake_session.posts[0]
    assert post_call["url"] == "https://example.test"
    assert post_call["data"]["action"] == "add_zadanie"
    assert post_call["data"]["category"] == "game"
    assert post_call["data"]["title"] == "Level 1".encode("cp1251")
    assert uploaded_levels == ["tech"]


def test_upload_levels_update_skips_zero_id(monkeypatch):
    fake_session = DummySession()
    monkeypatch.setattr(upload_levels, "get_session", lambda: fake_session)
    monkeypatch.setattr(upload_levels, "upload_files_to_source", lambda: None)
    monkeypatch.setattr(upload_levels, "upload_tech_level", lambda: None)

    sample_data = [{"Level 1": _build_level(skvoz=False, level_id="0")}]
    monkeypatch.setattr(upload_levels, "get_gdoc", lambda: sample_data)
    monkeypatch.setattr(upload_levels, "test_doc", lambda data, add: False)

    monkeypatch.setattr(upload_levels, "GAME_ID", "game")
    monkeypatch.setattr(upload_levels, "S_URL", "https://example.test")

    inputs = iter(["2", "1", ""])
    monkeypatch.setattr(builtins, "input", lambda *args, **kwargs: next(inputs))

    upload_levels.upload_levels(add=False)

    assert fake_session.posts == []
