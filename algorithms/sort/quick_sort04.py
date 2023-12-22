
from random import choice, randint

#s = [randint(1, 3) for i in range(3)]

s = [3, 2, 1]

def qs(s):
    if len(s) < 2:
        return s
    else:
        c = choice(s)
        s.remove(c)
        l = [i for i in s if i <= c]
        r = [i for i in s if i > c]
    return qs(l) + [c] + qs(r)

if __name__ == '__main__':
    print(s)
    print(qs(s))

