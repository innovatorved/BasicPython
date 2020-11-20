import re

sentence = "we need to inform(related to tech) him about a new elex. technology(matlab)"



#search operation is use to check the one value from a long string
#--------------search in sentence

if re.search("tech" , sentence):
    print("Word is find!")


