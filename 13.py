import sys
D = open(sys.argv[1],'r').read().strip()
L = D.split('\n')

p1=p2=0

B = D.split('\n\n')


def transpose(m):
    out = []
    for x in range(len(m[0])):
        tmp = ''
        for y in m:
            tmp += y[x]
        out.append(tmp)
    return out


def delta(a,b):
    return sum(a[n]!=b[n] for n in range(len(a)))


for n,b in enumerate(B):
    b = b.split('\n')
    w, h = len(b[0]), len(b)

    y_hit = None
    for yy in range(h-1):
        y_hit = yy
        j, k = yy, yy+1
        while 0 <= j and k < h:
            if b[j] != b[k]:
                y_hit = None
                break
            j -= 1
            k += 1
        if y_hit is not None: break


    b = transpose(b)
    w, h = len(b[0]), len(b)

    x_hit = None
    for yy in range(h-1):
        x_hit = yy
        j, k = yy, yy+1
        while 0 <= j and k < h:
            if b[j] != b[k]:
                x_hit = None
                break
            j -= 1
            k += 1
        if x_hit is not None: break

    p1 += x_hit+1 if x_hit is not None else (y_hit+1)*100


    b = transpose(b)
    w, h = len(b[0]), len(b)
    y_hit = None
    for yy in range(h-1):
        y_hit = yy
        j, k = yy, yy+1
        err = 0
        while 0 <= j and k < h and err < 2:
            tmp = delta(b[j], b[k])
            err += tmp
            j -= 1
            k += 1
        if err == 1:
            break
        else:
            y_hit = None
    b = transpose(b)
    w, h = len(b[0]), len(b)
    x_hit = None
    for yy in range(h-1):
        x_hit = yy
        j, k = yy, yy+1
        err = 0
        while 0 <= j and k < h and err < 2:
            tmp = delta(b[j], b[k])
            err += tmp
            j -= 1
            k += 1
        if err == 1:
            break
        else:
            x_hit = None

    p2 += x_hit+1 if x_hit is not None else (y_hit+1)*100
print(p1)
print(p2)


