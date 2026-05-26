class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        s = 0
        s2 = 0
        for el in arr:
            s+=el
            s2+=(el**2)

        sn = 0
        sn2 = 0
        for i in range(1,n+1):
            sn+=i
            sn2+=(i**2)

        val1 = sn - s  # x-y
        val2 = sn2 - s2 #x^2 -y^2
        val3 = val2//val1 #x+y

        x = (val1+val3)//2
        y = x-val1
        return [y, x]
    
a = Solution()
print(a.findTwoElement([3, 1, 2, 5, 4, 6, 7, 6]))