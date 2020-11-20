import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#seaborn direct load data from github
d = sns.load_dataset('flights')
sns.relplot(x = 'passengers' , y = 'month' , data = d)
