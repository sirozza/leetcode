

def foo(x):
    s = []
    for i in range(x+1):
        if i%2 == 0:
            s.append(i)
    return s


if __name__ == '__main__':
    assert foo(3) == [0, 2]

