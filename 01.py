import sys
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
p1=p2=0
words = ['zero', 'one','two','three','four','five','six','seven','eight','nine']
digits = '0123456789'

for line in L:
    nums = [ch for ch in line if ch in digits]
    a, b = nums[0], nums[-1]
    p1 += int(a+b)

    for i in range(len(line)):
        a = None
        if line[i] in '0123456789':
            a = line[i]
            break
        for n,w in enumerate(words):
            if line[i:i+len(w)] == w:
                a = str(n)
                break
        if a is not None:
            break
    else:
        raise Exception('wat')

    for i in range(len(line),0,-1):
        b = None
        if line[i-1] in '0123456789':
            b = line[i-1]
            break
        for n,w in enumerate(words):
            if line[i-len(w):i] == w:
                b = str(n)
                break
        if b is not None:
            break
    else:
        raise Exception('wat')

    p2 += int(a+b)

print(p1)
print(p2)
