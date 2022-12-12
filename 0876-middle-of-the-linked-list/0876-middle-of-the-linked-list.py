# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle_array = head
        end_array = head
        while end_array != None and end_array.next != None:
            middle_array = middle_array.next
            end_array = end_array.next.next
        return middle_array
        