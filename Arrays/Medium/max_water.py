class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        i, j = 0, n-1
        max_water = 0

        while i < j:
            mini = min(height[i], height[j])
            max_water = max(max_water, (j - i)* mini )

            if height[i] < height[j]: 
                #that means everything less that j will decrease the length
                #  which will decraese area so we will rule those out by increasing i
                i += 1
            else:
                #same here if the jth el is smaller increasing i will only decraese the area so just change the 
                j -= 1
        return max_water