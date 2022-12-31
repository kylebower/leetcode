# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # base case: if list of length 0 or 1, return
        if not head or not head.next:
            return
        
        # reorder the list
        # find midpoint of list
        fast = head
        slow = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # break list
        prev.next = None
        
        # reorder list
        first = head
        second = reverse(slow)
        while first != None and second != None:
            next_first = first.next
            next_second = second.next
            first.next = second
            if next_first == None:
                second.next = next_second
            else:
                second.next = next_first
            
            first = next_first
            second = next_second
        
        # return
        return

# reverse order of list
def reverse(head):
    if head == None or head.next == None:
        return head
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
    