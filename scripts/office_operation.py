# excel
#sample1
import openpyxl as px

wb = px.Workbook()
wb.save('excel_sample.xlsx')

#sample2
import openpyxl as px

wb = px.load.Workbook('excel_sample.xlsx')
ws = wb.active
ws['A1'] = 'Hello'
ws.title = 'sample_title1'
wb.save('excel_sample.xlsx')