package goldman;

import java.util.Arrays;


// Dynamic programming (buttom - up approach)
public class CoinChange {

    static int coinChange(int[] coins, int amount) {
        if (coins.length == 0 || (coins.length == 1 && coins[0] < amount)) {
            return -1;
        }

        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int i = 0; i <= amount; i++) {
            for(int j = 0; j < coins.length; j++) {
                if (coins[j] <= i) {
                    dp[i] = Math.min(dp[i], 1 + dp[i - coins[j]]);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }

    public static void main(String[] args) {
        int[] array = new int[] { 1, 2, 5 };
        int amount = 11;
        System.out.println(coinChange(array, amount)); //3
    }
}
