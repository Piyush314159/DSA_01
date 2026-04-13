class Solution:
    def frequencyOfOccurance(self,arr):
        occ = {}
        for el in arr:
            occ[el] = occ.get(el, 0) + 1 #finds the element's occurance in the dictionary(occ) if not able find then returns 0(default), get(element,default)

        output = []
        for i in range(1,len(arr)+1):
            output.append(occ.get(i,0))

        return output
     
a = Solution()
print(a.frequncyOfOccurance([2, 3, 2, 3, 5]))