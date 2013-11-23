#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
サンプルテスト
"""

import re


def pytest_generate_tests(metafunc):
    """
    Parametrizing test methods through per-class configuration
    http://pytest.org/latest-ja/example/parametrize.html#id5
    """
    try:
        funcarglist = metafunc.cls.params[metafunc.function.__name__]
    except AttributeError:
        return
    argnames = list(funcarglist[0])
    metafunc.parametrize(
        argnames,
        [[funcargs[name] for name in argnames] for funcargs in funcarglist]
    )


class TestPython:
    def test_be_out_of_question(self):
        from acme.snake import Python
        assert re.match(r'^(Hiss\!)+$', Python().say()), 'シャー'


class TestMontyPython:
    params = {
        'test_say_name': [
            dict(name='Monty Python'),
            dict(name='John Smith'),
        ],
    }

    def test_say_name(self, name):
        from acme.snake import MontyPython
        assert MontyPython().say(name) == 'Hello ' + name
