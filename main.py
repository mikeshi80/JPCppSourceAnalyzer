#!/usr/bin/env python
# -*- encoding: utf8 -*-

import sys
import os.path
import logging
import codecs

from JPAnalyzer import analyze


def visitor(options, dirname, names):
    mynames = filter(lambda n : os.path.splitext(n)[1].lower() in options[1], names)
    
    data = options[0]
    for name in mynames:
        fname = os.path.join(dirname, name)
        if not os.path.isdir(fname):
            data[fname] = analyze(fname)

def output(data):
    f = codecs.open('output.txt', 'w', 'utf-8')


    dkeys = data.keys()
    dkeys.sort()
    for k in dkeys:
        if len(data[k]) == 0:
            continue

        lines = []
        
        lines.append(u'########## %s ##########' % k.decode(sys.getfilesystemencoding()))

        vkeys = data[k].keys()
        vkeys.sort()
        for ln in vkeys:
            lines.append('%d, \t%s' % (ln, data[k][ln].rstrip('\r\n')))

        f.writelines('\r\n'.join(lines))
        f.writelines('\r\n')

    f.close()

'''
Usage:
    python extractJP.py topdir .ext1 [.ext2] ...
'''
if __name__ == "__main__":
    logging.basicConfig(filename='analyze.log')

    topdir = sys.argv[1]

    filters = sys.argv[2:]

    data = {}

    os.path.walk(topdir, visitor, (data, filters))

    output(data)

    


