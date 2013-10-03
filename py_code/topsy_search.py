# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import BeautifulSoup as bs4
import urllib
import re

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)

# <codecell>

search_con = 'ios4'
t_since = '1276473611'#time for June 14th 2010, 3600 is an hour
t_until = '1277683211'#time for June 28th 2010, 3600 is an hour
page_num = 0 #page #, 1/2/3/4/5...
lang = 'en'

search_str = 'http://topsy.com/s?q=' + search_con + '&type=tweet&sort=-date&language=' + lang + '&offset=' + str(page_num) + '0&mintime=' + t_since + '&maxtime=' + t_until
f = urllib.urlopen(search_str)

sss_html = f.read()
sssoup = bs4.BeautifulSoup(sss_html)
print sssoup.title
print search_str
print "/n/n"

# <codecell>

tmp_res = sssoup.findAll('div')
for elem in tmp_res:
    if (elem.get('class') == u'media-body'):
        print elem.getText(separator = u' ')
        print '\n\n'

# <codecell>


