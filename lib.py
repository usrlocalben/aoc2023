ICOS = (1,0,-1,0)
ISIN = (0,1,0,-1)
import math

class refstr:
    def __init__(self, a):
        self.a = a
    def c_pre(self, p):
        if self.a.startswith(p):
            self.a = self.a[len(p):]
            return True
        return False
    def c_sp(s):
        while len(s.a) and s.a[0] == ' ':
            s.a = s.a[1:]
    def c_num(s):
        s.c_sp()
        ax = 0
        while len(s.a) and s.a[0].isdigit():
            ax = ax*10 + int(s.a[0])
            s.a = s.a[1:]
        return ax
    def c_tok(s):
        s.c_sp()
        ax = ''
        while len(s.a) and s.a[0] != ' ':
            ax += s.a[0]
            s.a = s.a[1:]
        return ax



class IVec2:
    def __init__(self, x=None,y=None):
        if x is None and y is None:
            self.x, self.y = 0, 0
        elif x is None:
            raise TypeError('cant set y w/o x')
        elif y is None:
            self.x, self.y = x, x
        else:
            self.x, self.y = x, y
    def t(self):
        return (self.x,self.y)
    def __eq__(self, other):
        return self.x==other.x and self.y ==other.y
    def __hash__(self):
        return (self.x,self.y).__hash__()
    def __add__(self, other):
        if isinstance(other, int):
            return IVec2(self.x+other, self.y+other)
        elif isinstance(other, IVec2):
            return IVec2(self.x+other.x, self.y+other.y)
        else:
            raise TypeError('IVec2 type error')
    def __sub__(self, other):
        if isinstance(other, int):
            return IVec2(self.x-other, self.y-other)
        elif isinstance(other, IVec2):
            return IVec2(self.x-other.x, self.y-other.y)
        else:
            raise TypeError('IVec2 type error')
    def __mul__(self, other):
        if isinstance(other, int):
            return IVec2(self.x*other, self.y*other)
        elif isinstance(other, IVec2):
            return IVec2(self.x*other.x, self.y*other.y)
        else:
            raise TypeError('IVec2 type error')
    def __div__(self, other):
        if isinstance(other, int):
            return IVec2(self.x//other, self.y//other)
        elif isinstance(other, IVec2):
            return IVec2(self.x//other.x, self.y//other.y)
        else:
            raise TypeError('IVec2 type error')
    def __neg__(self):
        return IVec2(-self.x, -self.y)
    def __mod__(self, other):
        if isinstance(other, int):
            return IVec2(self.x%other, self.y%other)
        elif isinstance(other, IVec2):
            return IVec2(self.x%other.x, self.y%other.y)
        else:
            raise TypeError('IVec2 type error')
    def abs(self):
        return IVec2(math.abs(self.x), math.abs(self.y))
    def rot(self, th):
        if th == 'L':
            th = 1
        elif th == 'R':
            th = -1
        th %= 4
        c, s = ICOS[th], ISIN[th]
        x, y = self.x, self.y
        return IVec2((c*x)-(s*y), (s*x)+(c*y))
    def __str__(self):
        return f"({self.x},{self.y})"

NSEW = {'N': IVec2(0,-1), 'S': IVec2(0,1), 'E': IVec2(1,0), 'W': IVec2(-1,0)}
