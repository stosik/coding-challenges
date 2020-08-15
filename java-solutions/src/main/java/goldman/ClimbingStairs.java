package goldman;

import java.util.HashMap;
import java.util.Map;

public class ClimbingStairs {

    private Map<Integer, Integer> memo = new HashMap<>();

    int climbWithDP(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }

        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i < n + 1; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }


    int climbWithRecursionAndMemo(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        if(memo.containsKey(n)) {
            return memo.get(n);
        } else {
            int result = climbWithRecursionAndMemo(n - 1) + climbWithRecursionAndMemo(n - 2);
            memo.put(n, result);
            return result;
        }
    }

    public static void main(String[] args) {
        int n = 3;
        ClimbingStairs climbingStairs = new ClimbingStairs();
        System.out.println(climbingStairs.climbWithRecursionAndMemo(n));
        System.out.println(climbingStairs.climbWithDP(n));
    }
}
