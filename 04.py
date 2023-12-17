import sys
lines = open(sys.argv[1]).read().strip().split('\n')
p1=p2=0

copies = [1] * len(lines)
for n, line in enumerate(lines):
    a, rest = line[4:].split(': ')
    a = int(a)
    left, right = rest.split('|')

    w = set(int(x) for x in left.split())
    h = set(int(x) for x in right.split())
    hit = sum(1 for x in h if x in w)
    if hit:
        p1 += 2**(hit-1)
    for j in range(hit):
        copies[n+j+1] += copies[n]

    p2 += copies[n]

print(p1)
print(p2)
