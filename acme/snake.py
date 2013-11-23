#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint


class Python(object):
    def say(self, greeting=None):
        return 'Hiss!' * randint(1, 9)


class MontyPython(Python):
    def say(self, greeting):
        return 'Hello %s' % greeting
