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

a = permrob(4)
print(a)
b = list(a)
print(b)
c = a.tolist()
print(c)
d = [4, 4, 6, 7]

import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()
try:
    cur.execute("CREATE TABLE test (word text, emw integer[]);")
except psycopg2.ProgrammingError:
    conn.rollback()
    
text = "ความรัก"
a = permrob(4)
c = a.tolist()
cur.execute("INSERT INTO test VALUES (%(str)s, %(integer[])s);", {'str':text, 'integer[]':c})
cur.execute("SELECT * FROM public.test;")
m = cur.fetchall()
for row in m:    
    print(row)
conn.commit()
cur.close()
conn.close()
