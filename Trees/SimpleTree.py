__author__ = 'mohammadsafwat'

myTree = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]

def binary_tree(r):
    return [r, [], []]

def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

r = binary_tree(3)
insert_left(r, 4)
insert_left(r, 5)

insert_right(r, 6)
insert_right(r, 7)

left_child = get_left_child(r)
#print(left_child)

right_child = get_right_child(r)
#print(right_child)
#print(r)
set_root_val(left_child, 9)
insert_left(left_child, 11)
#print(r)

new_tree = binary_tree('a')
insert_left(new_tree, 'b')
insert_right(new_tree, 'c')
insert_right(get_left_child(new_tree), 'd')
insert_right(get_right_child(new_tree), 'f')
insert_left(get_right_child(new_tree), 'e')
print(new_tree)