# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import time
from datetime import date

# <codecell>

d = date.fromtimestamp(12767473867)
print d

# <codecell>

def get_id_name(strTmp):
    return strTmp.split(' @')

# <codecell>

print get_id_name("Nick Robinson @ratkat")

# <codecell>

strtmp = "http://twitter.com/Ratkat/status/16106746744"
tmp_list = strtmp.split('Ratkat')
print "".join(tmp_list[0]) + 'Ratkat'

# <codecell>

import time
import datetime
import calendar

# <codecell>

print time.strftime('%Y-%m-%d %H:%M:%S')
print '5:04 PM - 13 Jun 10'

# <codecell>

def myParseDateTime(str):
    tmp_list = str.split()
    hour_min = tmp_list[0].split(':')
    minute = hour_min[1]
    hour = hour_min[0]
    if(tmp_list[1] == "PM"):
        hour = int(hour) + 12
    minute = int(minute)
    d = int(tmp_list[3])
    y = int(tmp_list[5])+2000
    dic_months = dict((v,k) for k,v in enumerate(calendar.month_abbr))
    m = dic_months[tmp_list[4]]
    dt = datetime.datetime(y, m, d, hour, minute, 0)
    #print dt
    return dt

# <codecell>

myParseDateTime('5:04 PM - 13 Jun 10')
tmp = myParseDateTime('5:36 PM - 13 Jun 10')

# <codecell>

dict((v,k) for k,v in enumerate(calendar.month_abbr))

# <codecell>

dt = datetime.datetime.now()
dt = None
print dt

# <codecell>

time.strftime(tmp)

# <codecell>

for i in 10:
    print i

# <codecell>

for i in range(10):
    print i;

# <codecell>

list_sin_until_time = ['1276473611', '1276560011', '1276646411', '1276732811', '1276819211', '1276905611', '1276992011']
t_since = list_sin_until_time[0]
t_until = list_sin_until_time[1]

# <codecell>

for i in range(6):
    t_since = list_sin_until_time[i]
    t_until = list_sin_until_time[i+1]
    print t_since, " ", t_until

# <codecell>

import re

# <codecell>

search_con = 'ios4'
#'1276473611'time for June 14th 2010, 3600 is an hour, really not acurate!
#'1276560011'time for June 15th 2010
#'1276646411'time for June 16th 2010
#'1276732811'time for June 17th 2010
#'1276819211'time for June 18th 2010
#'1276905611'time for June 19th 2010
#'1276992011'time for June 20th 2010
list_sin_until_time = ['1276473611', '1276560011', '1276646411', '1276732811', '1276819211', '1276905611', '1276992011']
t_since = list_sin_until_time[0]
t_until = list_sin_until_time[1]

page_num = 0 #page #, 1/2/3/4/5...
lang = 'en'
sort = ['-date','date']#newest or oldest

#search_url = 'http://topsy.com/s?q=' + search_con + '&type=tweet&sort=' + sort[0] + '&language=' + lang + '&offset=' + str(page_num) + '0&mintime=' + t_since + '&maxtime=' + t_until

#print search_url

# <codecell>

for sort_index in range(2):
    for since_until_index in range(6):
        for page_num in range(10):
            print page_num, " "
        t_since = list_sin_until_time[since_until_index]
        t_until = list_sin_until_time[since_until_index]
        print t_since, " ", t_until
    print sort[sort_index]

# <codecell>

const = 1306972811
mylist = []
for i in range(10):
    mylist.append(const + i*3600*24)
    print type(mylist[i])
print mylist

# <codecell>


