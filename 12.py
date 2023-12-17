import sys
D = open(sys.argv[1],'r').read().strip()
# D = "??.???.?.?.??.???. 2,2,1,1,2,1"
L = D.split('\n')

for rep in (1,5):
    many = 0
    for l in L:

        P, S = l.split()
        P = '?'.join([P]*rep)
        S = ','.join([S]*rep)
        S = [int(x) for x in S.split(',')]
        P += '$$'
        minspan = sum(S)+len(S)
        # print(minspan)

        M = {}
        def BT(j, k, d=0):
            if (j,k) in M: return M[(j,k)]

            if P[j] == '$':
                good = int(k == len(S))
                # print('. '*d, 'end of pattern and', 'OK' if good else 'BAD')
                return good

            #if j and P[j-1] == '#':
            #    return 0

            """
            if k == len(S):
                n = int(all(ch=='?' or ch=='.' for ch in P[j:]))
                memo[(j,k)] = n
                return n
            """

            if k == len(S):
                good = all(ch in '?.$' for ch in P[j:])
                # print('. '*d, 'segments done and rest', 'OK' if good else 'BAD')
                return int(good)

            jj = j
            many = 0
            chunk = S[k]
            while P[j] != '$':
                sz = len(P) - j - 2
                if sz < sum(S[k:])+len(S[k:])-1:
                    break
                m = all((P[j+n] in '#?') for n in range(chunk))
                sep = P[j+chunk] in '?.$'
                # print('. '*d, j,k,P[j],S[k],sz, 'FIT' if m else 'NOPE', sep)
                if m and sep:
                    many += BT(j+chunk+1, k+1, d+1)
                if P[j] == '#':
                    break
                j+=1

            M[(jj,k)] = many
            return many

        q = BT(0,0)
        # print(l, q)
        many += q
    print(many)
