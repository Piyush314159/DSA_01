class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(start, current):
            res.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
                
        backtrack(0, [])
        return res

sol = Solution()
print(sol.subsets([1,2,3]))

'''
pick - don't pick logic
'''
lst = []
def sequences(i, c, arr):
    if i >= len(arr):
        lst.append(c[:])
        return 

    c.append(arr[i])
    sequences(i+1, c, arr)  #pick
    c.pop()
    sequences(i+1, c, arr)  #don't pick
    return lst

print(sequences(0, [], [3, 1, 2]))