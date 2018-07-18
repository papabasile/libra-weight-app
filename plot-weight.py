
#load libs
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import pandas as pd

#load csv file and skip first 3 rows
x=pd.read_csv('Libra_2017-12-15.csv',skiprows=3,delimiter=';')

#convert dates from string to number
datesx=[dates.datestr2num(i) for i in x['#date']]

plt.plot_date(datesx,x['weight'])
plt.xlabel('date')
plt.ylabel('lbs')
plt.show()
