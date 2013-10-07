# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

labels = ['Positive', 'Negative', 'Others']
fracs = [None]*2
pos = (565, 619)
neg = (478, 352)
all_count = (2207, 2234)
for i in range(2):
    fracs[i] = [pos[i], neg[i], all_count[i]-pos[i]-neg[i]]

explode = (0.05, 0, 0)

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'burlywood']
plt.title('')
the_grid = GridSpec(1, 2)
plt.subplot(the_grid[0, 0], aspect = 1)
plt.pie(fracs[0], explode, labels = labels, colors = colors,
        autopct = '%1.1f%%', shadow = True)
plt.title('iPhone 5S', bbox = {'facecolor':'white', 'alpha':0.5, 'pad':5})

plt.subplot(the_grid[0, 1], aspect = 1)
plt.pie(fracs[1], explode, labels = labels, colors = colors,
        autopct = '%1.1f%%', shadow = True)
plt.title('iPhone 5C', bbox = {'facecolor':'white', 'alpha':0.5, 'pad':5})

plt.show()

# <codecell>


