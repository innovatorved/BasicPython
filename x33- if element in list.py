fruits=('apple','bannana','pine apple','guava')
a=input('Enter the fruit name: ')
if a in fruits:
    print('fruit is already available-@',fruits.index(a))
    print(fruits.index(a))
else:
    print('fruit is not available')
