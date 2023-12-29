import xlrd
import statistics

wb = xlrd.open_workbook(filename='salaries.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
city = [0, 0]
for n in range(1, 9):
    if statistics.median(sh.row_values(n)[1:]) > city[1]:
        city.insert(0, sh.row_values(n)[0])
        city.insert(1, statistics.median(sh.row_values(n)[1:]))
print(city[0])

profLen = len(sh.row_values(0)[1:])

prof = {}

for i in range(1, profLen):
    prof.pop(sh.row_values(0)[i])
    print(sh.row_values(0)[i])
print(prof)
# nmin = sh.row_values(6)[2]
# print(nmin)
# for rownum in range(7, 27):
#     temp = sh.row_values(rownum)
#     nmin = min(nmin, temp[2])
# print(nmin)