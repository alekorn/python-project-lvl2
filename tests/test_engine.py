from diff.engine import generate_diff
from diff.formatters import json_format
import json

# EXP_GENERATE_DIFF = json.loads(open('./tests/fixtures/exp_generate_diff.txt', 'r').read().rstrip())
EXP_GENERATE_DIFF = {('added', 'group3'): {'fee': '100500'},
 ('deleted', 'group2'): {'abc': '12345'},
 ('has_child', 'common'): {('added', 'setting4'): 'blah blah',
  ('added', 'setting5'): {'key5': 'value5'},
  ('deleted', 'setting2'): '200',
  ('deleted', 'setting6'): {'key': 'value'},
  ('not_changed', 'setting1'): 'Value 1',
  ('not_changed', 'setting3'): True},
 ('has_child', 'group1'): {('not_changed', 'foo'): 'bar',
  ('changed', 'baz'): ('bas', 'bars')}}
EXP = open('./tests/fixtures/exp_json.txt', 'r').read().rstrip()
EXP_REC = open('./tests/fixtures/exp_recursion.txt', 'r').read().rstrip()

BEFORE_JSON = './tests/fixtures/before.json'
AFTER_JSON = './tests/fixtures/after.json'
BEFORE_YAML = './tests/fixtures/before.yml'
AFTER_YAML = './tests/fixtures/after.yml'
BEFORE_REC_JSON = './tests/fixtures/before_recursion.json'
AFTER_REC_JSON = './tests/fixtures/after_recursion.json'
BEFORE_REC_YAML = './tests/fixtures/before_recursion.yaml'
AFTER_REC_YAML = './tests/fixtures/after_recursion.yaml'


def test_json_format_rendering():
    assert json_format.rendering(generate_diff(BEFORE_JSON, AFTER_JSON, 'json')) == EXP
    assert json_format.rendering(EXP_GENERATE_DIFF) == EXP_REC


def test_yaml_format_rendering():
    assert json_format.rendering(EXP_GENERATE_DIFF) == EXP_REC


def test_generate_diff():
    assert generate_diff(BEFORE_REC_JSON, AFTER_REC_JSON, 'json') == EXP_GENERATE_DIFF
