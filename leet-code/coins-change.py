def coinChange(self, coins, amount):
  dp = [amount + 1] * (amount + 1)
  dp[0] = 0
  for i in range(0, amount + 1):
    for j in range(0, len(coins)):
      if coins[j] <= i:
        dp[i] = min(dp[i], 1 + dp[i - coins[j]])
        
  return -1 if dp[amount] > amount else dp[amount]

print(coinChange([1, 2, 5], 11))