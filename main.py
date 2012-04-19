#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import tntparser

HTML_TEMPLATE_HEADER = \
    """
<!DOCTYPE HTML PUBLIC “-//W3C//DTD XHTML 1.0 Strict//EN” “http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd”>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title></title>
    </head>
    <body>
        <table border="1">
"""

HTML_TEMPLATE_FOOTER = """
        </table>
    </body>
</html>
"""


def toTR(i, film):
    return '<tr><td>%d</td><td><a href="%s">%s</a></td><td><a href="%s">torrent</a></td></tr>' \
        % (i, film['http'], film['title'], film['torrent'])


if __name__ == '__main__':
    with open(sys.argv[1], 'w') as fp:
        fp.write(HTML_TEMPLATE_HEADER)
        for (i, film) in enumerate(tntparser.filmGenerator()):
            fp.write(toTR(i, film).encode('utf-8'))
        fp.write(HTML_TEMPLATE_FOOTER)
