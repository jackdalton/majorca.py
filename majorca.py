#!/usr/bin/env python
# coding=utf-8

class Majorca(object):
    def __init__(self, key):
        super(Majorca, self).__init__()
        self.key = key
    def encrypt(self, text):
        blocks = []
        out = ""
        for i in text:
            blocks.append(ord(i))
        for i in range(len(blocks)):
            blocks[i] = blocks[i] * self.key
        for i in blocks:
            out += str(i) + "?"
        out = out[:-1]
        return out
    def decrypt(self, text):
        blocks = text.split("?")
        out = ""
        for i in blocks:
            i_num = int(i)
            out += chr(i_num / self.key)
        return out
