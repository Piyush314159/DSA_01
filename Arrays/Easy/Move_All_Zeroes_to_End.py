class Solution:
    def pushZerosToEnd(self, arr):

        n = len(arr)

        j = -1

        for i in range(n):
            if arr[i]==0:
                j=i
                break #finding first zero idx
        
        if j==-1:
            return arr #no zero found

        for i in range(j+1,n):
            if arr[i]!=0:
                arr[i], arr[j] = arr[j], arr[i]
                j+=1
        
        return arr

a = Solution()
print(a.pushZerosToEnd([1, 2, 0, 4, 3, 0, 5, 0, 6, 4 ,0, 1]))