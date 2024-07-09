#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ultimate_answer():
    return 42


class Python:
    def say(self, greeting=None):
        return 'Hiss!'


class MontyPython(Python):
    def say(self, greeting):
        return 'Hello %s' % greeting
