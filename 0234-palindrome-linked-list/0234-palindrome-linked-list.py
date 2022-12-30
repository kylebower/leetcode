# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # base case: if list of length 0 or 1, return True
        if not head or not head.next:
            return True

        # define fast and slow pointers
        fast = head
        slow = head

        # traverse list until slow is in middle and fast is at end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half of linked list
        L = head
        R = reverse(slow)
        
        # check if list is a palindrome
        # i.e., first half equals second half
        while R:
            if L.val != R.val:
                return False
            L = L.next
            R = R.next

        # return true if it is a palindrome or false otherwise
        return True
    
def reverse(head):
    # base case
    if not head or not head.next:
        return head

    # reverse
    pre = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre
        
        