#Public , Protected and Private Metheods
class nextin:

    def __init__(self):
        self.__nextid = 4123
        self._nextus = "innovator_ved"
        self.nextna = "Ved Prakash Gupta"
        self._nextsa = 250000

    def __so(self):
        print("this is a private block")
        self.a = 1
        self.b = 2
        return self.a

    def yo(self):
        print("this is a public block")
        self.a = 1
        self.b = 2

    def _no(self):
        print("this is a prottective block block")
        self.a = 1
        self.b = 2

a = nextin()
print(a._nextin__nextid)

b = a._nextin__so()
print(b)

c = a.yo()
print(c)

d = a._no()
print(d)
