import os
from time import sleep 

Dir_location = os.getcwd()   #find current directory location

print(Dir_location)

os.mkdir('New folder_OS')  #make new folder on same location

#sleep(2)

os.rename('New folder_OS' , 'OS folder name_changed')  #change name of folder

#sleep(2)

os.rmdir('OS folder name_changed')  #remove or delete directory

#sleep(2)

os.chdir('C:\\Users\\VED GUPTA\\Desktop\\PYTHON files\\data manager')   # use for change directory

print(os.getcwd())

list = os.listdir()   #list of directories
print(list)

file = open('OS.txt' , 'a')  #open the file
file.write('hello i m \n')
file.write('hell \n')
print('\n')

file.close()   #closing the file

file = open('OS.txt')
print(file.read())    #and read it
file.close()

