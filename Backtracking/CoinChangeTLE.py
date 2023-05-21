# Works but too slow, use DP
class Solution:
    def coinChange(self, coins, amount) -> int:
        res = []
        subset = []
        def dfs(i,amount):
            if amount == 0:
                res.append(len(subset))
                return
            if amount < 0 or i>=len(coins):
                return
            subset.append(coins[i])
            dfs(i,amount-coins[i])
            subset.pop()
            dfs(i+1,amount)
        dfs(0,amount)
        sol = res[0] if res else -1
        for nc in res:
            if nc < sol:
                sol = nc
        return sol
