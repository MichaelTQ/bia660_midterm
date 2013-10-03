# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from twitter import *

# <codecell>

CONSUMER_TOKEN = 'DFt2SbICTcRct5WxNL5i2g'
CONSUMER_SECRET = 'jEYr5a9bd7zs0i5LCEieESAfnmEda1Jao4dsoINzhQ'
OAUTH_TOKEN = '214469280-G8QhbLdf3F1UgzpMfP0Rl73gVSYSV73A5S2Lin3Y'
OAUTH_SECRET = 'bhQKNT0XrF6YPAyEJaAhXHPqpnX1729XTUph2Nduas'

# <codecell>

t = Twitter(auth= OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_TOKEN, CONSUMER_SECRET))

# <codecell>

t.search.tweets(q="from:Com2uS", max_id = 384916745376391169)

# <codecell>


