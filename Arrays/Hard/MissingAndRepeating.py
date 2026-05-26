class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        occurance = {}

        for el in arr:
            if el in occurance:
                occurance[el]+=1
            else:
                occurance[el]=1
        print(occurance)

        repeating = -1
        missing = -1

        for i in range(1,n+1):
            if i not in occurance:
                missing = i
            elif occurance[i]==2:
                repeating = i

        return [repeating, missing]
    
a = Solution()
print(a.findTwoElement([3, 1, 2, 5, 4, 6, 7, 6]))