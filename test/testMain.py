

def func(*args):
    return print('Hello', *args, '!')


name = ['Gvido', 1]


if __name__ == '__main__':
    func(*name)
