import pytest

import utils


def test_encode_text_replaces_newlines_and_removes_control_characters():
    original = "Line1\nLine2\ufeffExtra\u000b""smart quotes: ”"
    encoded = utils.encode_text(original)

    assert isinstance(encoded, bytes)
    assert encoded == "Line1<br>Line2Extrasmart quotes: \"".encode("windows-1251")


def test_rgb_to_hex_handles_none_and_rounding():
    assert utils.rgb_to_hex(None, None, None) == "#000000"
    assert utils.rgb_to_hex(0.5, 0.5, 0.5) == "#808080"


@pytest.mark.parametrize(
    "r, g, b, expected",
    [
        (1, 0, 0, "#ff0000"),
        (0, 1, 0, "#00ff00"),
        (0, 0, 1, "#0000ff"),
        (0.1, 0.2, 0.3, "#1a334c"),
    ],
)
def test_rgb_to_hex_various_inputs(r, g, b, expected):
    assert utils.rgb_to_hex(r, g, b) == expected
