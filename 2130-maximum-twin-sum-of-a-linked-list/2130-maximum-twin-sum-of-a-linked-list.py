# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=head
        slow=head
        while fast and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        pre=None
        while slow:
            nx=slow.next
            slow.next=pre
            pre=slow
            slow=nx

        f=head
        s=pre
        ans=0
        while s!=None:
            ans=max(ans,f.val+s.val)
            f=f.next
            s=s.next
        return ans


        