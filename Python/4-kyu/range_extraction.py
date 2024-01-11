'''
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
'''

def solution(args):
    res = []
    beg = args[0]
    end = args[0]
    for i in args[1:] + [""]:        
        if i != end + 1:
            if end == beg:
                res.append(str(beg))
            elif end == beg + 1:
                res.extend([str(beg),str(end)])
            else:
                res.append(str(beg) + "-" + str(end))
            beg = i
        end = i

    return ",".join(res)
