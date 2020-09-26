"""




"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        
        last_node = None
        current_node = head
        while ( current_node.next != None ):
            if last_node != None and current_node.val == last_node.val:
                last_node.next = current_node.next
            else:
                last_node = current_node
            current_node = current_node.next
        
        if current_node.val == last_node.val:
            last_node.next = None

        return head
