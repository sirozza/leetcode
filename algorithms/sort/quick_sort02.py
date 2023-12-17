from random import choice


s = [3, 0, 7, 1, 5, 2]

print(s)

def quick_soft(s):
    if len(s)<2:
        return s
    q = choice(s)
    l, m, r = [], [], []

    for x in s:
        if x <= q:
            l.append(x)
        elif x > q:
            r.append(x)
        else:
            m.append(x)
    return quick_soft(l) + m + quick_soft(r)

print(quick_soft(s))
