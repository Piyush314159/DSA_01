# so first we will calculate the prefix sum of the array and store it in a hashmap with the index as value.
# then we will check if the prefix sum at current index - k is present in the hashmap or not.
# if it is present then we will calculate the length of the subarray and update the max_len variable.

class Solution:
    def longestSubarray(self, arr, k):  
        n = len(arr)
        max_len = 0
        prefix = 0
        hashmap = {0:-1}

        for i in range(n):
            prefix+=arr[i]

            if prefix-k in hashmap:
                max_len = max(max_len,i-hashmap[prefix-k])
            
            if prefix not in hashmap:
                hashmap[prefix]=i

        return max_len

    
a = Solution()
print(a.longestSubarray( [10, 5, 2, 7, 1, -10, 7, 8, 10, -10], 15))


# prefix[i] - prefix[j] = k , where j < i and j-->starting index of the subarray and i-->ending index of the subarray

# at some earlier index j, the prefix sum was prefix[j] and at current index i,
# the prefix sum is prefix[i]. 
# If we want to find a subarray that sums to k, 
# then we can check if there exists an index j such that prefix[i] - prefix[j] = k.
# This can be rearranged to prefix[j] = prefix[i] - k.
# prefix[i] - prefix[j] = k
