import xlrd
import statistics

wb = xlrd.open_workbook(filename='salaries.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])

profLen = len(sh.row_values(0))



city = [0, 0]
for n in range(1, profLen):
    if statistics.median(sorted(sh.row_values(n)[1:])) > city[1]:
        city.pop()
        city.pop()
        city.insert(0, sh.row_values(n)[0])
        city.insert(1, statistics.median(sorted(sh.row_values(n)[1:])))
    print(city)

profLen = len(sh.row_values(0))
#print(profLen)
cityLine = len(sh.col_values(0))
#print(sh.row_values(1)[1:])
city_list = sh.col_values(0)[1:]


prof_list = sh.row_values(0)[1:]

max_pay_prof_city = []

for i in range(1, profLen):
    print(int(sum(sh.row_values(i)[1:])/len(sh.row_values(i)[1:])))
    max_pay_prof_city.append(int(sum(sh.row_values(i)[1:])/len(sh.row_values(i)[1:])))
    print(max_pay_prof_city)

print(max_pay_prof_city)
print(max_pay_prof_city.index(max(max_pay_prof_city)))

#print(max(max_pay_prof_city))
#print(prof_list[max_pay_prof_city.index(max(max_pay_prof_city))])
# for i in range(1, profLen):
#     print(sh.row_values(i)[1:])
#     max_pay_prof_city.append(prof_list[(sh.row_values(i)[1:].index(max(sh.row_values(i)[1:])))])
#     print(sh.row_values(i)[1:].index(max(sh.row_values(i)[1:])))
#
# print(max_pay_prof_city)
