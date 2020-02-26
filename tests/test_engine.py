from gendiff.engine import get_diff
from gendiff.formatters import recursive, plain, dump
import json
import yaml

EXP_GEN_DIFF = json.loads(open('./tests/fixtures/result/exp_generate_diff.txt', 'r').read().rstrip())
EXP_REC = open('./tests/fixtures/result/exp_recursion.txt', 'r').read().rstrip()
EXP_PLAIN = open('./tests/fixtures/result/exp_flat.txt', 'r').read().rstrip()
BEFORE_REC_JSON = json.loads(open('./tests/fixtures/input/before_recursion.json', 'r').read().rstrip())
AFTER_REC_JSON = json.loads(open('./tests/fixtures/input/after_recursion.json', 'r').read().rstrip())
BEFORE_REC_YAML = yaml.safe_load(open('./tests/fixtures/input/before_recursion.yml', 'r').read().rstrip())
AFTER_REC_YAML = yaml.safe_load(open('./tests/fixtures/input/after_recursion.yml', 'r').read().rstrip())


def test_generate_diff_1():
    assert get_diff(BEFORE_REC_JSON, AFTER_REC_JSON) == EXP_GEN_DIFF


def test_generate_diff_2():
    assert get_diff(BEFORE_REC_YAML, AFTER_REC_YAML) == EXP_GEN_DIFF


def test_recursive_rendering():
    assert recursive.rendering(EXP_GEN_DIFF) == EXP_REC


def test_flat_rendering():
    assert plain.rendering(EXP_GEN_DIFF) == EXP_PLAIN
