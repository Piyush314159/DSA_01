class Solution:
    def recursiveBubbleSort(self, arr, i, n):

        if n == 1:
            return arr

        if i == n-1:
            return self.recursiveBubbleSort(arr, 0, n-1)

        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

        return self.recursiveBubbleSort(arr, i+1, n)


arr1 = [5, 3, 2, 8, 1]
a = Solution()
print(a.recursiveBubbleSort(arr1, 0, len(arr1)))