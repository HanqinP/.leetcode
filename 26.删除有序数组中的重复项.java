/*
 * @lc app=leetcode.cn id=26 lang=java
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {
        int left = 0;
        int right = 1;
        for(int i=1;i<nums.length;i++){
            right = i;
            if(nums[right]!=nums[left]){
                left++;
                nums[left] = nums[right];
            }
        }
        
        return left+1;
    }
}
// @lc code=end

