__author__ = 'mohammadsafwat'

from Stack import Stack

def convertIntegerToBinary(integer):
    remstack = Stack()

    while integer > 0:
        rem = integer % 2
        remstack.push(rem)
        integer //= 2

    binarry_string = ""
    while not remstack.isEmpty():
        binarry_string += str(remstack.pop())
    return binarry_string

print(convertIntegerToBinary(8))
print(convertIntegerToBinary(20))