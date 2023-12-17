import sys
import math
import random
from collections import defaultdict
from math import gcd, lcm
oo = 0x3f3f3f3f3f3f3f3f
from pprint import pprint
from lib import refstr, Vec2, NSEW
lines = open(sys.argv[1]).read().strip().split('\n')
p1, p2 = 0, 0
from functools import cmp_to_key

ins = lines[0]

M = {}
for line in lines[2:]:
    s, dl, dr = line.replace('(', '').replace(')','').replace('=','').replace(',','').split()
    M[s] = (dl, dr)
   
i = 0
# pos = 'AAA'

cyc = {}

init = list(set(k for k in M.keys() if k.endswith('A')))
hit = {}
for h in init:
    visited = {}
    foo = set()
    i = 0
    s = 0
    hh = h
    while True:
        if hh.endswith('Z') and hh not in foo:
            foo.add(hh)
            hit[h] = s
            print(h, 'end at', hh, s, i)
        if (i, hh) in visited:
            cyc[h] = (hh, s)
            print(h, 'cycle at', s, i, hh, visited[(i,hh)])
            break
        visited[(i,hh)] = s
        x = 0 if ins[i] == 'L' else 1
        hh = M[hh][x]
        i = (i+1)%len(ins)
        s += 1

lead = {}
init = list(set(k for k in M.keys() if k.endswith('A')))
for h in init:
    i = 0
    s = 0
    hh = h
    while hh != cyc[h][0]:
        x = 0 if ins[i] == 'L' else 1
        hh = M[hh][x]
        i = (i+1)%len(ins)
        s += 1
    lead[h] = s

print(lead)

p2 = 1
for h, l in lead.items():
    p2 = math.lcm(p2, hit[h])
    print(h, l, cyc[h][1], cyc[h][1]-l, hit[h])

print(p2)

'''
while not all(it.endswith('Z') for it in pos):
    x = 0 if ins[i%len(ins)] == 'L' else 1
    i += 1
    pos = set(M[it][x] for it in pos)
    #pos = M[pos][x]

print(i)
'''  
