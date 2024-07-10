#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ultimate_answer() -> int:
    return 42


class Python:
    def say(self, greeting: str = '') -> str:
        return 'Hiss!'


class MontyPython(Python):
    def say(self, greeting: str = '') -> str:
        return 'Hello %s' % greeting
