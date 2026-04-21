class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        pointer = 0 #points the position where the next nonzero will go

        for i in range(n): #making the nonzero list part
            if arr[i]!=0:
                arr[pointer],arr[i] = arr[i],arr[pointer]
                pointer+=1
        return arr

a = Solution()
print(a.pushZerosToEnd( [1, 2, 0, 4, 3, 0, 5, 0]))
