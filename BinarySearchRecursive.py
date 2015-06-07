__author__ = 'mohammadsafwat'

def binarySearchRecursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearchRecursive(alist[:midpoint], item)
            else:
                return binarySearchRecursive(alist[midpoint+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearchRecursive(testlist, 3))
print(binarySearchRecursive(testlist, 32))

