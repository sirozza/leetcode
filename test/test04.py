l = ['программа', 'привет', 'машина', 'продукт', 'город', 'прозрачный', 'дом']
t = l[0]
t.startswith('п')
print(t)
def f(s):
    f_words = [word for word in s if word.startswith('м')]
    return f_words

print(*f(l))