__author__ = 'mohammadsafwat'

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, new_node):
        if self.leftChild == None:
            leftChild = BinaryTree(new_node)
            self.leftChild = leftChild
        else:
            leftChild = BinaryTree(new_node)
            leftChild.leftChild = self.leftChild
            self.leftChild = leftChild

    def insert_right(self, new_node):
        if self.rightChild == None:
            rightChild = BinaryTree(new_node)
            self.rightChild = rightChild
        else:
            rightChild = BinaryTree(new_node)
            rightChild.rightChild = self.rightChild
            self.rightChild = rightChild

    def get_right_child(self):
        return self.rightChild

    def get_left_child(self):
        return self.leftChild

    def set_root_value(self, obj):
        self.key = obj

    def get_root_value(self):
        return self.key

tree = BinaryTree('a')
tree.insert_left('b')
tree.insert_right('c')
tree.get_left_child().insert_right('d')
tree.get_right_child().insert_right('f')
tree.get_right_child().insert_left('e')

print(tree.get_root_value())
print(tree.get_left_child().get_root_value())
print(tree.get_right_child().get_root_value())
print(tree.get_left_child().get_right_child().get_root_value())
print(tree.get_right_child().get_right_child().get_root_value())
print(tree.get_right_child().get_left_child().get_root_value())
