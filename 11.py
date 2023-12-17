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

dx = D.find('\n')
dy = len(L)


G = set()
for y in range(dy):
    for x in range(dx):
        if L[y][x] == '#':
            G.add((x,y))


exp = 1000000

gg = set()
gt = set(G)
sx = 0
while gt:
    gx = set()
    gg_tmp = set()
    for x,y in gt:
        if x == sx:
            gg_tmp.add((x,y))
        else:
            gx.add((x,y))
    if gg_tmp:
        for it in gg_tmp:
            gg.add(it)
        sx += 1
        gt = gx
    else:
        gt = set((x+exp-1,y) for x, y in gx)
        sx = sx + exp




gt = set(gg)
gg = set()
sy = 0
while gt:
    gx = set()
    gg_tmp = set()
    for x,y in gt:
        if y == sy:
            gg_tmp.add((x,y))
        else:
            gx.add((x,y))
    if gg_tmp:
        [gg.add(it) for it in gg_tmp]
        sy += 1
        gt = gx
    else:
        print('EXP Y', sy, sy+exp)
        gt = set((x,y+exp-1) for x, y in gx)
        sy = sy + exp

#print('len after y', len(gg))
print('size now', (sx,sy))
dx,dy=sx+1,sy+1




pairs = set()
dists = {}
for a in gg:
    for b in gg:
        if a is b: continue
        lo = min(a,b)
        hi = max(a,b)
        pairs.add((lo,hi))
        lx,ly = lo
        hx,hy = hi
        dist = abs(hx-lx) + abs(hy-ly)
        dists[(lo,hi)] = dist

print(sum(it for it in dists.values()))

'''
sys.exit(1)
dists = {}

pts = list(gg)
for j in range(len(pts)):

    if len(dists) == len(pairs):
        break
        
    src = pts[j]
    print(src)

    remaining = set(gg)
    remaining.remove(src)
    visited = set()
    queue = [(0, src)]
    while queue and remaining:
        dist, here = queue.pop(0)
        x,y=here
        if not (0 <= x < dx and 0 <= y <= dy): continue
        if here in visited: continue
        visited.add(here)

        if here in gg and here != src:
            remaining.remove(here)
            pair = (src,here) if src < here else (here,src)
            # print('pair', pair)
            dists[pair] = dist
        queue.append((dist+1, (x-1,y)))
        queue.append((dist+1, (x+1,y)))
        queue.append((dist+1, (x,y-1)))
        queue.append((dist+1, (x,y+1)))


print(len(dists))
print(sum(v for v in dists.values()))
# print(p1)

'''

'''
BFS
visited = set()
queue = [(0, init)]
while queue:
    dist, here = queue.pop(0)
    if here in visited: continue
    visited.add(here)
    if here is target:
        p1 = dist
        break
    # next steps with dist+1
'''

'''
djykstra
queue = []
visited = set()
dist = {}
heapq.heappush(queue, (0, init))
while queue:
    dist, here = heapq.heappop(queue)
    if here in visited: continue
    visited.add(here)

    # do stuff

    cand_cost = dist.get(here,oo)+cost
    if cand_cost < dist.get(next,oo):
        dist[next] = cand_cost
        heapq.heappush(queue, (cand_cost, next))
'''
