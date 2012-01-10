# -*- coding: utf-8 -*-
# bscrawler lite by Ian Lurie
# Huge kudos to BeautifulSoup
# lite version differs only in that it does not use database storage
#!/usr/bin/env python
import sys
import httplib
import urllib2
import urlparse
import string
from BeautifulSoup import BeautifulSoup, SoupStrainer
from time import gmtime, strftime, time
import sqlite3


def getPage(root,link):
    #does all the dirty work re: finding the page in the URL
    parsedUrl = urlparse.urlparse(link)
    site = parsedUrl.netloc
    if (parsedUrl.query):
        page = parsedUrl.path + '?' + parsedUrl.query
    else:
        page = parsedUrl.path
    if (page == root):
        page = "/"
        site = root
    if (site == ''):
        site = root
    if (site != root):
        external = 1
    else:
        external = 0
    return link, site, page, external

def fixPage(page):
    #tests to make sure page starts with "/"
    test = page.find("/",0,1)
    if (test == -1):
        page = "/" + page
    return page


def gera_lista_links():
        pass


def check_url_existence(url, base, tabela):
        con = sqlite3.connect(base)
        cur = con.cursor()
        cur.execute('select * from %s where url="%s"' % (tabela, url))
        data = cur.fetchall()
        con.close()
        if len(data) == 0:
                return True
        else:
                return False

def insert_table_links(url, base, tabela):
        # Cria uma conexão e um cursor
        if check_url_existence(url, base, tabela):
                con = sqlite3.connect(base)
                cur = con.cursor()
                sql = 'insert into %s values ("%s", %s)' % (tabela, url, 0)
                cur.execute(sql)
                con.commit()
                con.close()
        else:
                pass

def select_de_url(base, tabela):
        con = sqlite3.connect(base)
        cur = con.cursor()
        cur.execute('select url from %s' % (tabela))
        data = cur.fetchall()       
        return data


def check_word(url, word):
        word = word.lower()
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        document = str(response.read()).lower()    
        if word in document:
            return True
        else:
            return False

if __name__ == "__main__":
    con = sqlite3.connect("crawler.db")
    cur = con.cursor()
    cur.execute('select * from links limit 200')
    data = cur.fetchall()
    count = 0
    count_strike = 0
    saida = 0
    for da in data:
        url = da[0]
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            document = response.read()
            doc_list = document.split("\n")
        except:
            print "erro urllib"
        linha = 1
        for d in doc_list :
            linha_minuscula = d.lower ()
            if "jesus" in linha_minuscula:
                print linha_minuscula
                print "Linha %s - %s"  % (linha, url)
                linha = linha + 1
                count_strike = count_strike + 1
            else:
                linha = linha + 1
                
	count = count + 1


    print "count = %s - count_strike = %s\n\n" % (count, count_strike)


