import gspread
from oauth2client.service_account import ServiceAccountCredentials

url = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\VED GUPTA\\Desktop\\PYTHON files\\data manager\\stu.json', url)

client = gspread.authorize(creds)

sheet = client.open('data_student').sheet1

data = sheet.get_all_records()

print(data)

print(sheet.row_count)

z = ['Ansh Gupta' , '18' , '7317479266' , 'anshgmay@gmail.com']
b=3
a=0
for x in z:
    a = a+1
    sheet.update_cell(b,a, x)


data = sheet.get_all_records()
print(data)
print(len(data))
    
    

