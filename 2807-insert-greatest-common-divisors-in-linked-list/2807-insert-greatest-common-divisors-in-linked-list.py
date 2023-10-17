# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        next_list = head.next
        
        while next_list:
            new_node = ListNode(math.gcd(head.val, next_list.val))
            
            head.next = new_node
            new_node.next = next_list
            
            head = next_list
            next_list = next_list.next
        
        return dummy