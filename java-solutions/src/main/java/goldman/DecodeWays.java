package goldman;

public class DecodeWays {

    static int decodeWays(String message) {
        int[] dp = new int[message.length() + 1];
        dp[0] = 1;
        dp[1] = message.charAt(0) == '0' ? 0 : 1;
        for (int i = 2; i <= message.length(); i++) {
            int oneDigit = Integer.parseInt(message.substring(i - 1, i));
            int twoDigit = Integer.parseInt(message.substring(i - 2, i));

            if (oneDigit >= 1) {
                dp[i] += dp[i - 1];
            }

            if (twoDigit >= 10 && twoDigit <= 26) {
                dp[i] += dp[i - 1];
            }
        }

        return dp[message.length()];
    }

    public static void main(String[] args) {
        String message = "12";
        System.out.println(decodeWays(message));
    }
}
