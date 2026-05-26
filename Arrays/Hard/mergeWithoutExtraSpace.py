class Solution:
    def mergeArrays(self, a, b):
        i, j = len(a)-1, 0              #start from the end of a and the beginning of b

        while i>=0 and j<len(b):
            if a[i]>b[j]:               #if the current element of a is greater than the current element of b, swap them and move the pointer of a to the left
                a[i], b[j] = b[j], a[i]
                i-=1
            else:                       #otherwise, move the pointer of b to the right    
                j+=1
        a.sort()
        b.sort()
        return a, b

a = Solution()
print(a.mergeArrays([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]))