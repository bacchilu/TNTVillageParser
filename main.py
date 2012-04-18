#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import HTMLParser

URL = \
    'http://www.tntvillage.scambioetico.org/index.php?act=allreleases&st=0&filter=&sb=1&sd=0&cat=4'


class Tokenizer(HTMLParser.HTMLParser):

    def __init__(self, *args, **argd):
        HTMLParser.HTMLParser.__init__(self, *args, **argd)
        self.tokens = []

    def handle_starttag(self, tag, attrs):
        self.tokens.append(('STARTTAG', tag, attrs))

    def handle_endtag(self, tag):
        self.tokens.append(('ENDTAG', tag))

    def handle_data(self, data):
        self.tokens.append(('DATA', data))

    def tokensGen(self):
        return (elem for elem in self.tokens)


def parseHeader(tokenizer):
    t = tokenizer.next()
    assert t[0] == 'STARTTAG'
    assert t[1] == 'tr'


def parseDocument(tokenizer):
    for t in tokenizer:
        if t[0] == 'STARTTAG' and t[1] == 'table' and ('class',
                'copyright') in t[2]:
            break
    parseHeader(tokenizer)


if __name__ == '__main__':
    response = urllib2.urlopen(URL)
    t = Tokenizer()
    t.feed(response.read())
    parseDocument(t.tokensGen())
