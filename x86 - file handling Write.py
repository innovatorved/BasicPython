file = open('alpha.txt' , 'r')
print('sucessfully Read')

print(file,'\n')

output = file.readlines()
print(output)

i = 1
for line in output:
    #use strip() function to remove extra line '\n'
    print(i,') ',line.strip())
    i +=1

f_out = open('re_alpha.txt' , 'w')
f_out.writelines(output[0:2])
f_out.close()
print('Succesfully Write')

f = open('re_alpha.txt' , 'w+')
out = f.read()
print(out)
f.close()
