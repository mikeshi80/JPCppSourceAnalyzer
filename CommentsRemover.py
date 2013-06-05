import logging


def procCStyle(line, pos):
    logging.debug('procCStyle pos is [%d], line is {%s}', pos, line)

    start = 0
    if pos == 0: # pos == 0 means that inComment is True
        start = 0
    else: # else means inComment is False
        start = pos - 2


    if "*/" in line[pos:]: # try to find whether there is */ to end the comment
        end = line.index("*/", pos)
        logging.debug("remove the /**/ style line {%s}", line[start:end+2])
        return removeComments(line[:start] + line[end+2:], False)
    else:
        logging.debug("remove the /* style line {%s}", line[:start])
        return line[:start], True

def removeComments(line, inComment):
    '''
    return the string without comments

    @parameters
    line: the line string to remove comments
    inComment: indicate whether the line is in /* */ style comments

    @return
    return value string, inComment
    string is the value to return
    inComment is boolean value, true if we are in /* */ style comment


    >>> removeComments(u'hello world // this is the new world', False)
    (u'hello world ', False)
    >>> removeComments(u'hello world /* this is the new world*/', False)
    (u'hello world ', False)
    >>> removeComments(u'hello /* new */world', False)
    (u'hello world', False)
    >>> removeComments(u'hello world //* this is another', False)
    (u'hello world ', False)
    >>> removeComments(u'hello world //* this is another world */', False)
    (u'hello world ', False)
    >>> removeComments(u'hello world /* //this is a good test */', False)
    (u'hello world ', False)
    >>> removeComments(u'hello /*new*/world // this is a better test', False)
    (u'hello world ', False)
    >>> removeComments(u'hello world /* this is aaaa test', False)
    (u'hello world ', True)
    >>> removeComments(u'hello world /* this a aaa // test', False)
    (u'hello world ', True)
    >>> removeComments(u'*/hello world', True)
    (u'hello world', False)
    >>> removeComments(u'something else*/hello world', True)
    (u'hello world', False)
    >>> removeComments(u'something else*/hello world // this is a good day', True)
    (u'hello world ', False)
    >>> removeComments(u'something else*/hello world /* this is a good day */', True)
    (u'hello world ', False)
    >>> removeComments(u'something else*/hello world /* this is a good day //', True)
    (u'hello world ', True)
    >>> removeComments(u'something else*/hello/*yes ppg!*/ world /* this is a good day //', True)
    (u'hello world ', True)
    >>> removeComments(u'/**/', False)
    (u'', False)
    >>> removeComments(u'', False)
    (u'', False)
    >>> removeComments(u'', True)
    (u'', True)
    >>> removeComments(u'something else', True)
    (u'', True)
    >>> removeComments(u'something //else', True)
    (u'', True)
    >>> removeComments(u'something else/*hello world */ this is a good day', True)
    (u' this is a good day', False)

    '''

    if inComment:
        return procCStyle(line, 0)

    i1 = -1
    i2 = -1
    if "//" in line:
        i1 = line.index("//")
        logging.debug("meet the // comment at %d", i1)
    if "/*" in line:
        i2 = line.index("/*")
        logging.debug("meet the /* comment at %d", i2)

    if i1 > -1 and i2 > -1: # Both // and /* style comments appear
        if i1 < i2: # if // appears before /*
            logging.debug("return removed // style line {%s}", line[:i1])
            return line[:i1], False
        else:
            logging.debug("both // and /* detected")
            return procCStyle(line, i2+2)

    else:
        if i1 > -1: # Only // style comment
            logging.debug("return removed // style line {%s}", line[:i1])
            return line[:i1], False
        elif i2 > -1: # Only /* style comment
            return procCStyle(line, i2+2)
        else: # There is no comments at all
            return line, False

if __name__ == "__main__":

    import doctest
    doctest.testmod()

