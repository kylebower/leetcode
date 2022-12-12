# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        reached_end_of_list = 0
        head_curr = head
        while reached_end_of_list == 0:
            n +=1
            if head_curr.next == None:
                reached_end_of_list = 1
            else:
                head_curr = head_curr.next
        middle_node = head
        for i in range(floor(n/2)):
            middle_node = middle_node.next
        return middle_node
        