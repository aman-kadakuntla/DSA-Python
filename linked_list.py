'''
Implementation of single linked list
'''

class Node:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList:

    def __init__(self):
        self.head=Node()

    def insert_at_end(self,val):
        if self.head.data is None:
            self.head.data = val
        else:
            new_node=Node()
            new_node.data=val
            new_node.next=None
            pointer_node = self.head
            while pointer_node.next is not None:
                pointer_node=pointer_node.next
            pointer_node.next=new_node

    def insert_at_begining(self,val):
        if self.head.data is None:
            self.head.data=val
        else:
            new_node=Node()
            new_node.data=val
            new_node.next=self.head
            self.head=new_node
    
    def insert_at_index(self,index,val):
        if self.head.data is None:
            self.head.data=val
        else:
            pos=1
            new_node=Node()
            new_node.data=val
            pointer_node=self.head
            while True:
                if pos is index:
                    next_node = pointer_node.next
                    pointer_node.next=new_node
                    new_node.next=next_node
                    break
                pointer_node=pointer_node.next
                pos=pos+1
    
    def delete_at_index(self,index):
        if self.head.next is None:
            self.head = None
        else:
            pos=1
            pointer_node=self.head
            while True:
                if pos is index:
                    delete_node = pointer_node.next
                    pointer_node.next = delete_node.next
                    break
                pointer_node=pointer_node.next
                pos=pos+1

    def delete_value(self,val):
        if self.head.data is val:
           self.head = None
        else:
           prev_node = self.head
           current_node = self.head.next
           while True:
               if current_node.data is val:
                   prev_node.next = current_node.next
                   break
               prev_node = current_node
               current_node=current_node.next    

    def print_values(self): # print all the values from start to end
        values=[]
        pointer_node = self.head
        while pointer_node.next is not None:
            values.append(pointer_node.data)
            pointer_node=pointer_node.next
            if pointer_node.next is None:
                values.append(pointer_node.data)
        return values
    
    def length(self):
        return len(self.print_values())
    
linked_list = LinkedList()

linked_list.insert_at_begining(1)
linked_list.insert_at_begining(3)
linked_list.insert_at_begining(8)
linked_list.insert_at_begining(4)
linked_list.insert_at_end(9)
linked_list.insert_at_end(10)

print(linked_list.print_values())

linked_list.delete_value(8)

print(linked_list.print_values())

