class Solution:
    
    def mergeSort(self, arr, l, r):
        if l >= r:
            return
        
        mid = (l + r) // 2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)
        
        # merge inline
        left = arr[l:mid+1]
        right = arr[mid+1:r+1]
        
        i = 0 #left idx
        j=0 #right idx
        k = l #merge arr idx
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr
    
a = Solution()
print(a.mergeSort([5,3,8,2,1,6,7],0,6))

# mergeSort([5,3,8,2,1,6,7], 0, 6)  → mid=3
# ├── mergeSort([5,3,8,2,...], 0, 3)  → mid=1
# │   ├── mergeSort([5,3,...], 0, 1)  → mid=0
# │   │   ├── mergeSort([5,...], 0, 0)  → BASE CASE (returns)
# │   │   └── mergeSort([3,...], 1, 1)  → BASE CASE (returns)
# │   │   ✅ MERGE: [5,3] → [3,5]
# │   └── mergeSort([8,2,...], 2, 3)  → mid=2
# │       ├── mergeSort([8,...], 2, 2)  → BASE CASE (returns)
# │       └── mergeSort([2,...], 3, 3)  → BASE CASE (returns)
# │       ✅ MERGE: [8,2] → [2,8]
# │   ✅ MERGE: [3,5] + [2,8] → [2,3,5,8]
# └── mergeSort([...,1,6,7], 4, 6)  → mid=5
#     ├── mergeSort([1,6,...], 4, 5)  → mid=4
#     │   ├── mergeSort([1,...], 4, 4)  → BASE CASE (returns)
#     │   └── mergeSort([6,...], 5, 5)  → BASE CASE (returns)
#     │   ✅ MERGE: [1,6] → [1,6]
#     └── mergeSort([7,...], 6, 6)  → BASE CASE (returns)
#     ✅ MERGE: [1,6] + [7] → [1,6,7]
# ✅ FINAL MERGE: [2,3,5,8] + [1,6,7] → [1,2,3,5,6,7,8]