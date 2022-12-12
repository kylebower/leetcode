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
        array = []
        while reached_end_of_list == 0:
            array.append(head_curr)
            n +=1
            if head_curr.next == None:
                reached_end_of_list = 1
            else:
                head_curr = head_curr.next        
        return array[floor(n/2)]
        