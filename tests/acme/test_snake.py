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
    def test_be_out_of_question(self):
        assert re.match(r'^(Hiss\!)+$', Python().say()), 'シャー'


class TestMontyPython:
    @pytest.mark.parametrize(
        'name',
        [
            'Monty Python', 'John Smith'
        ])
    def test_say_name(self, name):
        assert MontyPython().say(name) == 'Hello ' + name
