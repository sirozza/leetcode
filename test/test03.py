a = '''name,price,qantity
spam,8,92
'''

d = {}

for line in a.splitlines():
    print(line)
    name, price, _ = line.split(',')
    d[name] = price

print(d)