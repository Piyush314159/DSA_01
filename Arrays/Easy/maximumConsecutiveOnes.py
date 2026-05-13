class Solution:
    def maxOnes(self, arr, k):
        n = len(arr)
        start = 0
        zeros = 0
        max_len = 0

        for end in range(n):
            if arr[end]==0 :
                zeros+=1

            if zeros > k:           # invalid → shrink by one
                if arr[start] == 0: #for reduce the zero if start itself is zero when we are moving forward start by one 
                    zeros -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
    
a = Solution()
print(a.maxOnes([1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],2))