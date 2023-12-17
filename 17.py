import sys
import heapq
oo = 99999999999999
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
W, H = len(L[0]), len(L)
p1=p2=oo

M = {}
for y in range(H):
    for x in range(W):
        M[(x,y)] = int(L[y][x])

# loss, pos, dir, steps
init = (0, (0,0), (1,0), 0)
Q = [init,]
visited = set()
dist = {}
while Q:
    loss, here, dir_, step = heapq.heappop(Q)
    if (here,dir_,step) in visited: continue
    visited.add((here,dir_,step))

    if here == (W-1,H-1):
        p1 = loss
        break

    hx,hy = here
    h = [(0,1),(0,-1)] if dir_[0] != 0 else [(1,0),(-1,0)]

    if step < 3:
        hop = hx+dir_[0], hy+dir_[1]
        cell = M.get(hop)
        if cell is not None:
            cc = loss + cell
            if cc < dist.get((hop,dir_,step+1),oo):
                dist[(hop,dir_,step+1)] = cc
                heapq.heappush(Q, (cc,hop,dir_,step+1))

    for nd in h:
        hop = hx+nd[0], hy+nd[1]
        cell = M.get(hop)
        if cell is None: continue
        cc = loss + cell
        if cc < dist.get((hop,nd,0),oo):
            dist[(hop,nd,0)] = cc
            heapq.heappush(Q, (cc,hop,nd,1))

print(p1)


Q = [init,]
visited = set()
dist = {}
while Q:
    loss, here, dir_, step = heapq.heappop(Q)
    if (here,dir_,step) in visited: continue
    visited.add((here,dir_,step))

    if here == (W-1,H-1):
        p2 = loss
        break

    hx,hy = here
    h = [(0,1),(0,-1)] if dir_[0] != 0 else [(1,0),(-1,0)]

    if step < 10:
        hop = hx+dir_[0], hy+dir_[1]
        cell = M.get(hop)
        if cell is not None:
            cc = loss + cell
            if cc < dist.get((hop,dir_,step+1),oo):
                dist[(hop,dir_,step+1)] = cc
                heapq.heappush(Q, (cc,hop,dir_,step+1))

    if step >= 4:
        for nd in h:
            hop = hx+nd[0], hy+nd[1]
            cell = M.get(hop)
            if cell is None: continue
            cc = loss + cell
            if cc < dist.get((hop,nd,0),oo):
                dist[(hop,nd,0)] = cc
                heapq.heappush(Q, (cc,hop,nd,1))

print(p2)
