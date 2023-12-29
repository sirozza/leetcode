import xlrd
wb = xlrd.open_workbook(filename='salaries.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
name = sh.row_values(1)
for n in range(1, 8):
    print(sh.row_values(n)[1:])
# nmin = sh.row_values(6)[2]
# print(nmin)
# for rownum in range(7, 27):
#     temp = sh.row_values(rownum)
#     nmin = min(nmin, temp[2])
# print(nmin)