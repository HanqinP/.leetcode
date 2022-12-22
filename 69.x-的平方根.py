#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left<=right:
            mid = (left+right)//2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid*mid < x:
                left = mid+1
            else:
                right = mid-1

        return left
# @lc code=end

