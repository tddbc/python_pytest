#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
サンプルテスト
"""

import pytest

from acme.snake import ultimate_answer, Python, MontyPython


def test_ultimate_answer():
    assert ultimate_answer() == 42


class TestPython:
    def test_say(self):
        # Arrange
        # sut = System Under Test
        sut = Python()
        # Act
        actual = sut.say()
        # Assert
        assert actual == 'Hiss!'


class TestMontyPython:
    @pytest.mark.parametrize(
        'name, expected',
        [
            ('Monty Python', 'Hello Monty Python'),
            ('John Smith', 'Hello John Smith'),
        ])
    def test_say_name(self, name, expected):
        # Arrange
        sut = MontyPython(name)
        # Act
        actual = sut.say()
        # Assert
        assert actual == expected
