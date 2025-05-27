class ListNode:
    def __init__(self, val, next = None) -> None:
       self.val = val
       self.next = None
    
class MyLinkedList:
    def __init__(self, head):
        self.head = None
    
    def get(self, index):
        if self.head is None or index == -1:
            return -1
        
        count = 0
        current = self.head

        while current:
            if count == index:
                return current.val

            count += 1
            current = current.next
        
        return -1
    
    def addAtHead(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
    
    def addAtTail(self, val):
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        
        while current.next:
            current = current.next
        
        current.next = new_node
        current = current.next
    
    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return
        
        new_node = ListNode(val)
        count = 0
        current = self.head

        while current:
            if count == index - 1:
                new_node.next = current.next
                current.next = new_node
                return
            
            count += 1
            current = current.next
        
        if index == count:
            self.addAtTail(val)
            return
        

    def deleAtIndex(self, index):
        if index == 0 and self.head:
            self.head = self.head.next
            return 
        
        count = 0
        current = self.head

        while current and current.next:
            if count == index - 1:
                current.next = current.next.next()
                return 
            
            current = current.next
            count += 1