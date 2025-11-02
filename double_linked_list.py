'''
Implementation of Double Linked List
'''
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


class DoubleLinkedList:

    def __init__(self):
        self.head = Node()
    
    def insert_at_end(self,val):
        if self.head.data is None:
            self.head.data = val
        else:
            pointer = self.head
            new_node = Node()
            new_node.data = val
            while True:
                if pointer.right is None:
                    pointer.right = new_node
                    new_node.left = pointer
                    break
                pointer = pointer.right
    
    def insert_at_begining(self,val):
        if self.head.data is None:
            self.head.data = val
        else:
            new_node = Node()
            new_node.data = val
            new_node.right = self.head
            self.head.left = new_node
            self.head = new_node
    
    def delete_value(self,val):
        #todo
        pass
    
    def get_values(self):
        values = []
        pointer = self.head
        while self.head.right is not None:
            values.append(self.head.data)
            self.head = self.head.right
        values.append(self.head.data)
        self.head = pointer
        return values
    

d_linked_list = DoubleLinkedList()

d_linked_list.insert_at_end(2)
d_linked_list.insert_at_end(4)
d_linked_list.insert_at_end(5)

print(d_linked_list.get_values())


d_linked_list.insert_at_begining(10)


print(d_linked_list.get_values())