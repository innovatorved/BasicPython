import matplotlib.pyplot as plt

slices = [8,9,1,5,4]
label = ['first' , 'Second' , 'Third' , 'Fourth' ,'Fifth']
colors = ['c','m','r','b','k']

plt.pie(slices , labels = label , colors = colors , startangle=60 , shadow = True ,explode=(0,0,0,0.1,0) , autopct='%1.1f%%')

plt.title('Pie Chart')
plt.show()
