def combinationSum(arr, target):
    lst = []
    arr.sort()

    def helper(i, target, l):

        if target == 0:
            lst.append(l[:])
            return

        if i >= len(arr) or arr[i] > target:
            return

        l.append(arr[i])
        helper(i, target - arr[i], l)
        l.pop()
        helper(i+1, target, l)

    helper(0, target, [])

    return lst

print(combinationSum([2, 3, 6, 7], 7))