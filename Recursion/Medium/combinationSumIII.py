'''
k -> 1 to 9
n -> target
c -> current list
'''
def combinationSumIII(k, n):
    lst = []
    def helper(i, c, remaining):
        if len(c) >= k and remaining == 0 :
            lst.append(c[:])
            return

        if len(c) == k or i > 9 or remaining < 0:
            return

        c.append(i)
        helper(i + 1, c, remaining - i)
        c.pop()
        helper(i + 1 , c, remaining)

    helper(1, [], n)

    return lst

print(combinationSumIII(3, 9))