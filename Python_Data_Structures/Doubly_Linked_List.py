# creating class node

class node:
    def __init__(self, data):
        self.data = data  # node contains 3 fields data and reference link of next node and previous node. initially
        # ref is none
        self.nref = None
        self.pref = None


# creating another class to create links to nodes and do add,deletion and traversal operation
class doublyLinkedlist:
    def __init__(self):
        self.head = None  # initially head is none

    # Traversal operation - Going from forward and backward node and printing the data of each node
    def print_traversal_forward(self):
        if self.head is None:
            print("LINKED LIST IS EMPTY")
        else:
            n = self.head  # self.head as n
            while n is not None:  # till n is none #if we do n.nref is not none then last node will not print
                print(n.data, "-->", end=" ")
                n = n.nref  # increment to next node till last node reference link (n) is none

    def print_traversal_backward(self):  # we will go till last node and print data from backwards
        if self.head is None:
            print("LINKED LIST IS EMPTY")
        else:
            n = self.head  # self.head as n
            while n.nref is not None:  # till n is none
                n = n.nref  # increment to next node till last node reference link (n) is none
            while n is not None:  # if we do n.pref is not none then first node will not print
                print(n.data, "-->", end=" ")
                n = n.pref

    # when Linked lise is completely empty
    def Linked_list_empty(self, data):
        if self.head is None:
            new_node = node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

    # add operation - add node at beginning of the linked list
    def add_at_begin(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # add node at the end of the linked list
    def add_at_end(self, data):
        new_node = node(data)  # create new node obj from node class
        if self.head is None:  # initially if linked list is empty and head is none
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:  # to go to last node (finding last node till the condition and assigning new
                # node address to last node ref)
                n = n.nref
            # comes out of the loop with last node ref address
            n.nref = new_node
            new_node.pref = n

    # add node after the given node value
    def add_node_after(self, data, x):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                else:
                    n = n.nref
            if n is None:
                print("Node is not present in the Linked list")
            else:
                new_node = node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:  # if last node nref is not none
                    n.nref.pref = new_node
                n.nref = new_node

    # add node before the given node value
    def add_node_before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                else:
                    n = n.nref
            if n is None:
                print("Node is not present in the Linked list")
            else:
                new_node = node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:  # if we are not adding before first node
                    n.pref.nref = new_node
                else:
                    self.head = new_node  # if we are adding before first node head also need to be changed
                n.pref = new_node

    # Delete node at beginning of the linked list
    def delete_at_begin(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.nref is None:
            self.head = None
        else:
            self.head = self.head.nref  # after this first will be deleted
            self.head.pref = None  # making new first node pref as none

    #Delete node at end of the Linked list
    def delete_at_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    #Deleting by given data
    def delete_by_value(self,x):
        if self.head is None: # if Linked list is completely empty
            print("Linked list is empty")
        elif self.head.nref is None:  # if only one node is present in the Linked list
            if self.head.data == x:
                self.head = None
            else:
                print("node is not present in the Linked list")
        elif self.head.data == x: # if the deleting node is first node in the Linked list
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head # if we need to delete in the middle of the Linke dlist
        while n.nref is not None:
            if n.data == x:
                break
            else:
                n = n.nref
        if n.nref is not None: # if break statement is executed
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else: # if not we are in the last node of the linked list
            if n.data == x: # if deleting node is last node
                n.pref.nref = None
            else:
                print("node is not present in the Linked list")









dll = doublyLinkedlist()
# dll.Linked_list_empty(10)
dll.add_at_begin(20)
dll.add_at_begin(30)
dll.add_at_end(40)
dll.add_at_end(50)
dll.add_node_after(45, 40)
dll.add_node_before(25, 30)
dll.add_node_before(28, 30)
#dll.delete_at_begin()
#dll.delete_at_begin()
#dll.delete_at_end()
#dll.delete_at_end()
dll.delete_by_value(28)
dll.delete_by_value(40)
dll.print_traversal_forward()

# dll.print_traversal_backward()
