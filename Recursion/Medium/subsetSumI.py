def subsetSumsI(arr):
    lst = []
    def helper(i, sum):

        if i >= len(arr):
            lst.append(sum)
            return

        helper(i+1, sum + arr[i])
        helper(i+1, sum)

    helper(0, 0)
    lst.sort()
    return lst

print(subsetSumsI([2, 3]))