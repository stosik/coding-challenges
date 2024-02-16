package leetcode;

class LeetCode5LongestPalindromicSubstring {
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) return "";

        int start = 0;
        int end = 0;

        for(int i = 0; i < s.length(); i++) {

            // case when "racecar" (so expand from same point)
            int len1 = expandFromMiddle(s, i, i);

            // case when "abba" (so expand from two different points)
            int len2 = expandFromMiddle(s, i, i + 1);

            int len = Math.max(len1, len2);
            if(len > end - start) {
                start = i - ((len - 1) / 2);
                end = i + (len / 2);
            }
        }
        return s.substring(start, end + 1);
    }

    private int expandFromMiddle(String s, int left, int right) {
        if(s == null || s.length() < 1) return 0;

        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        return right - left - 1;
    }
}