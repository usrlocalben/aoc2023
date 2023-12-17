import sys
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
w = len(L[0])
h = len(L)
p1=p2=0

def tilt(m):
    u = {}
    for (x,y), typ in m.items():
        if typ == '#' or y==0:
            u[(x,y)] = typ
        else:
            if (x,y-1) not in m:
                u[(x,y-1)] = typ
            else:
                u[(x,y)] = typ
    return u

C = set()
R = set()
for y in range(h):
    for x in range(w):
        ch = L[y][x]
        pos = (x,y)
        if ch == 'O':
            R.add(pos)
        elif ch == '#':
            C.add(pos)
        else:
            pass
# print(len(R))


def rot(m):
    u = {}
    for y in range(h):
        for x in range(w):
            # dst = (x,h-y-1)
            elem = m.get((x,y))
            if elem:
                u[(h-y-1,x)] = elem
    return u


def tilt_until_settled(m):
    a = m
    while True:
        b = tilt(a)
        if b == a:
            break
        a = b
    return a


M = {}
for it in C: M[it] = '#'
for it in R: M[it] = 'O'

a = tilt_until_settled(M)

for y in range(h):
    for x in range(w):
        sys.stdout.write(a.get((x,y), '.'))
    sys.stdout.write('\n')

a = rot(a)
print('---------------------------------------------------')
for y in range(h):
    for x in range(w):
        sys.stdout.write(a.get((x,y), '.'))
    sys.stdout.write('\n')


for y in range(h):
    p1 += (h-y) * sum(1 if a.get((x,y)) == 'O' else 0 for x in range(w))

print(p1)

visited = {}
a = M
n = 0
while True:

    for _ in range(4):
        a = tilt_until_settled(a)
        a = rot(a)

    n += 1
    state = frozenset(k for k,v in a.items() if v == 'O')
    if state in visited:

        print('cycle detect after', n, 'ops, first n was', visited[state])
        cycle_len = n - visited[state]
        si = (1000000000 - visited[state]) % cycle_len + visited[state]

        for k, v in visited.items():
            if v == si:
                final = k
                break
        break
    visited[state] = n


for y in range(h):
    p2 += (h-y) * sum(1 if (x,y) in final else 0 for x in range(w))

print(p2)
