class Solution:
    def maxSumSubarray(self, arr):
        sum_ = arr[0]
        max_sum = arr[0]
        start = 0
        ansStart = ansEnd = -1

        for i in range(1,len(arr)):
            if sum_<0: #if the sum(not including current element) is negative we are resetting the sum to current element
                sum_ = arr[i]
                start = i
            else: #if the sum is positive we add the current element to it
                sum_ += arr[i]
            
            if sum_>max_sum: #if the current sum is greater than previous max sum we are updating the max sum and the start and end index of subarray
                ansStart = start
                ansEnd = i
                max_sum = sum_

        return arr[ansStart:ansEnd+1]
    
a = Solution()
print(a.maxSumSubarray([-2,1,-3,4,-1,2,1,-5,4]))