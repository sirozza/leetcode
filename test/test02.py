
def temp_dec(func):
    def wrapper(*args, **kwargs):
        print('Начало wrapper')
        func()
        print('Конец wrapper')
    return wrapper


@temp_dec
def temp1():
    print('Hello')


if __name__ == '__main__':
    temp1()