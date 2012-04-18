#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
from lxml import etree

URL = \
    'http://www.tntvillage.scambioetico.org/index.php?act=allreleases&st=%d&filter=&sb=1&sd=0&cat=4'


def getUrl(page):
    return URL % (page * 35)


def getPageContent(page):
    response = urllib2.urlopen(getUrl(page))
    parser = etree.HTMLParser()
    tree = etree.parse(response, parser)
    root = tree.getroot()
    tableElement = \
        root.findall('body/div/div/table/tr/td/div/table/tr/td/div/table[@class="copyright"]'
                     )[0]
    rows = tableElement.findall('tr')
    rows = [e for (i, e) in enumerate(rows) if i > 0]
    values = []
    for r in rows:
        d = {'title': r[1].findall('a')[0].text,
             'torrent': r[0].findall('span/a')[1].attrib['href']}
        values.append(d)
    return values


def pagesGenerator():
    page = 0
    while True:
        yield getPageContent(page)


if __name__ == '__main__':
    for (i, pageContent) in enumerate(pagesGenerator()):
        print i
