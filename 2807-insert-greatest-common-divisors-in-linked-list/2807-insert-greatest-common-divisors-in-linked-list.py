# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
          curr=head
          while curr and curr.next:
            g=gcd(curr.val,curr.next.val)
            newnode=ListNode(0)
            newnode.val=g
            newnode.next=curr.next
            curr.next=newnode
            curr=newnode.next
          return head
            
