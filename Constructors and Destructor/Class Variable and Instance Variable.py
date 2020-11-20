#Class Variable and Instance Variable


class NextIn:
    domain = "nextinnovation.tech"  #Class Variable or local Variable
    _do = "hlo Next"   #protective block
    def __init__(self):
        self.user_id = 171  #Instance Variable

#class variable should not be accesed using object, if we do that then it become an instance variable for that object

n = NextIn()

print(n.domain)
print(n._do)
print(id(n.domain))
n.user_id = 45
print(n.user_id)

print("\n")

n.domain = "Nextin.tech"
print(n.domain)
print(id(n.domain))

print("\n")

n2 = NextIn()
print(n2.domain)
print(n2._do)
print(id(n2.domain))        
print(n2.user_id)


print(n.__dict__)
print("\n")
print(n2.__dict__)
