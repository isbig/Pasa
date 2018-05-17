import numpy as np
import random

#เพิ่มขนาดของ emb_word
def permsize(emwd):
    i = 0
    n = 0
    samashic_text = np.arange((len(emwd))*2)
    while i < len(emwd):
        b = random.choice(range(10))
        samashic_text[n] = emwd[i] - b
        samashic_text[n + 1] = b
        if samashic_text[n] < 0:
            samashic_text[n] = samashic_text[n] + 9
        n = n + 2
        i = i + 1
    return samashic_text

#เพิ่มขนาดของ emb_word กี่รอบ
def permrob(rob):
    n = random.choice(range(10))
    a = np.array([n])
    i = 0 
    while i in range(rob):
        a = permsize(a)
        i = i + 1 
    return a

import psycopg2

a = permrob(4)
print(a)
b = list(a)
print(b)
c = a.tolist()
print(c)
d = [4, 4, 6, 7]
