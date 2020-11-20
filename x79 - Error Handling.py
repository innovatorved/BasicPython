def divide_num(a,b):
    '''if we divide any number by 0 then they show error
        by try and except we print that this is not possible if
        we try to divide num by 0'''
    try:
        c=a/b
    except ZeroDivisionError:
        print('\nAny num is not divide by 0')
        c = None
    print(c)
    return c

divide_num(float(input('Enter the Num: ')),float(input('Enter the Divider: ')))

