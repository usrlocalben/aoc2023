import sys
import math
import heapq
import random
from collections import defaultdict as DD
from math import gcd, lcm
oo = 0x3f3f3f3f3f3f3f3f
from pprint import pprint
from lib import refstr, IVec2, NSEW
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
p1=p2=0

IN = DD(set)
OUT = DD(list)
TYP = {}

B = []
for l in L:
    id_, dests = l.split(' -> ')
    dests = set(dests.replace(',','').split())
    if id_ == 'broadcaster':
        [B.append(it) for it in dests]
    else:
        typ = 'F' if id_[0] == '%' else 'J'
        id_ = id_[1:]
        TYP[id_] = typ

    for d in dests:
        IN[d].add(id_)
    for d in dests:
        OUT[id_].append(d)

MEM = DD(dict)
for id_, typ in TYP.items():
    if typ == 'J':
        for n in IN[id_]:
            MEM[id_][n] = False

FF = {id_: False for id_,typ in TYP.items() if typ == 'F'}

sc = {False: 0, True: 0}

n = 0
p2 = None

p2c = {}

while True:
    if n == 1000:
        p1 = sc[False] * sc[True]

    if p1 and p2:
        break
    n += 1
    
    # sys.stdout.write('.')
    # sys.stdout.flush()
    sc[False] += 1
    Q = [('broadcast', dst, False) for dst in B]
    while Q:
        src, dst, sig = Q.pop(0)
        sc[sig] += 1
        if dst in ('cl','rp','lb','nj') and not sig and dst not in p2c:
            p2c[dst] = n
        if len(p2c) == 4:
            p2 = 1
            for nn in p2c.values():
                p2 = math.lcm(p2, nn)

        try:
            typ = TYP[dst]
        except KeyError:
            continue

        outs = OUT[dst]
        if typ == 'J':
            MEM[dst][src] = sig
            level = all(MEM[dst].values())
            for dd in outs:
                Q.append((dst, dd, not level))
        else:
            if sig:
                pass
            else:
                FF[dst] = not FF[dst]
                for dd in outs:
                    Q.append((dst, dd, FF[dst]))


print(p1)
print(p2)
