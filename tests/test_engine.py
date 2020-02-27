from gendiff.engine import get_diff
from gendiff.formatters import recursive, plain, dump
from gendiff.fileloader import json_load, yaml_load, txt_load
from gendiff import generate_diff

EXP_GEN_DIFF = json_load('./tests/fixtures/result/exp_generate_diff.json')
EXP_REC = txt_load('./tests/fixtures/result/exp_recursion.txt')
EXP_PLAIN = txt_load('./tests/fixtures/result/exp_plain.txt')
EXP_DUMP = txt_load('./tests/fixtures/result/exp_dump.txt')

BEFORE_REC_JSON = json_load('./tests/fixtures/input/before_recursion.json')
AFTER_REC_JSON = json_load('./tests/fixtures/input/after_recursion.json')
BEFORE_REC_YAML = yaml_load('./tests/fixtures/input/before_recursion.yml')
AFTER_REC_YAML = yaml_load('./tests/fixtures/input/after_recursion.yml')


def test_get_diff_1():
    assert get_diff(BEFORE_REC_JSON, AFTER_REC_JSON) == EXP_GEN_DIFF


def test_get_diff_2():
    assert get_diff(BEFORE_REC_YAML, AFTER_REC_YAML) == EXP_GEN_DIFF


def test_recursive_rendering():
    assert recursive.rendering(EXP_GEN_DIFF) == EXP_REC


def test_plain_rendering():
    assert plain.rendering(EXP_GEN_DIFF) == EXP_PLAIN


def test_dump_rendering():
    assert dump.rendering(EXP_GEN_DIFF) == EXP_DUMP


def test_generate_diff_1():
    assert generate_diff(
            './tests/fixtures/input/before_recursion.json',
            './tests/fixtures/input/after_recursion.json',
            'json'
            ) == EXP_REC


def test_generate_diff_2():
    assert generate_diff(
            './tests/fixtures/input/before_recursion.yml',
            './tests/fixtures/input/after_recursion.yml',
            'yaml'
            ) == EXP_REC


def test_generate_diff_3():
    assert generate_diff(
            './tests/fixtures/input/before_recursion.json',
            './tests/fixtures/input/after_recursion.json',
            'plain'
            ) == EXP_PLAIN


def test_generate_diff_4():
    assert generate_diff(
            './tests/fixtures/input/before_recursion.json',
            './tests/fixtures/input/after_recursion.json',
            'dump'
            ) == EXP_DUMP
