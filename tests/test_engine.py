from diff.engine import generate_diff


def test_generate_diff():
    assert generate_diff('./tests/fixtures/before.json', './tests/fixtures/after.json') == '{\n    host: hexlet.io\n  + timeout: 50\n  - timeout: 20\n  - proxy: 123.234.53.22\n  + verbose: True\n}'
