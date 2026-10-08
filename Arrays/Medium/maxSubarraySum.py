class Solution:
    def maxSumSubarray(self, arr):
        sum_ = arr[0]
        max_sum = arr[0]
        start = 0
        ansStart = ansEnd = -1

        for i in range(1,len(arr)):
            sum_ = max(arr[i], sum_ + arr[i])  #if the current element is greater than the sum of previous elements we will start a new subarray from the current element
            start = i if sum_ == arr[i] else start 
            
            if sum_>max_sum:        #if the current sum is greater than previous max sum we are updating the max sum and the start and end index of subarray
                ansStart = start
                ansEnd = i
                max_sum = sum_

        return arr[ansStart:ansEnd+1]
    
a = Solution()
print(a.maxSumSubarray([-2,1,-3,4,-1,2,1,-5,4]))