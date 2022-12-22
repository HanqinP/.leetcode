#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0        
        for i,digit in enumerate(digits):
            num+=digit*10**(len(digits)-1-i)
        num+=1
        return [ int(x) for x in str(num)]
# @lc code=end

