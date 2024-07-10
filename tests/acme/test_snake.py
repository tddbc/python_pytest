#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
サンプルテスト
"""

import pytest
import re

from acme.snake import ultimate_answer, Python, MontyPython


def test_ultimate_answer():
    assert ultimate_answer() == 42


class TestPython:
    def test_say(self):
        assert Python().say() == 'Hiss!'


class TestMontyPython:
    @pytest.mark.parametrize(
        'name, expected',
        [
            ('Monty Python', 'Hello Monty Python'),
            ('John Smith', 'Hello John Smith'),
        ])
    def test_say_name(self, name, expected):
        sut = MontyPython(name)
        assert sut.say() == expected
