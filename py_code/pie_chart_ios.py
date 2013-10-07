# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

labels = ['Positive', 'Negative', 'Others']
fracs_ios4 = [745, 530, 2552 - 745 - 530]
fracs_ios5 = [787, 451, 2491 - 787 - 451]
fracs_ios6 = [843, 492, 2611 - 843 - 492]
fracs_ios7 = [729, 595, 2374 - 729 - 595]

explode = (0.05, 0, 0)

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'burlywood']
plt.title('')
the_grid = GridSpec(2, 2)
plt.subplot(the_grid[0, 0], aspect = 1)
plt.pie(fracs_ios4, explode, labels = labels, colors = colors,
        autopct = '%1.1f%%', shadow = True)
plt.title('iOS 4', bbox = {'facecolor':'white', 'alpha':0.5, 'pad':5})

plt.subplot(the_grid[0, 1], aspect = 1)
plt.pie(fracs_ios5, explode, labels = labels, colors = colors,
        autopct = '%1.1f%%', shadow = True)
plt.title('iOS 5', bbox = {'facecolor':'white', 'alpha':0.5, 'pad':5})

plt.subplot(the_grid[1, 0], aspect = 1)
plt.pie(fracs_ios6, explode, labels = labels, colors = colors,
        autopct = '%1.1f%%', shadow = True)
plt.title('iOS 6', bbox = {'facecolor':'white', 'alpha':0.5, 'pad':5})

plt.subplot(the_grid[1, 1], aspect = 1)
plt.pie(fracs_ios7, explode, labels = labels, colors = colors,
        autopct = '%1.1f%%', shadow = True)
plt.title('iOS 7', bbox = {'facecolor':'white', 'alpha':0.5, 'pad':5})

plt.show()

# <codecell>


