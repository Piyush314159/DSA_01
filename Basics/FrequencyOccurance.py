class Solution:
    def frequencyCount(self, arr):
        n=len(arr)
        result=[0]*n
        for i in range(1,n+1):
            for num in arr:
                if i==num:
                    result[i-1]+=1
                    
        return result
    
a=Solution()
print(a.frequencyCount([2, 3, 2, 3, 5]))