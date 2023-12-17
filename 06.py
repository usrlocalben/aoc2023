import sys
import math
import random
from collections import defaultdict
from math import gcd, lcm
oo = 99999999999999
from pprint import pprint
from lib import refstr, Vec2, NSEW
lines = open(sys.argv[1]).read().strip().split('\n')
p1, p2 = 0, 0

T = [int(x) for x in lines[0].split(':')[1].split()]
D = [int(x) for x in lines[1].split(':')[1].split()]
R = 1

p1 = 1
for i in range(4):
    tt = T[i]
    record = D[i]
    # print(tt,record)

    memo = {}

    def R(d, rt, rem, rel):
        # print(d,rt,rem)
        if (d,rt,rem,rel) in memo:
            return memo[(d,rt,rem,rel)]
        if rem == 0:
            return int(d < 0)
        foo = 0
        foo += R(d-rt, rt, rem-1, True)
        if not rel:
            foo += R(d, rt+1, rem-1, False)
        memo[(d,rt,rem,rel)] = foo
        return foo

    cnt = R(record, 0, tt, False)
    p1 *= cnt
    # print(cnt)

print(p1)


DD = int(''.join(str(n) for n in D))
TT = int(''.join(str(n) for n in T))
'''
(TT-n) * n > DD = win
'''


while True:
    n = random.randint(0,TT)
    if (TT-n)*n < DD:
        break

hit = n

lo = 0
hi = hit
while hi-lo > 2:
    mid = (lo+hi)//2
    if (TT-mid)*mid < DD:
        lo = mid
    else:
        hi = mid

n = lo
while (TT-n)*n < DD:
    n += 1
begin = n



lo = hit
hi = TT
while hi-lo > 2:
    mid = (lo+hi)//2
    if (TT-mid)*mid < DD:
        hi = mid
    else:
        lo = mid
n = hi
while (TT-n)*n < DD:
    n -= 1
end = n + 1

print(end - begin)












#print(p1)
#print(p2)
