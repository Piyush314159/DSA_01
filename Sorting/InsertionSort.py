class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1,n):
            key =arr[i] #hold the current element
            j = i-1
            while j>=0 and arr[j]>key:
                arr[j+1]= arr[j]# right shift
                j-=1
            arr[j+1] = key #insert 
        return arr

a = Solution()
print(a.insertionSort([5, 3, 8, 1, 2]))

