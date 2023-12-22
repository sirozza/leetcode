from random import randint


def quicksort(a, fst, lst):
    if fst >= lst:
        return
    i, j = fst, lst
    pivot = a[randint(fst, lst)]
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i, j = i + 1, j -1
    quicksort(a, fst, j)
    quicksort(a, i, lst)

a = [3, 2, 1]

quicksort(a, 0, len(a)-1)

print(a)