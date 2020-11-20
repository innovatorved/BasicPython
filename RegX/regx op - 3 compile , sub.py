import re

str_2 = "today is sunny day we can except a match between india and aus"

#re.compile --------(used for what you change in string)
regX = re.compile(" ")

#sub() ----------------(used for saying what is new world)
#-------- str = re.compile("what your change")sub("what new come" , str_name)

str_3 = regX.sub("\n" , str_2)
print(str_3)
