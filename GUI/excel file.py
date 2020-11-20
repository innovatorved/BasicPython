import xlwt

wb = xlwt.Workbook()

database = wb.add_sheet('Student data')

database.write(0,0,'value1')

wb.save('project.xlsx')
