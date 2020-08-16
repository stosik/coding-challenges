package goldman;

public class LongestCommonSubstring {

    static int longestCommonSubstring(char[] first, char[] second) {
        int[][] dp = new int[first.length + 1][second.length + 1];
        int result = 0;

        for (int i = 0; i <= first.length; i++) {
            for (int j = 0; j <= second.length; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 0;
                } else if (first[i - 1] == second[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    result = Math.max(result, dp[i][j]);
                } else {
                    dp[i][j] = 0;
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        String X = "OldSite:GeeksforGeeks.org";
        String Y = "NewSite:GeeksQuiz.com";

        System.out.println(longestCommonSubstring(X.toCharArray(), Y.toCharArray()));
    }
}
