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
t_since = '2010-6-14'
t_until = '2010-6-28'
lang = 'en'

search_str = 'https://twitter.com/search?q='+ search_con +'%20lang%3A'+ lang +'%20since%3A'+ t_since +'%20until%3A' + t_until + '&src=typd&f=realtime'
f = urllib.urlopen(search_str)

sss_html = f.read()
sssoup = bs4.BeautifulSoup(sss_html)
print sssoup.title
print search_str

# <codecell>

tmp_res = sssoup.findAll('p')
for elem in tmp_res:
    if (elem.get('class') == u'js-tweet-text tweet-text'):
        print elem.getText(separator = u' ')
        print '\n\n'

# <codecell>


