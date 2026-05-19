class Solution:
    def leaders(self, arr):
        n= len(arr)
        leader = []
        max_right = arr[-1]                 #the rightmost element is always a leader, so we add it to the list and set it as the initial max_right

        leader.append(arr[-1])              #add the rightmost element to the list of leaders

        for i in range(n-2, -1, -1):
            if arr[i]>= max_right:           #if the current element is greater than the max_right, it is a leader, so we add it to the list and update max_right
                leader.append(arr[i])
                max_right = arr[i]
        return leader[::-1]                 #reverse the list of leaders to maintain the original order of leaders in the input array

a = Solution()
print(a.leaders([16, 17, 4, 3, 5, 2]))
