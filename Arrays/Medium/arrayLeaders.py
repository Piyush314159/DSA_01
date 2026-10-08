class Solution:
    def leaders(self, arr):
        leader = [arr[-1]]
        n = len(arr)
        i, j = n-1, n-2
        while j >= 0:
            if arr[j] >= arr[i]:
                leader.append(arr[j])
                i = j
            j -= 1
        return leader[::-1]               #reverse the list of leaders to maintain the original order of leaders in the input array

a = Solution()
print(a.leaders([16, 17, 4, 3, 5, 2]))
