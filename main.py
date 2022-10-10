"""This is the main file"""


class Node:
    """This class is intended to represent a doubly linked list"""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """This class is for our functions """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size_ = 0
        # self.new_head = None
        # self.new_tail = None
        # self.new_size_ = 0

    def append(self, data):
        """this function is for adding an element to our main list"""

        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.size_ += 1
            return

        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.size_ += 1

    def begin(self):
        """This function returns elements from the beginning"""

        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def end(self):
        """This function returns elements from the end"""

        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev


    def index(self, data):
        start = self.head
        for i in range(self.size_):
            if start.data == data:
                return i
            start = start.next
        return None

    def emplace(self, index, data):
        """"This function emplace the element at the given index"""

        if index > self.size_ or index < 0:
            raise ValueError(f"Index out of range: {index}, size: {self.size_}")
        if index == self.size_:
            self.append(data)
            return
        if index == 0:
            self.head.prev = Node(data)
            self.head.prev.next = self.head
            self.head = self.head.prev
            self.size_ += 1
            return
        start = self.head
        for _ in range(index):
            start = start.next
        start.prev.next = Node(data)
        start.prev.next.prev = start.prev
        start.prev.next.next = start
        start.prev = start.prev.next
        self.size_ += 1
        return

    def remove(self, index):
        """This function removes element by index"""

        if index >= self.size_ or index < 0:
            raise ValueError(f"Index out of range: {index}, size: {self.size_}")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.size_ -= 1
            return
        if index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size_ -= 1
            return
        start = self.head
        for i in range(index):
            start = start.next
        start.prev.next, start.next.prev = start.next, start.prev
        self.size_ -= 1
        return

    def front(self):
        """This function access the first element."""
        print(self.head.data)

    def back(self):
        """This function access the last element."""
        print(self.tail.data)

    def push_back(self, data):
        """This function is for adding an element to the end"""

        new_node = Node(data)
        if self.size_ == 0 and not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size_ += 1

    def push_front(self, data):
        """This function inserts an element to the beginning"""

        new_node = Node(data)
        if self.size_ == 0 and not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size_ += 1

    def empty(self):
        """This function is for checkin if the list is empty"""

        if self.size_ == 0:
            print("The list is empty.")
        else:
            return

    def size(self):
        """This function returns the number of elements"""
        return self.size_

    def clear(self):
        """This function clears the contents"""

        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size_ -= 1
        self.size_ -= 1
        print("Content cleared. ")

    def insert(self, key, data):
        """"This function inserts the element after the given key"""

        if self.size_ == 0 and not self.head and not self.tail:
            print("Please add some data to your List.")
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node:
                if current_node.data == key:
                    if not current_node.next:
                        current_node.next = new_node
                        new_node.prev = current_node
                        self.tail = new_node
                    else:
                        next_node = current_node.next
                        current_node.next = new_node
                        new_node.prev = current_node
                        new_node.next = next_node
                        next_node.prev = new_node
                    self.size_ += 1
                    return
                else:
                    current_node = current_node.next

    # def remove(self, data):
    #     """This function removes elements satisfying specific criteria"""

    #     # when the list is empty
    #     if self.size_ == 0 and not self.head and not self.tail:
    #         print("No data to remove")
    #     # when the list contains 1 node
    #     elif self.size_ == 1:
    #         self.head = None
    #         self.tail = None
    #         self.size_ -= 1
    #     # when the list contains more than one node
    #     elif self.size_ > 1:
    #         current_node = self.head
    #         previous_node = None
    #         while current_node:
    #             # while the current node is not None
    #             if current_node.data == data:
    #                 # removing the head node
    #                 if not previous_node:
    #                     next_node = current_node.next
    #                     next_node.prev = None
    #                     current_node.next = None
    #                     del current_node
    #                     self.head = next_node
    #                 # removing the tail node
    #                 elif not current_node.next:
    #                     previous_node.next = None
    #                     current_node.prev = None
    #                     del current_node
    #                     self.tail = previous_node
    #                 # removing any random node but not the head and the tail nodes
    #                 else:
    #                     next_node = current_node.next
    #                     current_node.prev = None
    #                     current_node.next = None
    #                     del current_node
    #                     previous_node.next = next_node
    #                     next_node.prev = previous_node
    #                 self.size_ -= 1
    #                 return
    #             else:
    #                 previous_node = current_node
    #                 current_node = current_node.next

    def delete_node(self, node):
        """This function is for deleting duplicate elements"""

        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                if not cur.next:
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    self.head = nxt
                    return
            elif cur == node:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    return
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    return
            cur = cur.next

    def unique(self):
        """"This function removes duplicate elements"""

        cur = self.head
        seen = {}
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt
                
    def merge(self, first, second):
        """This function merges two sorted lists"""
        
        if first is None: 
            return second  
        if second is None: 
            return first 
        if first.data < second.data: 
            first.next = self.merge(first.next, second) 
            first.next.prev = first 
            first.prev = None   
            return first 
        else: 
            second.next = self.merge(first, second.next) 
            second.next.prev = second 
            second.prev = None
            return second 
            
    def mergeSort(self, tempHead):
        """Function to do merge sort"""
        
        if tempHead is None:  
            return tempHead 
        if tempHead.next is None: 
            return tempHead
        second = self.split(tempHead) 
        tempHead = self.mergeSort(tempHead) 
        second = self.mergeSort(second)
        return self.merge(tempHead, second) 

    def split(self, tempHead):
        """This function splits a doubly linked list into two half-sized dlls"""
        
        fast = slow =  tempHead 
        while(True): 
            if fast.next is None: 
                break
            if fast.next.next is None: 
                break
            fast = fast.next.next 
            slow = slow.next
        temp = slow.next
        slow.next = None
        return temp 
        
    def printList(self, node):
        """This function prints merged list"""
        temp = node 
        while(node is not None): 
            print (node.data,end=" ") 
            temp = node 
            node = node.next
        print ("\n") 


    def print_list(self):
        """This function prints our list"""

        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next


if __name__ == "__main__":
    myList = DoublyLinkedList()
    myList.append(15)
    myList.append(21)
    myList.append(3)
    myList.append(12)
    myList.append(321)


    print("The original list:")
    myList.print_list()

    print("Size:", myList.size())
    print("The first element of the list is:", end=' ')
    myList.front()

    print("The last element of the list is:", end=' ')
    myList.back()

    print("returns the list from the beginning:")
    myList.begin()

    print("returns the list from the end:")
    myList.end()

    myList.insert(21, 4)
    myList.insert(321, 17)
    myList.remove(0)
    myList.emplace(3, 3)

    print("Changed list:")
    myList.print_list()
    print("Size:", myList.size())

    print("Unique elements:")
    myList.unique()
    myList.print_list()
    print("\n")
    
    myList.head = myList.mergeSort(myList.head)    
    print ("List after sorting") 
    myList.printList(myList.head)

    myList.empty()

    myList.clear()
    print("Size:", myList.size())
    myList.empty()
