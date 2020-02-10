from diff.engine import generate_diff, rendering

file1 = open('./tests/fixtures/exp_json.txt', 'r')
exp = file1.read().rstrip()
file2 = open('./tests/fixtures/exp_recursion.txt', 'r')
exp_recursion = file2.read().rstrip()


def test_generate_diff_json():
    assert rendering(generate_diff('./tests/fixtures/before.json', './tests/fixtures/after.json', 'json')) == exp


def test_generate_diff_yaml():
    assert rendering(generate_diff('./tests/fixtures/before.yml', './tests/fixtures/after.yml', 'yml')) == exp


def test_generate_diff_recursion_json():
    assert rendering(generate_diff('./tests/fixtures/before_recursion.json', './tests/fixtures/after_recursion.json', 'json')) == exp_recursion
