#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ultimate_answer() -> int:
    return 42


class Python:
    def say(self) -> str:
        return 'Hiss!'


class MontyPython(Python):
    def __init__(self, name: str):
        self.name = name

    def say(self) -> str:
        return f'Hello {self.name}'
