import xlrd
import statistics

wb = xlrd.open_workbook(filename='trekking1.xlsx')
sn = wb.sheet_by_name('Справочник')

prod = []

for i in range(1, len(sn.col_values(0)[1:])+1):
    prod.append({'name':sn.row_values(i)[0], 'calor':(sn.row_values(i)[1])})

print(prod)

d = {}

#d.get()


def get_data_for_sort(x):
    return x['calor'], x['name']


prod2 = sorted(prod, key=get_data_for_sort, reverse=True)

for i in prod2:
    print(i)

print(len(prod2))

for i in prod2:
    print(i.get('name').strip())

# def get_data_sort(x):
#
#
# sorted(prod, key=None, reverse=True)

# for i in range(1, len(sn.col_values(0)[1:])+1):
#     if statistics.median(sorted(sn.row_values(i)[1:])) > city[1]:
#         city.pop()
#         city.pop()
#         city.insert(0, sn.row_values(i)[0])
#         city.insert(1, statistics.median(sorted(sn.row_values(i)[1:])))
#
#
# for i in range(1, len(sn.row_values(0)[1:])+1):
#     if sum(sn.col_values(i)[1:])/len(sn.row_values(0)[1:]) > work[1]:
#         work.pop()
#         work.pop()
#         work.insert(0, sn.col_values(i)[0])
#         work.insert(1, sum(sn.col_values(i)[1:])/len(sn.row_values(0)[1:]))
#
# print(city[0], work[0])




