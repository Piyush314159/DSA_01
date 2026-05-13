class Solution:
    def leftRotate(self, arr, d):
        n = len(arr)
        if d>=n:
            return arr

        def reverse(l,r):
            while l<r:
                arr[l], arr[r] =arr[r], arr[l]
                l+=1
                r-=1
        reverse(0,d-1)
        reverse(d,n-1)
        reverse(0,n-1)
        return arr

a = Solution()
print(a.leftRotate( [-1, -2, -3, 4, 5, 6, 7], d = 2))

