# No need of creating extra class for extra node creating new object means creating new node
class BST:
    def __init__(self, key):
        self.key = key  # data/key of node
        self.lchild = None  # left subtree child
        self.rchild = None  # Right subtree child

    # insertion operation
    def insert(self, data):
        if self.key is None:  # self means root
            print("Tree is empty")  # if tree is empty
        elif self.key == data:
            return  # if there is any duplicate values
        if data < self.key:  # if duplicate values need to be placed in left subtree then need to mention <=
            if self.lchild:  # if there is already left subtree
                self.lchild.insert(data)  # recursion until we know left subtree is empty
            else:
                self.lchild = BST(data)  # After we know, if left subtree is empty we create new node by creating obj
        else:  # if duplicate values need to be placed in right subtree then need to mention >=
            if self.rchild:  # if there is already left subtree
                self.rchild.insert(data)  # recursion until we know left subtree is empty
            else:
                self.rchild = BST(data)  # After we know, if left subtree is empty we create new node by creating obj

    # Search operation
    def search(self, data):
        if self.key == data:  # if root node matches
            print("node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print(" Node is not present")  # if left subtree is empty
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print(" Node is not present")  # if right subtree is empty

    # Pre-order Traversal Algorithm
    def pre_order_traversal(self):  # Root, left node, Right node
        if self.key is None:
            print("Tree is empty")
            return
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.pre_order_traversal()  # Recursion
        if self.rchild:
            self.rchild.pre_order_traversal()

    # In-order Traversal
    def In_order_traversal(self):  # left node, root node, right node
        if self.key is None:
            print("Tree is empty")
            return
        if self.lchild:
            self.lchild.In_order_traversal()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.In_order_traversal()

    # Post-order Traversal
    def post_order_traversal(self):  # left node, right node, root node
        if self.key is None:
            print("Tree is empty")
            return
        if self.lchild:
            self.lchild.post_order_traversal()
        if self.rchild:
            self.rchild.post_order_traversal()
        print(self.key, end=" ")

    # Deletion operation , check video number 48 in Amulya Academy YouTube channel
    def delete(self, data, curr):  # curr = root.key
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print(" Node is not present")  # if left subtree is empty
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print(" Node is not present")  # if right subtree is empty
        else:
            if self.lchild is None:  # deleting node with 0 or 1 child
                temp = self.rchild
                if data == curr:  # deleting rootnode, this is when root node having one child that is on the right
                    # and left child is none
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:  # deleting rootnode, this is when root node having one child that is on the left
                    # and right child is none
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            node = self.rchild  # node having 2 child, Replacing deleting node with the smallest value of right subtree
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, curr)
        return self

    # Minimum and maximum of Binary search tree
    def Min_node(self):
        current = self  # storing root node in current
        while current.lchild:
            current = current.lchild  # till we find left child is empty
        print("Minimum node", current.key)

    def Max_node(self):
        current = self  # storing root node in current
        while current.rchild:
            current = current.rchild  # till we find right child is empty
        print("Maximum node", current.key)


# creating External function to know the count of nodes in a tree
def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)


rootnode = BST(10)  # creating new obj means creating new node and self means root node because root node goes in the
# place of self
# List = [23, 15, 2, 1, 3, 4, 5, 30, 32, 92]
List = [6, 3, 1, 6, 98, 3, 7]
# List = [10, 11, 12]
for i in List:
    rootnode.insert(i)
# rootnode.search(32)
# print("pre order Traversal", end=" ")
# rootnode.pre_order_traversal()
print()
# print("In order Traversal", end=" ")
# rootnode.In_order_traversal()
# print("post order Traversal")
# rootnode.post_order_traversal()
rootnode.pre_order_traversal()
if count(rootnode) > 1:  # Root node with 0 children
    print("Total node before deletion", count(rootnode))
    rootnode.delete(10, rootnode.key)  # rootnode key is to identify whether we are deleting root node or not
    print("Total node After deletion", count(rootnode))

else:
    print("cannot perform deletion operation as there is no children")
rootnode.pre_order_traversal()
rootnode.Min_node()
rootnode.Max_node()
