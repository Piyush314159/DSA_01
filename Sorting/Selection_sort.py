class Solution:
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i #tracking the index of the minimum in the list

            for j in range(i+1,n):
                if arr[j]<arr[min_idx]:
                    min_idx = j
            arr[i] , arr[min_idx] = arr[min_idx], arr[i] #swap
        
        return arr
    
a = Solution()
print(a.selectionSort([4, 3, 7, 9, 1]))  # [1, 3, 4, 7, 9]
