import xlwt
import xlrd

xls = xlwt.Workbook()
sheet = xls.add_sheet('sample')
sheet1 = xls.add_sheet('demo')
sheet.write(0, 0, 'netcon')
sheet.write(0, 1, 'conw.net')
for i in range(0, 100):
    for j in range(0, 10):
        sheet1.write(i, j,  i*j)
xls.save('sample.xls')
print("创建excel文件成功！")

xls = xlrd.open_workbook('sample.xls')
sheets = xls.sheets()
for sheet in sheets:
    rows = sheet.nrows
    for i in range(0, rows):
        print(sheet.row_values(i))


