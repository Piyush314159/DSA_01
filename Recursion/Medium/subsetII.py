def subset(nums):
    lst = []
    nums.sort()

    def backtrack(i, c):

        if i >= len(nums):
            lst.append(c[:])
            return

        c.append(nums[i])
        backtrack(i+1, c)
        c.pop()

        j = i + 1
        while j < len(nums) and nums[j] == nums[i]:
            j += 1
        backtrack(j, c)

    backtrack(0, [])
    return lst

print(subset([4,4,4,1,4]))