class Solution:
    def KthMissingElement(self, arr, k):
        missing_count = 0
        for i in range(len(arr) - 1):
            gap = arr[i+1] - arr[i] - 1
            if missing_count + gap >= k:            # if the missing count + gap is greater than or equal to k, it means that the kth missing number is in the gap between arr[i] and arr[i+1]
                return arr[i] + (k - missing_count)
            missing_count += gap
        return -1  # if we reach here, it means that the kth missing number is not in the array, so we return -1

a = Solution()
print(a.KthMissingElement([1, 3, 4, 5, 7], 2))                