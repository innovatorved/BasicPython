from matplotlib import pyplot as plt

age_group = [102,110,125,202,252,290,350,380,420,570,590,620,630,670,690,730,750,800,890]
gave=[100,200,300,400,500,600,700,800,900]

plt.hist(age_group,gave, histtype='bar', rwidth=0.5,color='b')

plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.title('Histograph')

plt.legend()
plt.show()
