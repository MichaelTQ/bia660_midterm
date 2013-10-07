# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

colors = ['seagreen','yellowgreen', 'gold', 'lightskyblue', 'royalblue', 'lightcoral', 'burlywood']

N = 4
pos = (745, 787, 843, 729)
neg = (530, 451, 492, 595)
all_count = (2552, 2492, 2611, 2374)

ind = np.arange(N)
width = 0.25

fig, ax = plt.subplots()
rects1 = ax.bar(ind, pos, width, color = colors[0])
rects2 = ax.bar(ind, neg, width, color = colors[2], bottom = pos)
rects3 = ax.bar(ind + width, all_count, width, color = colors[4])

#add some attributes
ax.set_ylabel('Tweet Numbers')
#ax.set_title('')
ax.set_xticks(ind + width)
ax.set_xticklabels(('iOS4', 'iOS5', 'iOS6', 'iOS7'))
leg = ax.legend((rects1[0], rects2[0], rects3[0]), ('Positive','Negative','All'),
          loc='best', fancybox = True)
leg.get_frame().set_alpha(0.5)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., height + 20, 
                '%d'%int(height), ha = 'center', va = 'bottom')
        
autolabel(rects1)

for i in range(4):
    height = rects2[i].get_height() + rects1[i].get_height()
    ax.text(rects2[i].get_x() + rects2[i].get_width()/2., height + 20,
            '%d'%int(height - rects1[i].get_height()), ha = 'center', va = 'bottom')

autolabel(rects3)

plt.show()

# <codecell>


