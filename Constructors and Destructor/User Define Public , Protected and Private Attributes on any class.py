#User Define Public , Protected and Private Attributes
'''
User Define Public , Protected and Private Attributes
__pri
_pro
pub


__pri - attribute are not easily fetched if u read them
metheod is classname()._classname__pri
'''

class nextin:
    def __init__(self):
        self.__pri = ("This Section is fully Private")
        self._pro  = ("This Section is Protective")
        self.pub   = ("This Section is Public")

n = nextin()
print(n.pub)
print(n._pro)
try:
    print(n.__pri)

except AttributeError:
    print("Attribute Error Formed")


print(n._nextin__pri)
