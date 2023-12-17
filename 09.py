import sys
import math
import heapq
import random
from collections import defaultdict as DD
from math import gcd, lcm
oo = 0x3f3f3f3f3f3f3f3f
from pprint import pprint
from lib import refstr, Vec2, NSEW
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
p1=p2=0


def ex1(nums):
    if all(x ==0 for x in nums):
        return 0

    ax = []
    for n in range(1,len(nums)):
        ax.append(nums[n] - nums[n-1])
    f = ex1(ax)
    return nums[-1] + f



def ex2(nums):
    if all(x ==0 for x in nums):
        return 0

    ax = []
    for n in range(1,len(nums)):
        ax.append(nums[n] - nums[n-1])
    f = ex2(ax)
    xx = nums[0] - f
    # print(xx, ax)
    return xx



for l in L:
    x = ex1([int(x) for x in l.split()])
    p1 += x

for l in L:
    x = ex2([int(x) for x in l.split()])
    p2 += x

print(p1)
print(p2)







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
