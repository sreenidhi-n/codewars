# Strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
def strip_comments(strng, markers):
    res = strng.split('\n')
    for i,j in enumerate(res):
        for k in markers:
            data = j.find(k)
            if data != -1:
                j = j[:data]
        res[i] = j.rstrip(' ')
    return '\n'.join(res)
