#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lengtha = len(a)-1
        lengthb = len(b)-1
        carry = 0
        result = ''

        while lengtha>=0 or lengthb>=0:
            sum = carry
            if lengtha>=0:
                sum+=int(a[lengtha])
                lengtha-=1
            if lengthb>=0:
                sum+=int(b[lengthb])
                lengthb-=1

            carry = 1 if sum>=2 else 0
            result+=str(sum%2)
            
        if carry>0:result+='1'
        return result[::-1]

# @lc code=end

