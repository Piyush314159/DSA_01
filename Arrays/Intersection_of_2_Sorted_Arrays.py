class Solution:
    def findIntersection(self, a, b):
        out_arr = []
        i=j=0

        while i<len(a) and j<len(b):
            if a[i]==b[j]:
                out_arr.append(a[i])
                i+=1
                j+=1
            elif a[i]<b[j]:
                i+=1
            else:
                j+=1

        return out_arr

a = Solution()
print(a.findIntersection([1, 2, 3, 4, 5], [1, 2, 3, 6, 7,8]))