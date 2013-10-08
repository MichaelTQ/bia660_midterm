# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pymysql
import string
from collections import Counter

db_user = "bia_user"
db_password = "biabiabia"
db_name = "ios_compare_db"
#tbl_name = "ios_four_tweets"
#str_result_file = '/users/michaelt/downloads/results/keywords_ios4.txt'

list_tbl_names = ['ios_four_tweets',
                  'ios_five_tweets',
                  'ios_six_tweets',
                  'ios_seven_tweets',
                  'iphone3gs_tweets',
                  'iphone4_tweets',
                  'iphone4s_tweets',
                  'iphone5_tweets',
                  'iphone5s_tweets',
                  'iphone5s_only_tweets',
                  'iphone5c_only_tweets']
list_result_files = ['./results/keywords_ios4.txt',
                     './results/keywords_ios5.txt',
                     './results/keywords_ios6.txt',
                     './results/keywords_ios7.txt',
                     './results/keywords_iphone3gs.txt',
                     './results/keywords_iphone4.txt',
                     './results/keywords_iphone4s.txt',
                     './results/keywords_iphone5.txt',
                     './results/keywords_iphone5s.txt',
                     './results/keywords_iphone5s_only.txt',
                     './results/keywords_iphone5c_only.txt']

if len(list_tbl_names) == len(list_result_files):
    print "matches!"
else:
    print "lists doe not match!"

# <codecell>

list_puncts = []
for each in string.punctuation:
    list_puncts.append(each)
#print list_puncts

# <codecell>

def removePunc(tmp_str):
    for i in tmp_str:
        if i in list_puncts:
            tmp_str = tmp_str.replace(i, "")
    return tmp_str

# <codecell>

list_useless_words = ['of', 'update', 'updated', 'itunes', 'be', 'will', 'so', 'ipod', 'out', 
                      'touch', 'that', 'this', 'ios', '4', 'iphone', 'for', 'the', 'to', 'on', 
                      'and', 'is', 'with', 'new', 'i','apple', 'in', 'a', 'app', 'no', 'rt', 
                      'apps', 'it', 'you', 'my', 'ipad', 'now', 'have', 'gets', 'get', 'its', 
                      'has', 'today', 'apples', 'but', '5', '6', '7', 'just', 'im', 'about',
                      'like', 'not', 'your', 'phone', '5s', '4s', 'dont', 'if', 'are', 'from',
                      'phone', 'me', 'or', 'what', 'when', 'all', 'tomorrow', 'can', 'comes', 'how',
                      'cant', 'wait', 'do', 'comes', 'at', 'via', 'time', 'store', 'an', 'than',
                      'iphone4', 'early', 'june', 'want', '5c', 'ad', 'one', 'got', 'look', 'by', 
                      '40', 'support', 'download', 'features', '8', '2', 's', 'upgrade', '3gs',
                      'launch', 'video', 'day', 'up', 'here', 'first', 'review', 'giving', 'more',
                      'away', '30', 'pre', 'preorders']

# <codecell>

def writeWordCounts(tbl_name, str_result_file):
    list_all_words = []
    conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = db_user, 
                           passwd = db_password, db = db_name)
    list_contents = []

    #get the data! get first 20 rows newest tweet first
    str_sql_get = 'select tw_url, tw_content, tw_time from ' + tbl_name + ' order by tw_time DESC'
    cur = conn.cursor()

    cur.execute(str_sql_get)
    for row in cur:
        content = row[1]
        list_contents.append(content)
    cur.close()
    conn.close()
    
    for content in list_contents:
        content = content.lower()
        content = removePunc(content)
        tmp_list = content.split()
        #tmp_list = removeUselessWords(tmp_list)
        list_all_words = list_all_words + tmp_list
    mycnt = Counter(list_all_words)
    for word in list(mycnt):
        if word in list_useless_words:
            del mycnt[word]
    list_count_results = mycnt.most_common(50)
    print list_count_results

    f = open(str_result_file, 'w')
    for i in range(20):
        f.write(list_count_results[i][0])
        f.write(": ")
        f.write(str(list_count_results[i][1]))
        f.write('\n')
    f.close()

# <codecell>

for i in range(len(list_tbl_names)):
    writeWordCounts(list_tbl_names[i], list_result_files[i])

# <codecell>


# <codecell>


