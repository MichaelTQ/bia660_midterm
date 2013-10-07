# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pymysql

# <codecell>

#Big difference with or without 'slow'
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


list_pos_iphone3gs = []
list_neg_iphone3gs = []
list_pos_iphone4 = []
list_neg_iphone4 = []
list_pos_iphone4s = []
list_neg_iphone4s = []
list_pos_iphone5 = []
list_neg_iphone5 = []
list_pos_iphone5s = []
list_neg_iphone5s = []
iphone3gs_count = 0
iphone4_count = 0
iphone4s_count = 0
iphone5_count = 0
iphone5s_count = 0

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

    list_pos_iphone = []
    list_neg_iphone = []

    cur.execute(str_sql_get)
    for row in cur:
        content = row[1].lower()
        
        for word in neg_words:
            if word in content:
                list_neg_iphone.append(content)
                break
        if word == neg_words[-1]:
            for word in pos_words:
                if word in content:
                    list_pos_iphone.append(content)
                    break
                    
    #print len(list_pos_iphone)
    #print len(list_neg_iphone)
    #print "\n"
    #for sen in list_pos_iphone:
    #    print sen
    #print "\n\n\n"
    #for sen in list_neg_iphone:
    #    print sen
    cur.close()
    conn.close()
    return [list_pos_iphone, list_neg_iphone, all_count]

# <codecell>

#get Attittude for iphone3gs
tbl_name = "iphone3gs_tweets"
[list_pos_iphone3gs, list_neg_iphone3gs, iphone3gs_count] = getAttitude(db_user, db_password, db_name, tbl_name)

#get Attitude for iphone4
tbl_name = "iphone4_tweets"
[list_pos_iphone4, list_neg_iphone4, iphone4_count] = getAttitude(db_user, db_password, db_name, tbl_name)

# <codecell>

#get Attitude for iphone4s
tbl_name = "iphone4s_tweets"
[list_pos_iphone4s, list_neg_iphone4s, iphone4s_count] = getAttitude(db_user, db_password, db_name, tbl_name)

# <codecell>

#get Attitude for iphone5
tbl_name = "iphone5_tweets"
[list_pos_iphone5, list_neg_iphone5, iphone5_count] = getAttitude(db_user, db_password, db_name, tbl_name)

# <codecell>

#get Attitude for iphone5s
tbl_name = "iphone5s_tweets"
[list_pos_iphone5s, list_neg_iphone5s, iphone5s_count] = getAttitude(db_user, db_password, db_name, tbl_name)

# <codecell>

list_iphone_attitude = [[list_pos_iphone4, list_neg_iphone4], [list_pos_iphone4s, list_neg_iphone4s], [list_pos_iphone5, list_neg_iphone5], [list_pos_iphone5s, list_neg_iphone5s]]

# <codecell>

#print out results:

perc_pos3 = 100*float(len(list_pos_iphone3gs))/float(iphone3gs_count)
perc_neg3 = 100*float(len(list_neg_iphone3gs))/float(iphone3gs_count)
perc_pos4 = 100*float(len(list_pos_iphone4))/float(iphone4_count)
perc_neg4 = 100*float(len(list_neg_iphone4))/float(iphone4_count)
perc_pos5 = 100*float(len(list_pos_iphone4s))/float(iphone4s_count)
perc_neg5 = 100*float(len(list_neg_iphone4s))/float(iphone4s_count)
perc_pos6 = 100*float(len(list_pos_iphone5))/float(iphone5_count)
perc_neg6 = 100*float(len(list_neg_iphone5))/float(iphone5_count)
perc_pos7 = 100*float(len(list_pos_iphone5s))/float(iphone5s_count)
perc_neg7 = 100*float(len(list_neg_iphone5s))/float(iphone5s_count)

pos_v_neg3 = float(len(list_pos_iphone3gs))/float(len(list_neg_iphone3gs))
pos_v_neg4 = float(len(list_pos_iphone4))/float(len(list_neg_iphone4))
pos_v_neg5 = float(len(list_pos_iphone4s))/float(len(list_neg_iphone4s))
pos_v_neg6 = float(len(list_pos_iphone5))/float(len(list_neg_iphone5))
pos_v_neg7 = float(len(list_pos_iphone5s))/float(len(list_neg_iphone5s))

print "iPhone 3GS"
print "Positive: ", len(list_pos_iphone3gs), "/", iphone3gs_count, "\t",
print ("%.5f"% perc_pos3),
print "%"
print "Negative: ", len(list_neg_iphone3gs), "/", iphone3gs_count, "\t",
print ("%.5f"% perc_neg3),
print "%"
print "Positive/Negative:\t",
print ("%.5f"% pos_v_neg3)
print "===================================="
print "iPhone 4:"
print "Positive: ", len(list_pos_iphone4), "/", iphone4_count, "\t",
print("%.5f"% perc_pos4),
print "%"
print "Negative: ", len(list_neg_iphone4), "/", iphone4_count, "\t",
print("%.5f"% perc_neg4),
print "%"
print "Positive/Negative:\t",
print("%.5f"% pos_v_neg4)
print "===================================="
print "iPhone 4S:"
print "Positive: ", len(list_pos_iphone4s), "/", iphone4s_count, "\t",
print("%.5f"% perc_pos5),
print "%"
print "Negative: ", len(list_neg_iphone4s), "/", iphone4s_count, "\t",
print("%.5f"% perc_neg5),
print "%"
print "Positive/Negative:\t",
print("%.5f"% pos_v_neg5)
print "===================================="
print "iPhone 5:"
print "Positive: ", len(list_pos_iphone5), "/", iphone5_count, "\t",
print("%.5f"% perc_pos6),
print "%"
print "Negative: ", len(list_neg_iphone5), "/", iphone5_count, "\t",
print("%.5f"% perc_neg6),
print "%"
print "Positive/Negative:\t",
print("%.5f"% pos_v_neg6)
print "===================================="
print "iPhone 5S:"
print "Positive: ", len(list_pos_iphone5s), "/", iphone5s_count, "\t",
print("%.5f"% perc_pos7),
print "%"
print "Negative: ", len(list_neg_iphone5s), "/", iphone5s_count, "\t",
print("%.5f"% perc_neg7),
print "%"
print "Positive/Negative:\t",
print("%.5f"% pos_v_neg7)

# <codecell>


