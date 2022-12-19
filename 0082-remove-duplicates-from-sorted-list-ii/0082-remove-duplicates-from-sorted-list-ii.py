# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Base case
        if head == None or head.next == None:
            return head
        
        dummy_array = ListNode(-101)
        dummy_array.next = head
        
        array_0 = dummy_array
        array_1 = head
        
        while array_1 != None:
            if array_1.next != None and array_1.val == array_1.next.val:
                while array_1.next != None and array_1.val == array_1.next.val:
                    array_1 = array_1.next
                array_0.next = array_1.next
            else:
                array_0 = array_1
            array_1 = array_1.next
                
        # return the linked list
        return dummy_array.next
    
        # time complexity: O(n)
        # space complexity: O(1)
