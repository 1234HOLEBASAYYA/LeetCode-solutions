# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        pre=None
        while slow:
            nex=slow.next
            slow.next=pre
            pre=slow
            slow=nex

        f=head
        s=pre
        ans=0
        while s:
            ans=max(ans,f.val+s.val)
            f=f.next
            s=s.next
        return ans