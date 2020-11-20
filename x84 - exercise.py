file_google = open('google.txt' , 'r')
out_lines = file_google.readlines()
print(out_lines)
file_google.close()
new_list = []
print('\n\n')

for element in out_lines:
    element = element.lower()
    element = element.replace('\n' , ' ')
    element = element.replace(',' , ' ')
    element = element.replace('(' , ' ')
    element = element.replace(')' , ' ')
    element = element.replace('[' , ' ')
    element = element.replace(']' , ' ')
    new_list.append(element)

print(new_list)
i=0
for x in new_list:
    print(i,') ',x)
    i+=1
x = len(new_list)
#print(x)

#list to string by function
txt = ''.join(new_list)
#print(txt)

words = txt.split()
print('Length of all World is: ',len(words))

word_fre = {}
for word in words:
    if word in word_fre:
        word_fre[word] +=1

    else:
        word_fre[word] = 1

#print(word_fre)
        
#print(sorted(word_fre))     #sorted key word sort value in assending order
#print(sorted(word_fre.items()))     #sorted key word sort value in assending order bt there element

# sorted(word_fre.items() , key = lambda item : item[1]
#print(sorted(word_fre.items(), key=lambda item : item[0]))

sorted_list =sorted(word_fre.items(), key=lambda item : item[1])
print('\n\n',sorted_list)

print('\n\n',sorted_list[-10:])

with open('nxt_file.txt' , 'w') as out:
    for element in sorted_list[-10:]:
        out.write(element[0] + '\n')

print('Successfully Added')
