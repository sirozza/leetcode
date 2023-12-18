from random import choice, randint

s = [5, 5, 4, 3, 2, 1]

print(f'Список без сортировки: {s}')


def quick_sort(s):
    if len(s) < 2:
        return s
    e = choice(s)
    print(f'e: {e}')
    l, c, r = [], [], []

    for i in s:
        print(s)
        print(len(s))
        if i < e:
            l.append(i)
        elif i > e:
            r.append(i)
        else:
            c.append(i)
    print(f'l: {l}, c: {c}, r: {r}')
    return quick_sort(l) + c + quick_sort(r)

print(f'Отсортированный список: {quick_sort(s)}')