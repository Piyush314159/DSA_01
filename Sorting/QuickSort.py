class Solution:
    def quickSort(self, arr, low, high):
        if low>=high:
            return
        pi = self.partition(arr,low,high) #getting the place where the pivot is
        self.quickSort(arr,low,pi-1) #left recursion
        self.quickSort(arr,pi+1,high) #right recursion
        return arr

    def partition(self, arr, low, high):
        pivot = arr[high] #last element
        i = low-1 #something that tracks "up to where have I placed small elements" → this is i, and it starts at low - 1

        for j in range(low,high):
            if arr[j]<=pivot:
                i+=1 #increasing the boundary
                arr[i], arr[j] = arr[j], arr[i] #placing the samller element at i 

        arr[i+1], arr[high] = arr[high] , arr[i+1] ## after loop, place pivot
        return i+1 #place of the pivot
    

a = Solution()
print(a.quickSort([8,3,1,2,9,5],0,5))