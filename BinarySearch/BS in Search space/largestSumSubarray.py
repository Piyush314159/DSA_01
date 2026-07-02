class Solution():
    def maxSumWithK(self, a, n, k):
        if len(a) == 0:
            return -1
        
        P = [0] * (n+1)
        for i in range(1,n+1):
            P[i] = P[i-1] + a[i-1]          # P ------> list of cumulative sums of arr a
            
        minP = P[0]                         # minimum prefix sum of the first k elements of P
        best = float("-inf")                # best ------> maximum sum of subarray of length k
        for j in range(k, n+1):
            best = max(best, P[j] - minP)   # finding best max sum by maximizing P[j] - minP by minimizing minP
            minP = min(minP, P[j - k + 1])  # minimizing minP by current minP and the prefix sum of the subarray of length k ending at index j
        return best

a = Solution()
print(a.maxSumWithK([1, -2, 2, -3], 4, 2))