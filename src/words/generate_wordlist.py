# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/30
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

import random


class WordFactory(object):
    """fuzz word factory

    """

    def generate_big_string(self, generate_lambda_list: list, length: int):
        ls = []
        for _ in range(length):
            index = random.randint(0, len(generate_lambda_list) - 1)
            ls.append(f"{generate_lambda_list[index]()}")
        return "".join(ls)

    def generate_invisible_characters(self):
        return '\x00'

def randletter(x, y):
    return chr(random.randint(ord(x), ord(y)))


if __name__ == '__main__':
    word = WordFactory()
    generate_int_0_9 = lambda: random.randint(0, 9)
    generate_string_a_z = lambda: randletter('a', 'z')

    generate_lambda_list = [generate_int_0_9, generate_string_a_z]
    # print(word.generate_big_string(generate_lambda_list, 10000))
    print(word.generate_invisible_characters())
