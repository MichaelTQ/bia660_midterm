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
    hour = int(hour_min[0])
    if(tmp_list[1] == "PM"):
        hour = int(hour) + 12
        if(hour == 24):
            hour=0
    minute = int(minute)
    d = int(tmp_list[3])
    y = int(tmp_list[5])+2000
    dic_months = dict((v,k) for k,v in enumerate(calendar.month_abbr))
    m = dic_months[tmp_list[4]]
    #print y, m, d, hour, minute
    #print type(y), type(m), type(d), type(hour), type(minute)
    dt = datetime(y, m, d, hour, minute, 0)
    return dt

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
            try:
                dt = myParseDateTime(str_ttime)    
            except TypeError, e:
                print dt, ' ',
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
        #demo showing
        #print list_tw_con
        print "User ID:\t\t", list_tw_con[0]
        print "User Name:\t", list_tw_con[1]
        print "User URL:\t", list_tw_con[2]
        print "Tweet Content:\t", list_tw_con[3]
        print "Tweet URL:\t", list_tw_con[4]
        print "Tweet Time:\t",
        print list_tw_con[5]
        print "\n"
    conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = dbuser, passwd = dbpsw, db = dbname)
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
            #print "unicode problem!",
            continue
        #print str_insert_sql
        cur.fetchall()
        cur.connection.commit()
        #print str(j)+"/10", " ",
        j = j + 1
    cur.close()
    conn.close()
    browser.close()
    #print "Page:" + str(page_num), " ",

# <codecell>

dbuser = "bia_user"
dbpsw = "biabiabia"
dbname = "demo_db"
tbl_name = 'demo_tbl'
search_con = '\"iOS 4\"'
t_since = '1277078425'
t_until = '1308700814'
page_num = '3'
lang = 'en'
sort_how = '-date'

myDBInsert(dbuser, dbpsw, dbname, tbl_name, search_con, t_since, t_until, page_num, lang, sort_how)

# <codecell>


