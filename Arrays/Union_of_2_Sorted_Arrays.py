class Solution:
    def findUnion(self, a, b):
        out_arr = []
        i=j=0

        while i<len(a) and j<len(b):
            #chechking which elemnt is greater
            if a[i]< b[j]:
                if len(out_arr)==0 or out_arr[-1]!=a[i]:
                    out_arr.append(a[i])
                i+=1
            elif a[i]>b[j]:
                if len(out_arr)==0 or out_arr[-1]!=b[j]:
                    out_arr.append(b[j])
                j+=1
            else:
                if len(out_arr) == 0 or out_arr[-1] != a[i]:
                    out_arr.append(a[i])
                i += 1
                j += 1

        #adding left-out element
        while i<len(a):
            if out_arr[-1] != a[i]:
                out_arr.append(a[i])
            i+=1

        while j<len(b):
            if out_arr[-1]!=b[j]:
                out_arr.append(b[j])
            j+=1

        return out_arr

a = Solution()
print(a.findUnion([1, 2, 3, 4, 5], [1, 2, 3, 6, 7,8]))