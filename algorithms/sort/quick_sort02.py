from random import choice, randint

#s = [randint(0, 25) for i in range(10)]

s = [4, 3, 3, 2, 1, 1, 3, 3]

print(s)

def quick_soft(s):
    if len(s) < 2:
        return s
    q = choice(s)
    l, r, c = [], [], []

    for x in s:
        if x < q:
            l.append(x)
        elif x > q:
            r.append(x)
        else:
            c.append(x)
    return quick_soft(l) + c + quick_soft(r)

print(quick_soft(s))
