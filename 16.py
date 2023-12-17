import sys
from collections import OrderedDict, defaultdict
from string import ascii_lowercase
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
p1=p2=0

H, W = len(L), len(L[0])


MIRROR = {
        '/': {(0,1): (-1,0),
              (0,-1): (1,0),
              (1,0): (0,-1),
              (-1,0): (0,1),},
        '\\': {(0,1): (1,0),
               (0,-1): (-1,0),
               (1,0): (0,1),
               (-1,0): (0,-1)}}

PIPE = {
        '-': {(0,1): ((-1,0),(1,0)),
              (0,-1): ((-1,0),(1,0)),
              (1,0): ((1,0),),
              (-1,0): ((-1,0),),},
        '|': {(0,1): ((0,1),),
              (0,-1): ((0,-1),),
              (1,0): ((0,1),(0,-1)),
              (-1,0): ((0,1),(0,-1)),},}


def shoot(coord, dir_):
    Q = [(0, coord, dir_)]
    V = set()
    VP = set()

    while Q:
        dist, pos, dir_ = Q.pop(0)
        px,py=pos
        dx,dy=dir_
        if not (0 <= px < W and 0 <= py < H): continue
        if (pos, dir_) in V: continue
        V.add((pos,dir_))
        VP.add(pos)

        ch = L[py][px]
        d1 = dist+1
        if ch == '.':
            Q.append((d1, (px+dx,py+dy), dir_))
        elif ch in '\\/':
            dx,dy = MIRROR[ch][dir_]
            Q.append((d1, (px+dx,py+dy), (dx,dy)))
        else:
            for dx,dy in PIPE[ch][dir_]:
                Q.append((d1, (px+dx,py+dy), (dx,dy)))
    return len(VP)

p1 = shoot((0,0),(1,0))
print(p1)


best = 0
for y in range(H):
    best = max(best, shoot((0,y), (1,0)))
    best = max(best, shoot((W-1,y), (-1,0)))
for x in range(W):
    best = max(best, shoot((x,0), (0,1)))
    best = max(best, shoot((x,H-1), (0,-1)))

print(best)
