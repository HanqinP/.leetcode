/*
 * @lc app=leetcode.cn id=66 lang=java
 *
 * [66] 加一
 */

// @lc code=start
class Solution {
    public int[] plusOne(int[] digits) {

        int carry = 1;
        for (int i = digits.length - 1; i >= 0; i--) {
            digits[i] = (digits[i] + carry) % 10;
            carry = digits[i] == 0 && carry != 0 ? 1 : 0;

        }

        if (digits[0] == 0) {
            int[] res = new int[digits.length + 1];
            res[0] = 1;
            return res;
        }

        return digits;
    }
}
// @lc code=end
