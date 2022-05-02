import pytest
from task import read_input_float, calculate, AbsException


def test_read_input_float_invalid(monkeypatch):
    for v in ['', '\n', '\r\n', 'str', '123abc', [], {}, None]:
        monkeypatch.setattr('builtins.input', lambda _: v)
        with pytest.raises(AbsException):
            read_input_float()


def test_read_input_float_valid(monkeypatch):
    for v in [x for x in range(-999, 999, 1)]:
        monkeypatch.setattr('builtins.input', lambda _: v)
        assert read_input_float() == float(v)


def test_calculate():
    for x in [x for x in range(-999, 999, 1)]:
        for y in [x for x in range(-999, 999, 1)]:
            assert calculate(x, y) == abs(x - y)
