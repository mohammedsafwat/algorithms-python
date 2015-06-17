__author__ = 'mohammadsafwat'

from Stack import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber //= base

    newString = ""

    while not remstack.isEmpty():
        newString += digits[remstack.pop()]

    return newString

print(baseConverter(20, 2))
print(baseConverter(25, 8))
print(baseConverter(30, 16))