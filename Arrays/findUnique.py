class Solution:
    def findUnique(self, arr):
        n = len(arr)
        freq = {}

        for el in arr:
            if el in freq:
                freq[el]+=1
            else:
                freq[el]=1
        
        for key,val in freq.items():
            if val==1:
                return key

    
a = Solution()
print(a.findUnique( [2, 30, 2, 15, 20, 30, 15]))