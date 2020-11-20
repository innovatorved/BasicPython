#scatter plot
import matplotlib.pyplot as plt

x=[1,4,5,8,9,10,11,15,13]
y=[5,2,6,8,9,5,9,8,2]

plt.scatter(x,y,label='Scatters',color='r')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')

plt.legend()
plt.show()
