class MyLinkedList(object):
    class Node(object):
        def __init__(self, val, next_node):
            self.val = val
            self.next = next_node
    
    def display(self):
        lst = []
        if self.length > 0:
            cur = self.head
            lst.append(cur.val)
            while cur.next is not None:
                cur = cur.next
                lst.append(cur.val)
        #print(lst)
                
        

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0
        
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < self.length:
            cur = self.head
            for i in range(index):
                cur = cur.next
            #self.display()
            return cur.val
        else:
            #self.display()
            return -1
            
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new = self.Node(val, self.head)
        self.head = new
        self.length += 1
        #self.display()
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        new = self.Node(val, None)
        if self.length == 0:
            self.head = new
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new
        self.length += 1
        #self.display()
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index <= self.length:
            cur = self.head
            if index == 0:
                self.addAtHead(val)
                return

            for i in range(index - 1):
                cur = cur.next
            if index == self.length:
                cur.next = self.Node(val, None)
            else:
                right = cur.next
                new = self.Node(val, right)

                cur.next = new
                new.next = right
            self.length += 1
        #self.display()
            
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < self.length:
            if index == 0:
                self.head = self.head.next
            else:
                cur = self.head
                for i in range(index - 1):
                    cur = cur.next
                deleted = cur.next
                right = cur.next.next
                cur.next = right
                deleted.next = None
                
            self.length -= 1
        #self.display()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)