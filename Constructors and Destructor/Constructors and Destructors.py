'''
#Constructor
   --the constructor is implemented using __init__(self) where you can define parameters that follows the self

#Destructors
   --The destructors is define using __def__(self).
         In the Example, the obj is created and manually deleted. Therefore, both messages will be displayed

'''

class testClass:
    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("destructor")


class math:
    def __init__(self):
        global a , b , c
        a = int(input("Enter a number: "))
        b = (input("Enter a String: "))

    global add
    add = (lambda x , y : x+y)
    
    def __del__(self):
        print(a)
        return self , "abc"

    
if __name__ == "__main__":
    obj = testClass()
    del obj
    
if __name__ == "__main__":
    b = math()
    #del b
