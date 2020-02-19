from diff.engine import generate_diff
from diff.formatters import recursive, flat

# EXP_GENERATE_DIFF = json.loads(open('./tests/fixtures/exp_generate_diff.txt', 'r').read().rstrip())
# EXP_GENERATE_DIFF = {('added', 'group3'): {'fee': '100500'},
#  ('deleted', 'group2'): {'abc': '12345'},
#  ('has_child', 'common'): {('added', 'setting4'): 'blah blah',
#   ('added', 'setting5'): {'key5': 'value5'},
#   ('deleted', 'setting2'): '200',
#   ('deleted', 'setting6'): {'key': 'value'},
#   ('not_changed', 'setting1'): 'Value 1',
#   ('not_changed', 'setting3'): True},
#  ('has_child', 'group1'): {('not_changed', 'foo'): 'bar',
#   ('changed', 'baz'): ('bas', 'bars')}}
EXP_GENERATE_DIFF = {'group3': {'status': 'added', 'value': {'fee': '100500'}}, 'group2': {'status': 'deleted', 'value': {'abc': '12345'}}, 'group1': {'status': 'has_child', 'value': {'foo': {'status': 'not_changed', 'value': 'bar'}, 'baz': {'status': 'changed', 'value1': 'bas', 'value2': 'bars'}}}, 'common': {'status': 'has_child', 'value': {'setting4': {'status': 'added', 'value': 'blah blah'}, 'setting5': {'status': 'added', 'value': {'key5': 'value5'}}, 'setting6': {'status': 'deleted', 'value': {'key': 'value'}}, 'setting2': {'status': 'deleted', 'value': '200'}, 'setting1': {'status': 'not_changed', 'value': 'Value 1'}, 'setting3': {'status': 'not_changed', 'value': True}}}}

EXP = open('./tests/fixtures/exp_json.txt', 'r').read().rstrip()
EXP_REC = open('./tests/fixtures/exp_recursion.txt', 'r').read().rstrip()
EXP_FLAT = open('./tests/fixtures/exp_flat.txt', 'r').read().rstrip()

BEFORE_JSON = './tests/fixtures/before.json'
AFTER_JSON = './tests/fixtures/after.json'
BEFORE_REC_JSON = './tests/fixtures/before_recursion.json'
AFTER_REC_JSON = './tests/fixtures/after_recursion.json'
BEFORE_REC_YAML = './tests/fixtures/before_recursion.yml'
AFTER_REC_YAML = './tests/fixtures/after_recursion.yml'


def test_generate_diff():
    assert generate_diff(BEFORE_REC_JSON, AFTER_REC_JSON, 'json') == EXP_GENERATE_DIFF
    assert generate_diff(BEFORE_REC_YAML, AFTER_REC_YAML, 'yml') == EXP_GENERATE_DIFF


def test_recursive_rendering():
    assert recursive.rendering(EXP_GENERATE_DIFF) == EXP_REC


def test_flat_rendering():
    assert flat.rendering(EXP_GENERATE_DIFF) == EXP_FLAT
