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
            if(result=="") return "";
            result = getCommonPrefix(result, strs[i]);
            
        }
        return result;
    }

    public String getCommonPrefix(String s1, String s2){
        
        int len = s1.length()<s2.length()? s1.length():s2.length();

        for(int i = 0;i<len;i++){
            if(s1.charAt(i)!=s2.charAt(i) && i==0) return "";
            if(s1.charAt(i)!=s2.charAt(i) && i!=0){
                return s1.substring(0, i);
            }
        }
        

        return s1.length()>s2.length()?s2:s1;
    }


}



// @lc code=end

