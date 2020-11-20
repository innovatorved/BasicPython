#ex-2 decorators


def fun_1(fun):
    def fun_2(a,k):
        print("Weilcome 1")
        f = fun(a,k)
        print("Weilcome 2")
        #print(f)
        return f
    return fun_2

@fun_1
def fun_3(a,b):
    print("Weilcome 3")
    return a*b



print(fun_3(10,20))
