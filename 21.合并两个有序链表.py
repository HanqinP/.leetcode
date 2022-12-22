#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 or not list2:
            return list1 or list2

        if list1.val >= list2.val:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1 

# @lc code=end

