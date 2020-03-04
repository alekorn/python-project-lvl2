from gendiff.engine import get_diff
from gendiff import format
from gendiff.loaders import json_load, yaml_load, txt_load
from gendiff import generate_diff
import json

EXP_GEN_DIFF = './tests/fixtures/result/exp_generate_diff.json'
EXP_REC = './tests/fixtures/result/exp_recursion.txt'
EXP_PLAIN = './tests/fixtures/result/exp_plain.txt'
EXP_DUMP = './tests/fixtures/result/exp_dump.txt'

BEFORE_REC_JSON = './tests/fixtures/input/before_recursion.json'
AFTER_REC_JSON = './tests/fixtures/input/after_recursion.json'
BEFORE_REC_YAML = './tests/fixtures/input/before_recursion.yml'
AFTER_REC_YAML = './tests/fixtures/input/after_recursion.yml'


def test_get_diff1():
    assert get_diff(json_load(BEFORE_REC_JSON
        ), json_load(AFTER_REC_JSON)) == json_load(EXP_GEN_DIFF)


def test_get_diff2():
    assert get_diff(yaml_load(BEFORE_REC_YAML
        ), yaml_load(AFTER_REC_YAML)) == json_load(EXP_GEN_DIFF)


def test_recursive_rendering():
    assert format.default(json_load(EXP_GEN_DIFF)) == txt_load(EXP_REC)


def test_plain_rendering():
    assert format.plain(json_load(EXP_GEN_DIFF)) == txt_load(EXP_PLAIN)


def test_dump_rendering():
    assert format.json(json_load(EXP_GEN_DIFF)
            ) == json.dumps(json_load(EXP_GEN_DIFF), indent=4)


def test_generate_diff1():
    assert generate_diff(
            BEFORE_REC_JSON,
            AFTER_REC_JSON,
            'default'
            ) == txt_load(EXP_REC)


def test_generate_diff2():
    assert generate_diff(
            BEFORE_REC_YAML,
            AFTER_REC_YAML,
            'default'
            ) == txt_load(EXP_REC)


def test_generate_diff3():
    assert generate_diff(
            BEFORE_REC_JSON,
            AFTER_REC_JSON,
            'plain'
            ) == txt_load(EXP_PLAIN)


def test_generate_diff4():
    assert generate_diff(
            BEFORE_REC_JSON,
            AFTER_REC_JSON,
            'json'
            ) == json.dumps(json_load(EXP_GEN_DIFF), indent=4)
