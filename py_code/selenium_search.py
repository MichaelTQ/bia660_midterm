# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import pymysql
import re

import time
from datetime import datetime
import calendar

# <codecell>

def myParseDateTime(str):
    tmp_list = str.split(' ')
    hour_min = tmp_list[0].split(':')
    minute = hour_min[-1]
    hour = hour_min[0]
    if(tmp_list[1] == "PM"):
        hour = int(hour) + 12
    minute = int(minute)
    d = int(tmp_list[3])
    y = int(tmp_list[5])+2000
    dic_months = dict((v,k) for k,v in enumerate(calendar.month_abbr))
    m = dic_months[tmp_list[4]]
    dt = datetime(y, m, d, hour, minute, 0)
    return dt

# <codecell>

dbuser = "bia_user"
dbpsw = "biabiabia"
dbname = "ios_compare_db"

# <codecell>

def myDBInsert(dbuser, dbpsw, dbname, tbl_name, search_con, t_since, t_until, page_num, lang, sort_how):
    search_url = 'http://topsy.com/s?q=' + search_con + '&type=tweet&sort=-date&language=' + \
    lang + '&offset=' + str(page_num) + '0&mintime=' + t_since + '&maxtime=' + t_until
    list_tweets = []

    browser = webdriver.Firefox()
    browser.get(search_url)
    assert "Twitter Search, Monitoring, & Analytics | Topsy.com" in browser.title
    try:
        elem_list = browser.find_elements_by_class_name('media-body')
    except NoSuchElementException:
        assert 0, "Not find!"

    for elem in elem_list:
        id_html = elem.get_attribute("innerHTML")
        soup_all = BeautifulSoup(id_html)
        soup_id_name = soup_all.find(attrs = {"class": "media-heading"})
        tmp_id_name_list = soup_id_name.text.split(' @')
        tmp_name = tmp_id_name_list[0]
        tmp_id = tmp_id_name_list[-1]
        #print tmp_id + "\t" + tmp_name #person's id & name the tweet belonged to
        str_uurl = "http://twitter.com/" + tmp_id #this guy's twitter url
        #print str_uurl
        soup_content = soup_id_name.nextSibling
        str_content = soup_content.getText(separator = u" ")
        #print str_content #tweet content
        soup_turl = soup_all.find(attrs = {"class": "muted"})
        str_turl = soup_turl["href"]
        #print str_turl #tweet url
        try:
            f = urllib.urlopen(str_turl)
        except IOError, e:
            print "cannot fetch tweet_url, donno why...",
            continue
        tweet_html = f.read()
        soup_tweet = BeautifulSoup(tweet_html)
        tag_time = soup_tweet.findAll('span', attrs = {"class":"metadata"})
        if(len(tag_time) != 0):
            str_ttime = tag_time[0].find('span')['title']
            #print str_ttime + "\n" #time of the tweet_html
            try:
                dt = myParseDateTime(str_ttime)
            except TypeError, e:
                print " type error!",
                continue
            #print dt
        else:
            str_ttime = ""
            dt = datetime.now()
            dt = None
            #print dt
        list_tw_con = [tmp_id, tmp_name, str_uurl, str_content, str_turl, dt]
        #print list_tw_con
        list_tweets.append(list_tw_con)
    conn = pymysql.connect(host = 'localhost', port = 3306, user = dbuser, passwd = dbpsw, db = dbname)
    cur = conn.cursor()
    j = 1;
    for i in list_tweets:
        if(i[5] == None):
            str_insert_sql = "insert ignore into " + tbl_name + " values( '" + re.escape(i[0]) + "', '" + re.escape(i[1]) + \
            "', '" + re.escape(i[2]) + "', '" + re.escape(i[3]) + "', '" + re.escape(i[4]) + \
            "', '" + "NULL" + "');"
        else:
            str_insert_sql = "insert ignore into " + tbl_name + " values( '" + re.escape(i[0]) + "', '" + re.escape(i[1]) + \
            "', '" + re.escape(i[2]) + "', '" + re.escape(i[3]) + "', '" + re.escape(i[4]) + \
            "', '" + i[5].isoformat(' ') + "');"
        try:
            cur.execute(str_insert_sql)
        except UnicodeEncodeError, e:
            print "unicode problem!",
            continue
        #print str_insert_sql
        cur.fetchall()
        cur.connection.commit()
        print str(j)+"/10", " ",
        j = j + 1
    cur.close()
    conn.close()
    browser.close()
    print "\nPage:" + str(page_num)

