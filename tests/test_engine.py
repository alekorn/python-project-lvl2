from diff.engine import generate_diff
from diff.formatters import recursive, flat
import json

EXP_GEN_DIFF = json.loads(open('./tests/fixtures/result/exp_generate_diff.txt', 'r').read().rstrip())
EXP_REC = open('./tests/fixtures/result/exp_recursion.txt', 'r').read().rstrip()
EXP_FLAT = open('./tests/fixtures/result/exp_flat.txt', 'r').read().rstrip()
BEFORE_REC_JSON = './tests/fixtures/input/before_recursion.json'
AFTER_REC_JSON = './tests/fixtures/input/after_recursion.json'
BEFORE_REC_YAML = './tests/fixtures/input/before_recursion.yml'
AFTER_REC_YAML = './tests/fixtures/input/after_recursion.yml'


def test_generate_diff_1():
    assert generate_diff(BEFORE_REC_JSON, AFTER_REC_JSON, 'json') == EXP_GEN_DIFF


def test_generate_diff_2():
    assert generate_diff(BEFORE_REC_YAML, AFTER_REC_YAML, 'yml') == EXP_GEN_DIFF


def test_recursive_rendering():
    assert recursive.rendering(EXP_GEN_DIFF) == EXP_REC


def test_flat_rendering():
    assert flat.rendering(EXP_GEN_DIFF) == EXP_FLAT
