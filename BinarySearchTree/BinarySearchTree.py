__author__ = 'mohammadsafwat'

import TreeNode


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __delitem__(self, key):
        self.delete(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self,k,v):
        self.put(k,v)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def _put(self, key, val, current_node):

        if key < current_node.key:
            # searching in left side
            if current_node.hasLeftChild():
                self._put(key, val, current_node.leftChild)
            else:
                current_node.leftChild = TreeNode(key, val, parent=current_node)
        elif key > current_node.key:
            # searching in right side
            if current_node.hasRightChild():
                self._put(key, val, current_node.rightChild)
            else:
                current_node.rightChild = TreeNode(key, val, parent=current_node)
        else:
            self._put(key, val, current_node)


    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

        self.size += 1


    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.leftChild)
        else:
            return self._get(key, current_node.rightChild)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)

            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')


    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild;
                else:
                    self.parent.rightChild = self.leftChild;
                self.leftChild.parent = self.parent;
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild;
                else:
                    self.parent.rightChild = self.rightChild;
                self.rightChild.parent = self.parent;


    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin();
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ


    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.paret.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else: #one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                               currentNode.leftChild.payload,
                                               currentNode.leftChild.leftChild,
                                               currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                               currentNode.rightChild.payload,
                                               currentNode.rightChild.leftChild,
                                               currentNode.rightChild.rightChild)



mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])