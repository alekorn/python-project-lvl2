from diff.engine import generate_diff
from diff.formatters import json

file1 = open('./tests/fixtures/exp_json.txt', 'r')
exp = file1.read().rstrip()
file2 = open('./tests/fixtures/exp_recursion.txt', 'r')
exp_recursion = file2.read().rstrip()


def test_generate_diff_recursion_json():
    assert json.rendering(generate_diff('./tests/fixtures/before_recursion.json', './tests/fixtures/after_recursion.json', 'json')) == exp_recursion


def test_generate_diff_json():
    assert json.rendering(generate_diff('./tests/fixtures/before.json', './tests/fixtures/after.json', 'json')) == exp


def test_generate_diff_yaml():
    assert json.rendering(generate_diff('./tests/fixtures/before_recursion.yaml', './tests/fixtures/after_recursion.yaml', 'yaml')) == exp_recursion
