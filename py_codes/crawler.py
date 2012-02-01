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
        cur.execute('select url from %s where checked=0' % (tabela))
        data = cur.fetchall()       
        return data

def mark_url_as_cheked(url, base):
        con = sqlite3.connect(base)
        cur = con.cursor()
        cur.execute('update links set checked=1 where url ="%s"' % url)
        con.commit()


if __name__ == "__main__":
        #print check_url_existence('blablbla', 'crawler.db', 'links')
	base = 'crawler.db'
        data = select_de_url(base, 'links')
        #data = [("http://www.xvideos.com")]
	for d in data:
                #print d[0]
                print "start time ",strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),"\n\n\n"


                root = d[0].strip('http://')
                print root
                outside = '1'


                linkz = []
                crawled = []
                imgz = []
                counter = 0
                start = time()
                result=0
                parsedRoot = urlparse.urlparse(root)

                if parsedRoot.port == 80:
                    hostRoot = parsedRoot.netloc[:-3]
                else:
                    hostRoot = parsedRoot.netloc

                linkz.append(root)

                imageTypes = "jpg,gif,png"
                skipIt = "javascript,mailto"


                for l in linkz:
                    try:
                        conn = httplib.HTTPConnection(root)
                    
                        e = getPage(root,l)
                        link = e[0]
                        site = e[1]
                        page = e[2]
                        external = e[3]
                        page = fixPage(page)
                        skipCheck = skipIt.find(l)
                        if (outside == 1):
                            skipCheck2 = 0
                        else:
                            if (external == 0):
                                skipCheck2 = 0
                            else:
                                skipCheck2 = 1
                        if (skipCheck == -1) & (skipCheck2 == 0):
                            conn.request("GET", page)
                            code = conn.getresponse() # read response code 
                            src = code.read()
                            src = str(src)
                            flist = l.split('.')
                            ftype = flist[-1]
                            imageCheck = imageTypes.find(ftype)
                            links = SoupStrainer('a') # grab all anchors
                            imgs = SoupStrainer('img') # grab all img elements
                            if (imageCheck == -1): 
                                bs = BeautifulSoup(src, parseOnlyThese=links) # parse for anchors
                                if (imageCheck == -1): 
                                    print "Crawling\t",l,"\t",code.status
                                    # loop through all of the anchors found on the page
                                    # crawler only records the FIRST time it finds a link. If a link is on 20 pages
                                    # it will still only show up once in the log.
                                    for j in bs.findAll('a', {'href':True}):
                                        testresult = 0
                                        absUrl = urlparse.urljoin(l, j['href'])
                                        # check for javascript/mailto
                                        checkAbs = absUrl.split(':')
                                        checkAbs = checkAbs[0]
                                        checkAbs = checkAbs.strip()
                                        nskipCheck = skipIt.find(checkAbs)
                                        if ((nskipCheck == -1) & (absUrl.find('#') == -1)):
                                            absUrl = absUrl.strip()
                                            absUrl = absUrl.replace(' ','%20')
                                            e = getPage(root,absUrl)
                                            link = e[0]
                                            site = e[1]
                                            page = e[2]
                                            external = e[3]
                                            page = fixPage(page)
                                            if (outside == 1):
                                                skipCheck2 = 0
                                            else:
                                                if (external == 0):
                                                    skipCheck2 = 0
                                                else:
                                                    skipCheck2 = 1
                                            if (skipCheck2 == 0):
                                                try:
                                                    if (page not in linkz):
                                                        conn.request("GET", page)
                                                        tcode = conn.getresponse() # read response code 
                                                        conType = tcode.getheader("content-type")
                                                        conTest = conType.find("text/html")
                                                        status = str(tcode.status)
                                                        if (status != '200'):
                                                            print '\t' + page + '\t' + 'page' + '\t' + status + '\t'
                                                        else:
                                                            if (conTest == 0): # only doing pages, thank you very much
                                                                cleanUrl = absUrl.strip()
                                                                nimageCheck = imageTypes.find(cleanUrl)
                                                                if (nimageCheck == -1):
                                                                    thistype = "page"
                                                                    linkz.append(page)
                                                                else:
                                                                    thistype = "image"
                                                                print '\t' + page + '\t' + thistype + '\t' + str(tcode.status)
                                                                counter = counter + 1
                                                    else:
                                                        print '\t' + page + '\t' + thistype + '\t' + 'already crawled'
                                                except:
                                                    pass        
                                            else:
                                                #print '\t' + absUrl + '\t' + 'skipped external URL'
                                                print absUrl
                                                try:
                                                        insert_table_links(absUrl, 'crawler.db', 'links')
                                                except:
                                                        print 'erro'
                                                
                        # now to try to grab some images on the same page
                                    bsi = BeautifulSoup(src, parseOnlyThese=imgs)
                                    for i in bsi.findAll('img', {'src':True}):
                                        absUrl = urlparse.urljoin(l, i['src'])
                                        e = getPage(root,absUrl)
                                        external = e[3]
                                        img = e[2]
                                        site = e[1]
                                        img = fixPage(img)
                                        if (img not in imgz):
                                            conn.request("GET", img)
                                            tcode = conn.getresponse() # read response code 
                                            conType = tcode.getheader("content-type")
                                            if (external == 0):
                                                print '\t' + img + '\timage' + '\t' + str(tcode.status)
                                        else:
                                            print '\t' + img + '\timage' + '\t' + 'already crawled' 
                                        counter = counter + 1
                                        imgz.append(img)
                        conn.close()
                    except:
                        pass


                print "Completed at ",strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),"\n\n\n",counter," urls in ", (time() - start)
                mark_url_as_cheked(d[0], base)
