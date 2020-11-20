import re


sentence = "we need to inform(related to tech) him about a new elex. technology(matlab)"


#---------------findall (return a list of all find value)
store_value = re.findall("tech" , sentence)
print(store_value)
 
#---------------finditer (use to find the location of the word)
it = re.finditer("tech" , sentence)
print(it)

for i in it:
    print(i)
    loc = i.span() #span retuen the int value from index
    print(loc)



#searching multiple value with same relattion
values = "sat hat mat batnnn pat zat cat"

all_word = re.findall("[a-z][a-z]*" , values)  #we can check specific characteer by type it after the first column
print(all_word)

all_wor = re.findall("[shpz]at" , values)  #we can check specific characteer by type it after the first column
print(all_wor)
