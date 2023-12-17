import sys
import math
from collections import defaultdict
from math import gcd, lcm
oo = 9999999999999

lines = open(sys.argv[1]).read().strip().split('\n')
p1=p2=0

ICOS = (1,0,-1,0)
ISIN = (0,1,0,-1)

M = defaultdict(list)

def main():
    seeds = [int(x) for x in lines[0].split()[1:]]
    
    chunks = '\n'.join(lines[2:]).split('\n\n')

    for chunk in chunks:
        cl = chunk.split('\n')
        l, cl = cl[0], cl[1:]
        l = l.split()[0].split('-')
        # print(l)
        src, _, dst = l
        for l in cl:
            ds, ss, sz = [int(x) for x in l.split()]
            M[(src, dst)].append((ss, ds, sz))

    for v in M.values():
        v.sort()

    p1 = oo
    for s in seeds:
        typ = 'seed'
        while typ != 'location':

            mm = None
            for k, v in M.items():
                if k[0] == typ:
                    mm = (k,v)
                    break
            else:
                raise Exception('wat')

            for ss, ds, sz in mm[1]:
                if ss <= s and s <= ss+sz:
                    nv = ds + (s-ss)
                    break
            else:
                nv = s
            typ = mm[0][1]
            s = nv
        if s < p1:
            p1 = s
    
                
    print(p1)

    p2 = oo
    for i in range(len(seeds)//2):
        ss, many = seeds[i*2], seeds[i*2+1]

        def R(typ, b, e, d=0):
            # print(' '*d, typ, b, e)
            if e <= b:
                return
            nonlocal p2
            if typ == 'location':
                if b < p2:
                    p2 = b
                return

            mm = None
            for k, v in M.items():
                if k[0] == typ:
                    mm = (k, v)
                    break
            else:
                raise Exception('wat')
            nt = mm[0][1]

            mi = 0
            while b<e:

                if mi < len(mm[1]):
                    ss,ds,sz = mm[1][mi]
                    sb, se = ss, ss + sz  # xxx

                    if se <= b:
                        mi += 1
                        continue

                    if b < sb:
                        R(nt, b, min(sb,e), d+1)
                        b = min(sb,e)
                        continue

                    if sb <= b:
                        R(nt, b-ss+ds, min(se,e)-ss+ds, d+1)
                        b = min(se,e)
                        mi += 1
                        continue

                else:
                    R(nt,b,e,d+1)
                    b = e

        # print('seed', ss, ss+many)
        R('seed', ss, ss+many)

    print(p2)


if __name__ == '__main__':
    main()
