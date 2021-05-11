#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
サンプルテスト
"""

import pytest
from acme.snake import Python, MontyPython


def test_python_hisses():
    sut = Python()
    actual = sut.say()
    assert 'Hello' not in actual, 'PythonはHelloと言わない'


@pytest.fixture
def monty_python():
    return MontyPython()


class TestMontyPython:
    def test_say_name_guido(self, monty_python):
        actual = monty_python.say('Guido')
        assert actual == 'Hello Guido'

    def test_say_name_kent(self, monty_python):
        actual = monty_python.say('Kent')
        assert actual == 'Hello Kent'

    @pytest.mark.parametrize(
        "name, expected",
        [
            ('Terry', 'Hello Terry'),
            ('John', 'Hello John'),
        ]
    )
    def test_say_name(self, monty_python, name, expected):
        actual = monty_python.say(name)
        assert actual == expected
