class Solution:
    def missingRepeatingNumber(self, arr):
        n = len(arr)
        occurance = {}

        for num in arr:
            if num in occurance:
                occurance[num]+=1
            else:
                occurance[num] = 1

        missing = -1
        repeating = -1

        for i in range(1,n+1):
            if i not in occurance:
                missing = i
            elif occurance[i]==2:
                repeating = i

        return occurance,missing,repeating
    
a = Solution()
print(a.missingRepeatingNumber([3, 1, 2, 5, 4, 6, 7, 6]))