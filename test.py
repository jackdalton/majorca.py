#!/usr/bin/env python
# coding=utf-8

from majorca import Majorca

key = 2425967623052370772757633156976982469681

crypto = Majorca(key)
enc = crypto.encrypt("This is a test.")
print(enc)
print(crypto.decrypt(enc))
