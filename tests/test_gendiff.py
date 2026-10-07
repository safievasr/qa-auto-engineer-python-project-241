from pathlib import Path

import pytest

from gendiff import generate_diff
from gendiff.formatters.plain import to_plain_value
from gendiff.formatters.stylish import format_value
from gendiff.parser import parse

FIXTURES = Path(__file__).parent / "test_data"


def read_expected(name):
    return (FIXTURES / name).read_text().rstrip("\n")


# stylish


@pytest.mark.parametrize("ext", ["json", "yaml"])
def test_generate_diff_stylish(ext):
    file1 = FIXTURES / f"file1.{ext}"
    file2 = FIXTURES / f"file2.{ext}"

    expected = read_expected("expected_flat.txt")
    actual = generate_diff(str(file1), str(file2))

    assert actual == expected


# plain


@pytest.mark.parametrize("ext", ["json", "yaml"])
def test_generate_diff_plain(ext):
    file1 = FIXTURES / f"file1.{ext}"
    file2 = FIXTURES / f"file2.{ext}"

    expected = read_expected("expected_plain.txt")
    actual = generate_diff(str(file1), str(file2), "plain")

    assert actual == expected


# json


@pytest.mark.parametrize("ext", ["json", "yaml"])
def test_generate_diff_json(ext):
    file1 = FIXTURES / f"file1.{ext}"
    file2 = FIXTURES / f"file2.{ext}"

    expected = read_expected("expected_json.txt")
    actual = generate_diff(str(file1), str(file2), "json")

    assert actual == expected

# format_value ---


def test_format_value_none():
    assert format_value(None) == "null"


def test_format_value_true():
    assert format_value(True) == "true"


def test_format_value_false():
    assert format_value(False) == "false"


def test_format_value_int():
    assert format_value(50) == "50"


def test_format_value_string():
    assert format_value("hexlet.io") == "hexlet.io"


def test_format_value_list():
    assert format_value([1, 2, 3]) == "[1, 2, 3]"


def test_format_value_dict():
    assert format_value({"a": 1}) == '{"a": 1}'


# to_plain_value ---


def test_to_plain_value_string():
    assert to_plain_value("hexlet.io") == "'hexlet.io'"


def test_to_plain_value_true():
    assert to_plain_value(True) == "true"


def test_to_plain_value_false():
    assert to_plain_value(False) == "false"


def test_to_plain_value_none():
    assert to_plain_value(None) == "null"


def test_to_plain_value_int():
    assert to_plain_value(50) == "50"


def test_to_plain_value_list():
    assert to_plain_value([1, 2, 3]) == "[complex value]"


def test_to_plain_value_dict():
    assert to_plain_value({"a": 1}) == "[complex value]"


# parse ---


def test_parse_unsupported_format():
    with pytest.raises(ValueError):
        parse("{}", "xml")