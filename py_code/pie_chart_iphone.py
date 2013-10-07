# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

labels = ['Positive', 'Negative', 'Others']
fracs = [None]*5
pos = (1048, 707, 688, 633, 615)
neg = (554, 571, 554, 552, 422)
all_count = (3091, 3027, 2758, 2492, 2225)
for i in range(5):
    fracs[i] = [pos[i], neg[i], all_count[i]-pos[i]-neg[i]]

explode = (0.05, 0, 0)

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'burlywood']
plt.title('')
#the_grid = GridSpec(3, 2)
#plt.subplot(the_grid[0, 0], aspect = 1)
plt.subplot2grid((3, 2),(0,0),aspect = 1)
plt.pie(fracs[0], explode, labels = labels, colors = colors,
        autopct = '%1.1f%%', shadow = True)
plt.title('iPhone 3GS', bbox = {'facecolor':'white', 'alpha':0.5, 'pad':5})

#plt.subplot(the_grid[0, 1], aspect = 1)
plt.subplot2grid((3, 2),(1,0), aspect = 1)
plt.pie(fracs[1], explode, labels = labels, colors = colors,
        autopct = '%1.1f%%', shadow = True)
plt.title('iPhone 4', bbox = {'facecolor':'white', 'alpha':0.5, 'pad':5})

#plt.subplot(the_grid[1, 0], aspect = 1)
plt.subplot2grid((3, 2),(0,1), aspect = 1)
plt.pie(fracs[2], explode, labels = labels, colors = colors,
        autopct = '%1.1f%%', shadow = True)
plt.title('iPhone 4S', bbox = {'facecolor':'white', 'alpha':0.5, 'pad':5})

#plt.subplot(the_grid[1, 1], aspect = 1)
plt.subplot2grid((3, 2),(1,1), aspect = 1)
plt.pie(fracs[3], explode, labels = labels, colors = colors,
        autopct = '%1.1f%%', shadow = True)
plt.title('iPhone 5', bbox = {'facecolor':'white', 'alpha':0.5, 'pad':5})

#plt.subplot(the_grid[2,0], aspect = 1)
plt.subplot2grid((3, 2),(2,0), colspan = 2, aspect = 1)
plt.pie(fracs[4], explode, labels = labels, colors = colors,
        autopct = '%1.1f%%', shadow = True)
plt.title('iPhone 5S', bbox = {'facecolor':'white', 'alpha':0.5, 'pad':5})

plt.show()

# <codecell>


