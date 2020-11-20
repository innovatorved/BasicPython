file = open('alpha.txt' , 'r')
print('sucessfully Read')

print(file,'\n')

output = file.read()
print(output)

list_of_file = output.split()
print('\n',list_of_file)
file.close()

f = open('alpha.txt' , 'r')

#fun for read line by line
out_line = f.readline()
print('\n',out_line)
f.close()

#function change each line in to element of list
fl = open('alpha.txt' , 'r')
line_to_list = fl.readlines()
print('\n',line_to_list)
fl.close()

#in this metheod if we existing with this pack file were automatic close
with open('alpha.txt' , 'r') as fil:
    out = fil.read()
    print(out)

print('file automatic closed')
    
