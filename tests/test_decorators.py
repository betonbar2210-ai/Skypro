import pytest

from src.decorators import log


@log(filename="log.txt")
def log_in_file_error(bool):
    raise Exception()


def test_log_in_file_error(capsys):
    with pytest.raises(Exception):
        log_in_file_error(bool=True)
    captured = capsys.readouterr()
    assert captured.out == ""


@log(filename="str")
def log_in_consol_error(bool):
    raise Exception()


def test_log_in_consol_error(capsys):
    with pytest.raises(Exception):
        log_in_consol_error(bool=False)

    captured = capsys.readouterr()
    assert "Функция log_in_consol_error error:\n" in captured.out
    assert captured.err == ""


def test_log_in_file_ok(capsys):
    @log(filename="log.txt")
    def add_numbers(a, b):
        return a + b

    result = add_numbers(5, 8)
    assert result == 13

    captured = capsys.readouterr()
    assert captured.out == ""


def test_log_in_concol_error(capsys):
    @log(filename="str")
    def add_numbers(a, b):
        return a + b

    result = add_numbers(5, 8)
    assert result == 13

    captured = capsys.readouterr()
    assert "Функция add_numbers оk:" in captured.out
    assert "Результат:\n13" in captured.out
    assert captured.err == ""
