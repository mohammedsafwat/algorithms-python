__author__ = 'mohammadsafwat'

from Stack import Stack

def revstring(mystr):
    new_string = []
    original_string = list(mystr)
    while len(original_string) > 0:
        new_string.append(original_string.pop())
    return ''.join(new_string)

print(revstring("Apple"))

