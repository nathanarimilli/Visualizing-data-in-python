import json
import matplotlib.pyplot as plt
import os

indiagdp = []
with open('indiagdp.json') as f:
        india = f.read()
        indiagdp += json.loads(india)
xs = []
indgdpy = []
for line in indiagdp:
        xs.append(line['date'])
        indgdpy.append(line['value'])
xs.reverse()
indgdpy.reverse()


import numpy
fig, ax = plt.subplots()
ax.bar(xs, indgdpy, label = 'India')
plt.title('India GDP in US Dollars')    
plt.xlabel('year') 
plt.xticks(rotation=25) 
plt.xticks(numpy.arange(0, len(xs)+1, 5)) 
plt.ylabel('GDP (USD)') 
plt.legend()
plt.show()


