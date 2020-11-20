#decorators
def fun_1(fun):  #Decorator Definition
    def inner_fun1():
        #this is the Wrapper function . Heres the Argument is Called
        print("Welcome")
        fun()
        #the argument function has been called inside the wrapper function
        print("Execute process is Done!")
        
    return inner_fun1
        
        
def fun_3():     #The function is called inside the wrapper
    print("Hlww Mr. VED GUPTA")



#passing argument function inside the decorator to control its behavior
function_out = fun_1(fun_3)
#Calling the Function

function_out()
