#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: diego tostes

import urllib2
from BeautifulSoup import BeautifulSoup
pagina = urllib2.urlopen("http://thepiratebay.org/top/201").read()

tree = BeautifulSoup(pagina)
print tree("title").string
#print tree("table").string

