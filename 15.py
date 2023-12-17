import sys
from collections import OrderedDict, defaultdict
from string import ascii_lowercase
D = open(sys.argv[1]).read().strip()
S = D.split(',')
p1=p2=0


def h(s):
    ax = 0
    for ch in s:
        ax = (ax+ord(ch))*17%256
    return ax

for s in S:
    p1 += h(s)

# print(p1)

B = defaultdict(OrderedDict)

for s in S:
    l = ''
    while s[0] in ascii_lowercase:
        l += s[0]
        s = s[1:]

    op = s[0]
    rem = s[1:]
    box = h(l)

    if op == '-':
        try:
            del B[box][l]
        except KeyError:
            pass
    else:
        fl = int(rem)
        B[box][l] = fl

for bi in range(256):
    for si, fl in enumerate(B[bi].values()):
        p = (bi+1) * (si+1) * fl
        print(bi+1, bi, si+1, si, fl)
        p2 += p

print(p2)
