
def decor(func):
    def wrapper():
        func()
        print(f'Внутри Декоратора')
    return wrapper


@decor
def foo():
    return print('Это работает func()')


def foo2(a=None):
    print(a)


if __name__ == '__main__':
    foo()
    foo2(a=[1, 2, 3])
    foo2(['a', 'b'])
