#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            '(':')',
            '[':']',
            '{':'}'
        }

        stack = []

        for char in s:
            if char not in map and len(stack) == 0:
                return False
            elif char not in map and map[stack.pop()] != char:
                return False
            elif char in map:
                stack.append(char)
        
        return len(stack) == 0



# @lc code=end


