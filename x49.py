d={'child 1':{'name':'ved','year':2002},'child 2':{'name':'ansh','year':2000},'child 3':{'name':'sandeep','year':2012}}
for x in d:
    print(x)
    for a in d[x]:
        print(a)
        print(d[x][a])

    print('\n')

