# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

# <codecell>

N = 4
pos = (238, 220, 196, 174)
neg = (172, 151, 135, 133)
all_count = (813, 743, 622, 554)

# <codecell>

ind = np.arange(N)
width = 0.25

# <codecell>

fig, ax = plt.subplots()
rects1 = ax.bar(ind, pos, width, color = 'g')
rects2 = ax.bar(ind+width, neg, width, color = 'r')
rects3 = ax.bar(ind+2*width, all_count, width, color = 'y')

# <codecell>

#add some attributes
ax.set_ylabel('Tweet Numbers')
ax.set_title('Difference tweet response in iOS version')
ax.set_xticks(ind + width)
ax.set_xticklabels(('iOS4', 'iOS5', 'iOS6', 'iOS7'))
ax.legend((rects1[0], rects2[0], rects3[0]), ('Positive','Negative','All'))

# <codecell>

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/3., 1.05*height, 
                '%d'%int(height), ha = 'center', va = 'bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()

# <codecell>


