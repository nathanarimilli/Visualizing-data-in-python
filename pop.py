import json
import matplotlib.pyplot as plt
import os

chinapop = []
with open('chinapop.json') as f:
        chinap = f.read()
        chinapop += json.loads(chinap)
x = []
chipopy = []
for line in chinapop:
        x.append(line['date'])
        chipopy.append(line['value'])
x.reverse()
chipopy.reverse()

indiapop = []
with open('indiapop.json') as f:
        indiap = f.read()
        indiapop += json.loads(indiap)

indpopy = []
for line in indiapop:
        indpopy.append(line['value'])
indpopy.reverse()

import numpy
plt.plot(x,chipopy, label ='China')
plt.plot(x,indpopy, label ='India')
plt.title('China vs India Population')    #to add a title
plt.xlabel('Year') #x axis label
plt.xticks(rotation=25) #to rotate the bar labxwels
plt.xticks(numpy.arange(0, len(x)+1, 5)) #to change the frequency of the bar labels
plt.ylabel('Population') #y axis label
plt.legend() #this is to add a legend (labels are assigned when data was plotted)
plt.show()

