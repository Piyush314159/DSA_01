def combinationSumII(candidates, target):

    # Sorting the array is important to skip duplicates
    candidates.sort()
    lst = []

    def helper(i, target, c):
        if target == 0:
            lst.append(c[:])
            return
        
        if i >= len(candidates) or target < 0:
            return

        c.append(candidates[i])
        helper(i+1, target - candidates[i], c)
        c.pop()

        # SKIP — jump past all duplicates of candidates[i]
        j = i + 1
        while j < len(candidates) and candidates[j] == candidates[i]:
            j += 1
        helper(j, target, c)
        
    helper(0, target, [])
        
    return lst
        
print(combinationSumII([10,1,2,7,6,1,5], 8))