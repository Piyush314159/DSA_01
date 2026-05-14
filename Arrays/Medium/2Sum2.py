class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap:
                return [hashmap[compliment],i]
            hashmap[nums[i]] = i

    
a = Solution()
print(a.twoSum([2,7,11,15],9))