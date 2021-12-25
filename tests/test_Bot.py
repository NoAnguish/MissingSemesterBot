import pytest

from bot.Bot import Bot


def test_reverse_ok():
    data = "abcd"
    expected_result = "dcba"

    result = Bot().reverse_message(data)

    assert result == expected_result


def test_reverse_empty():
    result = Bot().reverse_message("")

    assert result == ""


def test_reverse_non_str():
    data = 32

    with pytest.raises(TypeError):
        Bot().reverse_message(data)
