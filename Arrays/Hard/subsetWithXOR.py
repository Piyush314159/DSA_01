'''
Subset XOR Count - Bitmask Enumeration:
    * Enumerate all subsets using bitmask → O(2^N)
    * For each subset, check N elements → O(N)
    * Total Time → O(2^N × N)
    * Space → O(1)
'''
class Solution:
    def subsetXOR(self, arr, N, K): 
        count = 0
        for i in range(2**N):           # Loop through all possible subsets (2^N)
            xor = 0                     #fresh xor value for each subset
            for j in range(N):          # Check if the j-th element is included in the current subset (i)
                if i & (1 << j):        # If the j-th bit of i is set, include arr[j] in the XOR calculation
                    '''
                    (1 << j) creates a number with only the j-th bit set (e.g., if j=2, it creates 00000100 in binary).
                    i & (1 << j) checks if the j-th bit of i is set.
                    If the result is non-zero, it means the j-th bit of i is set, and we include arr[j] in the XOR calculation.
                    '''
                    xor ^= arr[j]
            if xor == K:
                count += 1
        return count
    
a = Solution()
print(a.subsetXOR([1, 3, 4, 5], 4, 4))
    
