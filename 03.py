import sys
from collections import defaultdict
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
p1=p2=0

gears = set()
syms = set()
dim = 140
for y in range(dim):
    for x in range(dim):
        if lines[y][x] not in '.0123456789':
            syms.add((x,y))
        if lines[y][x] == '*':
            gears.add((x,y))

nums = {}
for y in range(dim):
    x = 0
    while x < dim:
        if lines[y][x] in '0123456789':
            ax = ''
            begin = x
            while x < dim and lines[y][x] in '0123456789':
                ax += lines[y][x]
                x += 1

            for xx in range(begin,x):
                nums[(xx,y)] = int(ax)

            for yy in range(y-1,y+2,1):
                for xx in range(begin-1,x+1):
                    if (xx,yy) in syms:
                        p1 += int(ax)
                        print(ax, begin, x)
        x += 1

for gx,gy in gears:
    foo = set()
    for yy in (-1,0,1):
        yy += gy
        for xx in (-1,0,1):
            xx += gx
            if (xx,yy) in nums:
                foo.add(nums[(xx,yy)])
    if len(foo) > 1:
        blah = list(foo)
        p2 += blah[0] * blah[1]

print(p1)
print(p2)
