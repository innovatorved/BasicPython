#Multiple Constructors
class Calender:
    '''
    bs aise hi program seekhne ke liye bnaye the

    '''
    def __init__(self , day , month , year):
        self.d = day
        self.m = month
        self.y = year
        
    @classmethod
    def dayy(cls , dayy , time , name):
        cls.day = dayy
        cls.tim = time
        cls.na = "Mr."+name+" You aRe Now Next In Member"
        return cls(cls.day , cls.tim , cls.na)

    class Math:
        def __init__(self):
            #print("this class for math")
            self.a = 0
            self.b = 0
            
        @classmethod
        def sum(cls,a):
            '''
            cls.c=a+b
            return cls.c
            
            '''
            #print(a)
            cls.b = 0
            #a = [1,2,3,4,5]
            for x in a:
                #print(x)
                cls.b+=x
                #print(b)
            return cls.b

        @classmethod
        def sub(cls,a):
            '''
            cls.c=a-b
            return cls.c
            
            '''
            #print(a)
            cls.b = 0
            #a = [1,2,3,4,5]
            for x in a:
                #print(x)
                cls.b-=x
                #print(b)
            return cls.b

        @classmethod
        def mul(cls,a):
            '''
            cls.c=a*b
            return cls.c
            
            '''
            #print(a)
            cls.b = 1
            #a = [1,2,3,4,5]
            for x in a:
                #print(x)
                cls.b*=x
                #print(b)
            return cls.b


        @classmethod
        def div(cls):
            '''
            cls.c=a/b
            return cls.c
            
            '''
            #print(a)
            cls.a = float(input('Enter the No. you Want to divide : '))
            cls.b = float(input('Enter the divider : '))
            #a = [1,2,3,4,5]
            cls.c = a/b
            return cls.c

      
        
a = Calender(4,2,2002)
#print(a.y)

b = Calender.dayy("zx","xc","Ved")

