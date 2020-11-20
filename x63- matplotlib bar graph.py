from matplotlib import pyplot as plt

x=[1,3,5,7,9,11]
y=[55,33,56,60,85,99]
x2=[2,4,6,8,10,12]
y2=[54,60,85,33,56,77]

plt.bar(x,y,label='fri',color='k')
plt.bar(x2,y2,label='Abhi',color='r')

plt.title("Information Data")

plt.xlabel("num")
plt.ylabel("Per")

plt.legend()
plt.show()
