#User function Template for python3

class Solution:
    def rearrange(self,arr):
        n = len(arr)
        pos = []
        neg = []
        new = []

        for i in range(n):
            if arr[i]>=0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])
        
        i=j=0
        while i<len(pos) and j<len(neg):
            new.append(pos[i])
            new.append(neg[j])
            i+=1
            j+=1

        while i<len(pos):
            new.append(pos[i])
            i+=1

        while j<len(neg):
            new.append(neg[j])
            j+=1
        
        return new

a =Solution()
print(a.rearrange( [9, 4, -2, -1, 5, 0, -5, -3, 2]))