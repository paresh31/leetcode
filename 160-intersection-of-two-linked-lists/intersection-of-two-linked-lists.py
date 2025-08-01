# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lista = headA
        listb = headB
        while lista != listb:
            lista = lista.next if lista else headB
            listb = listb.next if listb else headA
        return listb