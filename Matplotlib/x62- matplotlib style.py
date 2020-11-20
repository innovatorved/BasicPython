from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x=[2010,2011,2012,2013,2014,2015]
y=[55,33,56,60,85,99]

y2=[54,60,85,33,56,77]

plt.plot(x,y,'b',label='Ved Gupta', linewidth=1)
plt.plot(x,y2,'g',label='Abhishek Yadav', linewidth=1)

plt.title("Information Data")

plt.xlabel("Year")
plt.ylabel("Percentage")

plt.legend()
plt.grid(True,color='k')
plt.show()
