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

N = 140

s = None
M = {}
for y in range(N):
    for x in range(N):
        M[(x,y)] = L[y][x]
        if L[y][x] == 'S':
            s = (x,y)
print(s)
M[s] = 'L'


visited = set()
queue = [(0, s)]
best = 0
bestpos = None
while queue:
    dist, here = queue.pop(0)
    if here in visited: continue
    visited.add(here)
    
    x, y=  here
    if x  < 0 or x > N: continue
    if y < 0 or y > N: continue
    if dist > best:
        best = dist
        bestpos = here

    if M[here] == '|':
        queue.append((dist+1, (x, y-1)))
        queue.append((dist+1, (x, y+1)))
    elif M[here] == '-':
        queue.append((dist+1, (x-1, y)))
        queue.append((dist+1, (x+1, y)))
    elif M[here] == '7':
        queue.append((dist+1, (x-1, y)))
        queue.append((dist+1, (x, y+1)))
    elif M[here] == 'J':
        queue.append((dist+1, (x-1, y)))
        queue.append((dist+1, (x, y-1)))
    elif M[here] == 'F':
        queue.append((dist+1, (x+1, y)))
        queue.append((dist+1, (x, y+1)))
    elif M[here] == 'L':
        queue.append((dist+1, (x+1, y)))
        queue.append((dist+1, (x, y-1)))
    else:
        raise Exception('uh')


print(best)

asdf = set()
for k, v in M.items():
    if k not in visited:
        asdf.add(k)

for pos in asdf:
    del M[pos]

for y in range(N):
    for x in range(N):
        ch = M.get((x,y), '.')
        ch = 'S' if (x,y) == s else ch
        sys.stdout.write(ch)
    sys.stdout.write('\n')


init = None
for x in range(N):
    if M.get((x,0)):
        init = (x,0)
        break

print(init)

MM = M
M = {}
for (x,y),k in MM.items():
    M[(x,-y)] = k


cfg = {
        '-': set((IVec2(0,1),IVec2(1,1),IVec2(2,1))),
        '|': set((IVec2(1,0),IVec2(1,1),IVec2(1,2))),
        'F': set((IVec2(1,0),IVec2(1,1),IVec2(2,1))),
        '7': set((IVec2(1,0),IVec2(1,1),IVec2(0,1))),
        'L': set((IVec2(1,2),IVec2(1,1),IVec2(2,1))),
        'J': set((IVec2(1,2),IVec2(1,1),IVec2(0,1))),
        }
emptyset = set()


dirs = (IVec2(1,0),IVec2(-1,0),IVec2(0,1),IVec2(0,-1))
queue = [IVec2(0,0)]
visited = set()
reach = IVec2(0,0)
many = 0
while queue:
    here = queue.pop(0)
    x,y = here.x,here.y
    if not (0 <= x < N*3 and -N*3 < y <= 0): continue
    if here in visited: continue
    visited.add(here)

    sx,sy = x%3,y%3
    x,y=x//3,y//3

    ch = M.get((x,y))
    space = cfg.get(ch, emptyset)
    if IVec2(sx,sy) in space:
        continue  # wall

    [queue.append(here + it) for it in dirs]

print('hello')


p2 = 0
for yy in range(N):
    yy = -yy
    for xx in range(N):
        ch = M.get((xx,yy))

        pts = set()
        for py in range(3):
            for px in range(3):
                pts.add(IVec2(xx*3+px, yy*3-py))

        ch = M.get((xx,yy))
        if ch:
            sys.stdout.write('.')
            continue

        if all(it in visited for it in pts):
            sys.stdout.write('O')
            continue
        sys.stdout.write('I')
        p2 += 1
    sys.stdout.write('\n')


print(p2)

'''
init = IVec2(init[0], init[1])
pos = init
head = IVec2(0,1)
ofs = IVec2(1,-1)

steps = 0
print(init, head, ofs)

inner = set()
while steps==0 or init != pos:
    # print(steps, pos, head)
    if M.get((pos+ofs).t()) is None:
        inner.add(pos+ofs)
    m = M[pos.t()]
    if m == 'F':
        d = 'R' if head == IVec2(0,1) else 'L'
        # print('<F>', m, d, head)
        head = head.rot(d)
        # print('>', head)
        ofs = ofs.rot(d)
    elif m == 'J':
        d = 'R' if head == IVec2(0,-1) else 'L'
        head = head.rot(d)
        ofs = ofs.rot(d)
    elif m == 'L':
        d = 'L' if head == IVec2(0,-1) else 'R'
        head = head.rot(d)
        ofs = ofs.rot(d)
    elif m == '7':
        d = 'R' if head == IVec2(1,0) else 'L'
        head = head.rot(d)
        ofs = ofs.rot(d)
    pos += head
    steps += 1

print('yay', steps)
print(inner)



visited = set()
queue = list(inner)
i2 = set()
p2 = 0
while queue:
    here = queue.pop(0)
    if here in visited: continue
    visited.add(here)
    
    x,y=here.x,here.y
    if x < 0 or x >= N: continue
    if y > 0 or y <= -N: continue

    ch = M.get(here.t())
    if ch is None:
        i2.add(here)
        p2 += 1

        for nd in (IVec2(-1,0),IVec2(1,0),IVec2(0,1),IVec2(0,-1)):
            np = here + nd
            queue.append(np)


for y in range(N):
    for x in range(N):
        coord = IVec2(x,-y)
        ch = '.' if M.get(coord.t()) else ' '
        ch = 'X' if coord in i2 else ch

        sys.stdout.write(ch)
    sys.stdout.write('\n')



print(p2)
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
