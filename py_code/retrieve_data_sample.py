# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pymysql

# <codecell>

db_user = "bia_user"
db_password = "biabiabia"
db_name = "ios_compare_db"
tbl_name = "ios_four_tweets"

# <codecell>

conn = pymysql.connect(host = 'localhost', port = 3306, user = db_user, passwd = db_password, db = db_name)

#get the data! get first 20 rows newest tweet first
str_sql = 'select tw_url, tw_content, tw_time from ' + tbl_name + ' order by tw_time DESC limit 20'
cur = conn.cursor()
cur.execute(str_sql)

for row in cur:
    for i in row:
        print i
    print "\n"

cur.close()
conn.close()

# <codecell>


