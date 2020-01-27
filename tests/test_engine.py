from diff.engine import generate_diff

file = open('./tests/fixtures/exp_json.txt', 'r')
result = file.read().rstrip()


def test_generate_diff_json():
    assert generate_diff('./tests/fixtures/before.json', './tests/fixtures/after.json', 'json') == result


def test_generate_diff_yaml():
    assert generate_diff('./tests/fixtures/before.yml', './tests/fixtures/after.yml', 'yml') == result
