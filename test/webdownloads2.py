# from urllib.request import urlopen
# html = urlopen("file:///C:/Users/Sirozza/Desktop/2.html").read().decode('utf-8')


#елкипалки, без "re"
from collections import Counter ###счетчик
from urllib.request import urlopen
html = urlopen("file:///C:/Users/Sirozza/Desktop/2.html").read().decode('utf-8')
s = str(html)
data = []
spisok = s.split('<code>') ###делим по первому элементу
for x in spisok:
    data.append(x.split('</code>')[0]) ###добавляем в список, деля по второму элементу и беря  первый
c = Counter(data).most_common(3) ###считаем самые популярные 3
finalword = []
for i, f in c:
    finalword.append(i)
print(' '.join(finalword)) ###выводим список с разделителем пробелом






