import sys
D = open(sys.argv[1]).read().strip()
L = D.split('\n')

amt = {'red': 12, 'green': 13, 'blue': 14}

bad = set()
games = set()

p2 = 0
for line in L:
    line = line[5:]
    n, rest = line.split(':', 1)
    n = int(n)
    games.add(n)

    chunks = [it.strip() for it in rest.split(';')]
    mx = {k: 0 for k in ('red', 'blue', 'green')}
    for chunk in chunks:
        for seg in [it.strip() for it in chunk.split(',')]:
            a, b = seg.split()
            a = int(a)
            mx[b] = max(mx[b], a)
            if a > amt[b]:
                bad.add(n)
    p2 += mx['red']*mx['blue']*mx['green']


print(sum(n for n in games if n not in bad))
print(p2)
