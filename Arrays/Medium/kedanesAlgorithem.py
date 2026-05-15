class Solution:
    def maxSubarraySum(self, arr):
        sum_ = arr[0]
        max_sum = arr[0]

        for i in range(1, len(arr)):
            if sum_<0: # if the sum is negative, we can start a new subarray from the current element, as it will be greater than the sum of the previous subarray.
                sum_ = arr[i]
            else:   # if the sum is positive, we can continue adding the current element to the sum, as it will be greater than the current element alone.
                sum_+=arr[i]
            max_sum = max(max_sum, sum_) #we are keeping track of the maximum sum we have seen so far, and updating it if the current sum is greater than the maximum sum.
        return max_sum
    
a = Solution()
print(a.maxSubarraySum([-2,1,-3,4,-1,2,1,-5,4]))