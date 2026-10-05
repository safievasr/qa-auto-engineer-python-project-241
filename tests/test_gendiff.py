from pathlib import Path

from gendiff import generate_diff

FIXTURES = Path(__file__).parent / "test_data"


def read_expected(name):
    return (FIXTURES / name).read_text().rstrip("\n")


def test_generate_diff_flat_json():
    file1 = FIXTURES / "file1.json"
    file2 = FIXTURES / "file2.json"

    expected = read_expected("expected_flat.txt")
    actual = generate_diff(str(file1), str(file2))

    assert actual == expected