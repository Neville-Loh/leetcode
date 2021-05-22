"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Author: Neville
Date: 22 May 2021
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        current_node = head
        last_node = None
        while (current_node.next):
            next_node = current_node.next
            
            # set pointer
            current_node.next = last_node
            

            # go to next node
            last_node = current_node
            current_node = next_node
        
        current_node.next = last_node
        return current_node 

