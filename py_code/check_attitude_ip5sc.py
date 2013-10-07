# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pymysql

# <codecell>

neg_words = ['hate','terrible','awful','worse','worst','difficult','struggle','pain', 'bug', 'slow',
             'annoy','bad', 'annoying', ':(', 'horribl', 'not working', 'don\'t like', 'dont like', 'suffer', 'problem']
pos_words = ['love', 'loving','like','good','great','easy','awesome','brilliant','interesting',
             'fantastic','wonderful','amazing','stunning','charming', 'can\'t wait', 'smooth', 
             'congrats', ':)', 'cool', 'pleasant', 'pleased', 'looking good', 'satisf']

db_user = "bia_user"
db_password = "biabiabia"
db_name = "ios_compare_db"

# <codecell>

f = open('./att_words/pos_words.txt', 'r+')#txt file with words of positive attitude
for line in f:
    word = line[:-1]
    if word not in pos_words:
        pos_words.append(word)
f.close()

f = open('./att_words/neg_words.txt', 'r+')#txt file with words of negative attitude
for line in f:
    word = line[:-1]
    if word not in neg_words:
        neg_words.append(word)
f.close()

#print neg_words
#print "\n\n"
#print pos_words

# <codecell>

list_pos_iphone5s = []
list_neg_iphone5s = []
list_pos_iphone5c = []
list_neg_iphone5c = []

iphone5s_count = 0
iphone5c_count = 0

# <codecell>

def getAttitude(db_user, db_password, db_name, tbl_name):
    conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = db_user, passwd = db_password, db = db_name)
    str_sql_count = 'select count(*) from ' + tbl_name
    str_sql_get = 'select tw_url, tw_content, tw_time from ' + tbl_name + ' order by tw_time DESC'
    #print str_sql_get
    #print "\n"
    cur = conn.cursor()
    cur.execute(str_sql_count)
    (all_count,) = cur.fetchone()

    list_pos = []
    list_neg = []

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
                    
    #print len(list_pos)
    #print len(list_neg)
    #print "\n"
    #for sen in list_pos:
    #    print sen
    #print "\n\n\n"
    #for sen in list_neg:
    #    print sen
    cur.close()
    conn.close()
    return [list_pos, list_neg, all_count]

# <codecell>

#get Attitude for iPhone 5S only
tbl_name = "iphone5s_only_tweets"
[list_pos_iphone5s, list_neg_iphone5s, iphone5s_count] = getAttitude(db_user, db_password, db_name, tbl_name)

# <codecell>

#get Attitude for iPhone 4C only
tbl_name = "iphone5c_only_tweets"
[list_pos_iphone5c, list_neg_iphone5c, iphone5c_count] = getAttitude(db_user, db_password, db_name, tbl_name)

# <codecell>

# list_ios_attitude = [[list_pos_iphone5c, list_neg4], [list_pos5, list_neg5], [list_pos6, list_neg6], [list_pos7, list_neg7]]

# <codecell>

#print out results:

perc_pos5 = 100*float(len(list_pos_iphone5s))/float(iphone5s_count)
perc_neg5 = 100*float(len(list_neg_iphone5s))/float(iphone5s_count)
perc_pos6 = 100*float(len(list_pos_iphone5s))/float(iphone5c_count)
perc_neg6 = 100*float(len(list_neg_iphone5c))/float(iphone5c_count)

pos_v_neg5 = float(len(list_pos_iphone5s))/float(len(list_neg_iphone5s))
pos_v_neg6 = float(len(list_pos_iphone5c))/float(len(list_neg_iphone5c))

print "iPhone 5S Only:"
print "Positive: ", len(list_pos_iphone5s), "/", iphone5s_count, "\t",
print("%.5f"% perc_pos5),
print "%"
print "Negative: ", len(list_neg_iphone5s), "/", iphone5s_count, "\t",
print("%.5f"% perc_neg5),
print "%"
print "Positive vs. Negative:\t",
print("%.5f"% pos_v_neg5)
print "===================================="
print "iPhone 5C Only:"
print "Positive: ", len(list_pos_iphone5c), "/", iphone5c_count, "\t",
print("%.5f"% perc_pos6),
print "%"
print "Negative: ", len(list_neg_iphone5c), "/", iphone5c_count, "\t",
print("%.5f"% perc_neg6),
print "%"
print "Positive vs. Negative:\t",
print("%.5f"% pos_v_neg6)

# <codecell>


