#!/usr/bin/env python
# -*- encoding: utf8 -*-

import codecs
import logging
from CommentsRemover import removeComments
from JPChecker import hasJP

encoding = 'cp932'

def analyze(fname):
    u'''
    Analyze the file to get the analyzed result
    The result is a map

    retVal[110] = 'line without comments'
           ^^^     ^^^^^^^^^^^^^^^^^^^^^
          line no  the line string
    '''

    inComment = False
    retVal = {}
    try:
        f = codecs.open(fname, 'r', encoding)
        lineno = 0
        for line in f:
            lineno = lineno + 1
            l, inComment = removeComments(line, inComment)
            logging.debug("return line is {%s}, inComment is %s", l, inComment)
            if hasJP(l):
                retVal[lineno] = l
    except Exception as e:
        logging.error('error: %s', e)
    finally:
        f.close()
    
    return retVal


if __name__ == "__main__":
    import doctest
    doctest.testmod()


