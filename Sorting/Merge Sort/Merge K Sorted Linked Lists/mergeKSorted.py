# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for index in range(0, len(lists), 2):
                l1 = lists[index]
                l2 = lists[index + 1] if index + 1 < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))

            lists = mergedLists
        
        return lists[0]

    def mergeList(self, list1, list2):
        if list1 == None and list2 == None:
            return 
        
        new_list = ListNode(0)
        pointer = new_list
        pointer1, pointer2 = list1, list2

        while pointer1 and pointer2:
            if pointer1.val < pointer2.val: 
                pointer.next = pointer1
                pointer1 = pointer1.next
            else:
                pointer.next = pointer2
                pointer2 = pointer2.next
            
            pointer = pointer.next
        
        if pointer1:
            pointer.next = pointer1
        
        if pointer2:
            pointer.next = pointer2

        return new_list.next