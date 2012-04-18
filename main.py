#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import HTMLParser

URL = \
    'http://www.tntvillage.scambioetico.org/index.php?act=allreleases&st=0&filter=&sb=1&sd=0&cat=4'


class MyHTMLParser(HTMLParser.HTMLParser):

    def __init__(self, *args, **argd):
        HTMLParser.HTMLParser.__init__(self, *args, **argd)
        self.count = {'table': 0, 'tr': 0}

    def handle_starttag(self, tag, attrs):
        if tag == 'table' and ('class', 'copyright') in attrs:
            assert self.count['table'] == 0
            self.count['table'] = 1
            return
        if tag == 'table' and self.count['table'] > 0:
            self.count['table'] += 1
            return
        if tag == 'tr' and self.count['table'] > 0 and self.count['tr'] \
            == 0:
            assert self.count['tr'] == 0
            self.count['tr'] = 1
            return
        if tag == 'tr' and self.count['table'] > 0 and self.count['tr'] \
            > 0:
            self.count['tr'] += 1
            return
        if tag == 'td' and self.count['tr'] == 1:
            print 'td'

    def handle_endtag(self, tag):
        if tag == 'table' and self.count['table'] > 0:
            self.count['table'] -= 1
            return
        if tag == 'tr' and self.count['table'] > 0:
            assert self.count['tr'] > 0
            self.count['tr'] -= 1
            return

    def handle_data(self, data):
        if self.count['tr'] == 1:
            print data


if __name__ == '__main__':
    response = urllib2.urlopen(URL)
    parser = MyHTMLParser()
    parser.feed(response.read())
