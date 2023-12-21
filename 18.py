import sys
import heapq
from lib import IVec2
from collections import defaultdict, OrderedDict
oo = 99999999999999
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
W, H = len(L[0]), len(L)
p1=p2=0


M = {}
pos = IVec2(0, 0)

bot_left = IVec2(oo,oo)
top_right = IVec2(-oo,-oo)

for l in L:
    d, n, _ = l.split()
    n = int(n)
    vec = {'R':IVec2(1,0),'L':IVec2(-1,0),'D':IVec2(0,-1),'U':IVec2(0,1)}.get(d)
    ch = {'R':'-','L':'-','U':'|','D':'|'}.get(d)
    for _ in range(n):
        pos += vec
        bot_left = IVec2.vmin(bot_left, pos)
        top_right = IVec2.vmax(top_right, pos)
        M[pos] = ch

top_right += 1  # half-open
DIM = top_right - bot_left
# print(bot_left, DIM)

# find a point that is inside the space
inside = None
for y in range(bot_left.y, top_right.y):
    vt = set()
    bad = False
    for x in range(bot_left.x, top_right.x):
        coord = IVec2(x,y)
        if M.get(coord) == '|':
            vt.add(coord)
        elif M.get(coord) == '-':
            bad = True
            break
    if not bad and len(vt) == 2:
        vt = list(vt)
        a, b = vt[0], vt[1]
        mid = (a.x+b.x)//2
        inside = IVec2(mid, y)
        break

Q = [inside]
V = set()
while Q:
    pos = Q.pop(0)
    if pos in M: continue
    if pos in V: continue
    V.add(pos)
    for vec in (IVec2(1,0), IVec2(-1,0),
                IVec2(0,1), IVec2(0,-1)):
        Q.append(pos + vec)

p1 = len(V)+len(M)
print(p1)



bot_left = IVec2(oo,oo)
top_right = IVec2(-oo,-oo)
ux = set()
uy = set()
init = IVec2(0,0)
pos = init
RDLU = {'R': IVec2(1,0), 'D': IVec2(0,-1), 'L': IVec2(-1,0), 'U': IVec2(0,1)}
ux.add(pos.x)
uy.add(pos.y)
for l in L:
    _, _, h = l.split()
    c = int(h[2:-1], 16)
    amt = c >> 4;
    dir_ = 'RDLU'[c & 0xf]
    pos += RDLU[dir_] * amt
    ux.add(pos.x)
    uy.add(pos.y)
    bot_left = bot_left.vmin(pos)
    top_right = top_right.vmax(pos)


# print(bot_left, top_right, top_right+1-bot_left)
# print(len(ux), len(uy))

uy = sorted(uy)
ux = sorted(ux)
uy = uy + [uy[-1]+1]
ux = ux + [ux[-1]+1]

moves = []
for l in L:
    _, _, h = l.split()
    c = int(h[2:-1], 16)
    amt = c>>4;
    vec = RDLU['RDLU'[c&0xf]]
    moves.append((vec, amt))


p2 = 0
for yj in range(len(uy)-1):
    ya, yb = uy[yj], uy[yj+1]

    lines = []
    cross = set()
    p = init
    for vec, amt in moves:
        pp = p + vec * amt
        if p.y == pp.y and p.y == ya:  # horz. line
            left_x = min(p.x, pp.x)
            right_x = max(p.x, pp.x)
            lines.append((left_x, right_x))
        if p.x == pp.x:  # vert. line
            top_y = max(p.y, pp.y)
            bot_y = min(p.y, pp.y)
            if bot_y <= ya and (yb-1) <= top_y:
                cross.add(p.x)
        p = pp

    pit = False
    for xj in range(len(ux)-1):
        xa, xb = ux[xj], ux[xj+1]

        line_hit = False
        for l,r in lines:
            if l <= xa and (xb-1) <= r:
                line_hit = True
                break

        point_hit = False
        for l,r in lines:
            if l <= xa and xa <= r:
                point_hit = True
                break
            
        b_bl = IVec2(xa, ya)
        b_tr = IVec2(xb, yb)

        dim = b_tr - b_bl
        if pit:
            if b_bl.x in cross:
                pit = not pit
                if line_hit:
                    p2 += dim.y + dim.x - 1
                else:
                    p2 += dim.y
            else:
                p2 += dim.x * dim.y
        else:
            if b_bl.x in cross:
                pit = not pit
                p2 += dim.x * dim.y
            else:
                if line_hit:
                    p2 += dim.x
                elif point_hit:
                    p2 += 1

print(p2)


            

        




