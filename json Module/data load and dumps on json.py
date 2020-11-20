#json: JavaScript Object Notation
import json

#make a dictionary
data = {"name":"Ved Gupta" , "Gen":"Male"}
print(type(data))

json_str = json.dumps(data)
#dumps( ) - the original data gets transformed into json format and type will be string
print(json_str)
print(type(json_str))


orig = json.loads(json_str)
#loads() - the json format data gets decoded and the receiver gets the data in the original form and type will be again dictionary
print(orig)
print(type(orig))
