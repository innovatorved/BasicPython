a = input('Enter any string: ')
'''
changing string to int 
ValueError
problem

'''

try:
    b = int(a)

except ValueError:
    b = None
    print(b)
