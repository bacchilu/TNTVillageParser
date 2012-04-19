#!/usr/bin/python
# -*- coding: utf-8 -*-

import tntparser

if __name__ == '__main__':
    for (i, film) in enumerate(tntparser.filmGenerator()):
        print i, film['title']
