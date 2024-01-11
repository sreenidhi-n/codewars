'''
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

'''
def snail(arr):
    l1 = []
    while arr:
        for i in arr[0]:
            l1.append(i)
        arr.pop(0)
        if not arr:
            break  
        for j in arr:
            l1.append(j[-1])
            j.pop()
        for k in range((len(arr[-1])-1), -1, -1):
            l1.append(arr[-1][k])
        arr.pop()
        for l in reversed(arr):
            l1.append((l[0]))
            l.pop(0)
    return l1
