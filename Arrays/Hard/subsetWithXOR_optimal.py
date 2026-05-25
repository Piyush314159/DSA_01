class Solution:
    def subsetXOR(self, arr, N, K):
        dp = {0: 1}                                         #{xor_value: count_of_subsets_with_that_xor}--> initially we are setting xor= 0 to ssubset count as 1 (empty subset).
        for a in arr:
            new_dp = {}
            for x in dp:                                    # keys of dp as x
                # skip a
                new_dp[x] = new_dp.get(x, 0) + dp[x]        # if we skip a, the count of subsets with xor value x remains the same as in dp, so we add dp[x] to new_dp[x].
                # include a
                new_dp[x ^ a] = new_dp.get(x ^ a, 0) + dp[x]# if we include a, the new xor value becomes x ^ a, and the count of subsets with this new xor value increases by dp[x] (the count of subsets that had xor value x before including a).
            dp = new_dp
            print(dp)
        return dp.get(K, 0)

a = Solution()
print(a.subsetXOR([6, 9, 4, 2], 4, 6))