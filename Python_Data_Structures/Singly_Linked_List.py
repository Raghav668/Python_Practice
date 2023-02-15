# creating class node

class node:
    def __init__(self, data):
        self.data = data  # node contains 2 fields data and reference link of next node. initially ref is none
        self.ref = None


# creating another class to create links to nodes and do add,deletion and traversal operation
class Linkedlist:
    def __init__(self):
        self.head = None  # initially head is none

    # Traversal operation - Going from starting node to ending node and printing the data of each node
    def print_traversal(self):
        if self.head == None:
            print("LINKED LIST IS EMPTY")
        else:
            n = self.head  # self.head as n
            while n is not None:  # till n is none
                print(n.data, "-->", end=" ")
                n = n.ref  # increment to next node till last node reference link (n) is none

    # add operation - add node at beginning of the linked list
    def add_at_begin(self, data):
        new_node = node(data)  # create new node obj from node class
        new_node.ref = self.head  # head address in new node address
        self.head = new_node  # new_node address in head

    # add node at the end of the linked list
    def add_at_end(self, data):
        new_node = node(data)  # create new node obj from node class
        if self.head is None:  # initially if linked list is empty and head is none
            self.head = new_node
            new_node.ref = self.head
        else:
            n = self.head
            while n.ref is not None:  # to go to last node (finding last node till the condition and assigning new
                # node address to last node ref)
                n = n.ref
            # comes out of the loop with last node ref address
            n.ref = new_node

    # adding node in between -> in 2 ways after node and before node
    # adding after node, the adding node can't be first node as it is after node
    def add_between_after_node(self, data, x):
        n = self.head
        while n is not None:  # find x
            if n.data == x:
                break  # if x and node is same it will come out of the loop
            else:
                n = n.ref  # loop till we find x
        if n is None:  # if x is not found (node is not present)
            print("Node is not present in the Linked list")
        else:  # if found
            new_node = node(data)  # creating node from node class
            new_node.ref = n.ref
            n.ref = new_node

    # adding before node
    def add_between_before_node(self, data, x):
        if self.head is None:
            print("Linked List empty")
        elif self.head.data == x:  # if we need to add node before the first node
            new_node = node(data)  # create new node obj from node class
            new_node.ref = self.head  # head address in new node address
            self.head = new_node  # new_node address in head
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:  # checking the node data with previous node ref address till it equals x
                break
            else:
                n = n.ref
        if n.ref is None:  # if x is not found (node is not present)
            print("Node is not present in the Linked list")
        else:  # if x matches we will change ref address with the previous node
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # when Linked lise is completely empty
    def Linked_list_empty(self, data):
        if self.head is None:
            new_node = node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            print("Linked list is not empty")

    # Deleting the node at the beginning of the linked list
    def delete_at_begin(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.ref  # second node address which is stored in first node ref, now stored in head

    # Deleting the node at the end of the Linked list
    def delete_at_end(self):  #
        if self.head is None:
            print("Linked list is empty")
        elif self.head.ref is None:  # if only one node is present in the Linked list
            self.head = None
        else:  # we need to find second last node and make second last node ref to NONE to remove last node
            n = self.head
            while n.ref.ref is not None:  # till we find the last node
                n = n.ref
            n.ref = None

    # delete the node from the middle of the linked list by using value
    def delete_at_middle(self, data):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.data == data:  # if the deleting node is first node, pointing head to second node
            self.head = self.head.ref
        else:  # Go to previous node of given node change previous node ref to given node ref
            n = self.head
            while n.ref is not None:  # till the last node ref is none
                if n.ref.data == data:
                    break
                else:
                    n = n.ref
            if n.ref is None:
                print("Node is not present")
            else:
                n.ref = n.ref.ref


LL = Linkedlist()
LL.add_at_begin(10)
# LL.add_at_begin(20)
# LL.add_at_end(30)
# LL.add_at_end(40)
# LL.add_at_begin(100)
# LL.add_between_after_node(60, 40)
# LL.add_between_before_node(25, 70)
# LL.Linked_list_empty(20)
# LL.delete_at_begin()
# LL.delete_at_end()
LL.delete_at_middle(10)
LL.print_traversal()
