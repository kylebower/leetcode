# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        head_curr = head
        array = []
        array.append(head)
        while head_curr.next != None:
            n += 1
            head_curr = head_curr.next
            array.append(head_curr)
        return array[floor(n/2)]
        