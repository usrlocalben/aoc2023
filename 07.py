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

cc  = 'AKQJT98765432'
cc2 = 'AKQT98765432J'

def typ(h):
    e = [ch for ch in h]
    s = [cc.find(x) for x in e]
    tmp = defaultdict(int)
    for v in s:
        tmp[v] += 1
    print(h, tmp)
    for k, v in tmp.items():
        if v == 5:
            return 0
        if v == 4:
            return 1
        if v == 3:
            if len(tmp) == 2:
                return 2
            else:
                return 3

    if len(tmp) == 5:
        return 6
    if len(tmp) == 4:
        return 5
    if len(tmp) == 3:
        return 4


    raise Exception(f"oops {tmp}")


def typ2(h):
    F = defaultdict(int)
    for ch in h:
        F[ch] += 1
    # print(h, F)
    for k, v in F.items():
        if v == 5:
            return 0  # 5K
        if v == 4:
            if F['J'] > 0:
                return 0  # 4K + J = 5K
            return 1  # 4K
        if v == 3:
            if len(F) == 2:
                # 3 + 2
                if F['J'] > 0:
                    return 0  # upgrade to 5K
                else:
                    return 2  # 3K + 2K
            else:
                # 3 + 1 + 1
                if F['J'] == 1:
                    return 1  # 3K -> 4K
                elif F['J'] == 3:
                    return 1
                else:
                    return 3

    if len(F) == 5:
        if F['J'] == 1:
            return 5  # upgrade to one pair
        return 6  # high card
    if len(F) == 4:
        # one pair
        if F['J'] == 2:
            return 3  # upgrade 2J to 3K
        elif F['J'] == 1:
            return 3  # upgrade to 3K
        return 5
    if len(F) == 3:
        # 3 types, but not a 3K = 2+2+1
        if F['J'] == 1:
            return 2  # upgrade to full house
        if F['J'] == 2:
            return 1  # upgrade to 4K
        return 4


def cmp(a_, b_):
    a = a_[0]
    b = b_[0]
    va = typ(a)
    vb = typ(b)
    if va < vb:
        return -1
    elif va > vb:
        return 1
    else:
        sa = [cc.find(x) for x in a]
        sb = [cc.find(x) for x in b]
        return -1 if sa < sb else 1

def cmp2(a_, b_):
    a = a_[0]
    b = b_[0]
    va = typ2(a)
    vb = typ2(b)
    if va < vb:
        return -1
    elif va > vb:
        return 1
    else:
        sa = [cc2.find(x) for x in a]
        sb = [cc2.find(x) for x in b]
        return -1 if sa < sb else 1



ax = []
for l in lines:
    h, bid = l.split()
    bid = int(bid)
    ax.append((h, bid))

from functools import cmp_to_key
ax.sort(key=cmp_to_key(cmp), reverse=True)

print(ax)

i = 1
for h, bid in ax:
    p1 += bid *i
    i += 1






print(p1)


ax = []
for l in lines:
    h, bid = l.split()
    bid = int(bid)
    ax.append((h, bid))

ax.sort(key=cmp_to_key(cmp2), reverse=True)

print(ax)

i = 1
for h, bid in ax:
    p2 += bid *i
    i += 1
print(p2)
