'''
Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

Write a function that computes the nth smallest Hamming number.

Specifically:

The first smallest Hamming number is 1 = 203050
The second smallest Hamming number is 2 = 213050
The third smallest Hamming number is 3 = 203150
The fourth smallest Hamming number is 4 = 223050
The fifth smallest Hamming number is 5 = 203051
The 20 smallest Hamming numbers are given in the Example test fixture.
'''

def hamming(n):
    res = [1]
    i = 0
    j = 0
    k = 0
    count = 1
    while n>count:
        num = min(res[i]*2, res[j]*3, res[k]*5)
        if num == res[i]*2:
            i+=1
        if num == res[j]*3:
            j+=1
        if num == res[k]*5:
            k+=1
        count += 1
        res.append(num)
    return res[-1]
