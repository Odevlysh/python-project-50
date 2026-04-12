import os
from gendiff.scripts.gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)


def test_gendiff_json():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = open(get_fixture_path('expected_result.txt')).read().strip()
    result = generate_diff(file1, file2)
    assert result == expected


def test_gendiff_yaml():
    file1 = get_fixture_path('file1.yml')
    file2 = get_fixture_path('file2.yml')
    expected = open(get_fixture_path('expected_result.txt')).read().strip()
    result = generate_diff(file1, file2)
    assert result == expected