# <codecell>

def getSUTimeList(t_const):
    myList = []
    for i in range(10):
        myList.append(str(t_const + i*3600*24))
    print myList
    return myList

# <codecell>

#iOS 4 searching contents:
search_con = '\"iOS 4\"' #run again using 'iOS4'
t_const = 1276646411
list_sin_until_time = getSUTimeList(t_const)
t_since = list_sin_until_time[0]
t_until = list_sin_until_time[1]

page_num = 0 #page #, 1/2/3/4/5...
lang = 'en'
sort = ['-date','date']#newest or oldest

search_url = 'http://topsy.com/s?q=' + search_con + '&type=tweet&sort=' + sort[0] + '&language=' + lang + '&offset=' + str(page_num) + '0&mintime=' + t_since + '&maxtime=' + t_until

print search_url

# <codecell>

#iOS 4!!!
tbl_name = "ios_four_tweets"
for sort_index in range(2):
    for since_until_index in range(9):
        for page_num in range(10):
            myDBInsert(dbuser, dbpsw, dbname, tbl_name, search_con, list_sin_until_time[since_until_index],
                       list_sin_until_time[since_until_index + 1], page_num, lang, sort[sort_index])

# <codecell>

#iOS 5 searching contents:
search_con = '\"iOS 5\"' #run again using 'iOS5'
t_const = 1317945611
list_sin_until_time = getSUTimeList(t_const)
t_since = list_sin_until_time[0]
t_until = list_sin_until_time[1]

page_num = 0 #page #, 1/2/3/4/5...
lang = 'en'
sort = ['-date','date']#newest or oldest

search_url = 'http://topsy.com/s?q=' + search_con + '&type=tweet&sort=' + sort[0] + '&language=' + lang + '&offset=' + str(page_num) + '0&mintime=' + t_since + '&maxtime=' + t_until

print search_url

# <codecell>

#insert in to table ios_five_tweets
tbl_name = 'ios_five_tweets'
for sort_index in range(2):
    for since_until_index in range(9):
        for page_num in range(10):
            myDBInsert(dbuser, dbpsw, dbname, tbl_name, search_con, list_sin_until_time[since_until_index],
                       list_sin_until_time[since_until_index + 1], page_num, lang, sort[sort_index])

# <codecell>

#iOS 6 searching contents:
search_con = '\"iOS 6\"' #run again using 'iOS6'
t_const = 1347580811
list_sin_until_time = getSUTimeList(t_const)
t_since = list_sin_until_time[0]
t_until = list_sin_until_time[1]

page_num = 0 #page #, 1/2/3/4/5...
lang = 'en'
sort = ['-date','date']#newest or oldest

search_url = 'http://topsy.com/s?q=' + search_con + '&type=tweet&sort=' + sort[0] + '&language=' + lang + '&offset=' + str(page_num) + '0&mintime=' + t_since + '&maxtime=' + t_until

print search_url

# <codecell>

#insert in to table ios_six_tweets
tbl_name = 'ios_six_tweets'
for sort_index in range(2):
    for since_until_index in range(9):
        for page_num in range(10):
            myDBInsert(dbuser, dbpsw, dbname, tbl_name, search_con, list_sin_until_time[since_until_index],
                       list_sin_until_time[since_until_index + 1], page_num, lang, sort[sort_index])

# <codecell>

#iOS 7 searching contents:
search_con = '\"iOS 7\"' #run again using 'iOS7'
t_const = 1379462411
list_sin_until_time = getSUTimeList(t_const)
t_since = list_sin_until_time[0]
t_until = list_sin_until_time[1]

page_num = 0 #page #, 1/2/3/4/5...
lang = 'en'
sort = ['-date','date']#newest or oldest

search_url = 'http://topsy.com/s?q=' + search_con + '&type=tweet&sort=' + sort[0] + '&language=' + lang + '&offset=' + str(page_num) + '0&mintime=' + t_since + '&maxtime=' + t_until

print search_url

# <codecell>

#insert in to table ios_six_tweets
tbl_name = 'ios_seven_tweets'
for sort_index in range(2):
    for since_until_index in range(9):
        for page_num in range(10):
            myDBInsert(dbuser, dbpsw, dbname, tbl_name, search_con, list_sin_until_time[since_until_index],
                       list_sin_until_time[since_until_index + 1], page_num, lang, sort[sort_index])

