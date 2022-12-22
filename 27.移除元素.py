#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:return 0
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left+=1

            pass
        return left
# @lc code=end

