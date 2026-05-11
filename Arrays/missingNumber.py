class Solution:
    def missingNumber1(self, arr):
        n = len(arr)

        for i in range(1,n+1):
            if i  not in arr:
                return i
            
    def missingNumber2(self, arr):
        n = len(arr)+1

        sn = (n*(n+1))//2

        s = 0
        for i in range(n-1):
            s+=arr[i]

        return sn-s
            
a = Solution()
print(a.missingNumber1([8, 2, 4, 5, 3, 7, 1]))
            
print(a.missingNumber2([8, 2, 4, 5, 3, 7, 1]))