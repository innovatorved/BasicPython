#global and local variable

global_var = 20
class nextgen:
    '''
    self is only use in del or init function for better code
    cls use in all user define function under any class

    '''
    local_var = 11
    
    def innovate(self,):
        global v
        v = 2
        print(id(self.local_var))
        self.local_var += v
        print(self.local_var)
        print(id(self.local_var))
        return self.local_var
    
    def nextin(self,):
        print("hlo")
        #global_var = 2
        #return self.global_var



n = nextgen()

print(n.local_var)


n.local_var =  19
print(n.local_var)


