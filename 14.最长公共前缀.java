/*
 * @lc app=leetcode.cn id=14 lang=java
 *
 * [14] 最长公共前缀
 */

// @lc code=start
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String result = strs[0];

        if(strs.length==0) return "";

        if(strs.length==1) return strs[0];

        for(int i = 1; i<strs.length;i++){
            for(int j = 0;j<strs[i].length();j++){
                if(result.charAt(j) != strs[i].charAt(j) && j == 0){
                    return "";
                }else if(!result.contains(strs[i].substring(0, j+1))){
                    result = strs[i].substring(0,j);
                    break;
                }

                if(strs[i].length()==1) result = strs[i];

            }
        }
        return result;
    }
}



// @lc code=end

