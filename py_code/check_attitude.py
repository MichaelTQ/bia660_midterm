# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pymysql

# <codecell>

neg_words = ['hate','terrible','awful','worse','worst','difficult','struggle','pain', 'bug',
             'annoy','bad', 'annoying', ':(', 'horribl', 'not working', 'don\'t like', 'dont like', 'suffer', 'problem']
pos_words = ['love', 'loving','like','good','great','easy','awesome','brilliant','interesting',
             'fantastic','wonderful','amazing','stunning','charming', 'can\'t wait', 'smooth', 
             'congrats', ':)', 'cool', 'pleasant', 'pleased', 'looking good', 'satisf']

db_user = "bia_user"
db_password = "biabiabia"
db_name = "ios_compare_db"
tbl_name = "ios_four_tweets"

# <codecell>

f = open('/users/michaelt/downloads/pos_words.txt', 'r+')
for line in f:
    word = line[:-1]
    if word not in pos_words:
        pos_words.append(word)
f.close()

f = open('/users/michaelt/downloads/neg_words.txt', 'r+')
for line in f:
    word = line[:-1]
    if word not in neg_words:
        neg_words.append(word)
f.close()

#print neg_words
#print "\n\n"
#print pos_words

# <codecell>

conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = db_user, passwd = db_password, db = db_name)

str_sql_count = 'select count(*) from ' + tbl_name
str_sql_get = 'select tw_url, tw_content, tw_time from ' + tbl_name + ' order by tw_time DESC'
print str_sql_get
print "\n"
cur = conn.cursor()
cur.execute(str_sql_count)
(all_count,) = cur.fetchone()

list_pos = [];
list_neg = [];

cur.execute(str_sql_get)
for row in cur:
    content = row[1].lower()
    
    for word in neg_words:
        if word in content:
            list_neg.append(content)
            break
    if word == neg_words[-1]:
        for word in pos_words:
            if word in content:
                list_pos.append(content)
                break
                
print len(list_pos)
print len(list_neg)
print "\n"
for sen in list_pos:
    print sen
print "\n\n\n"
for sen in list_neg:
    print sen
cur.close()
conn.close()

# <codecell>


