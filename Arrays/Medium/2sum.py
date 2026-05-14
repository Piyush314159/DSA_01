class Solution:
    def allPairs(self, target, arr1, arr2):
        freq = {}
        for x in arr2:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        pair = []
        for y in sorted(arr1): #sort arr1 to ensure pairs are in ascending order
            complement = target - y
            if complement in freq:
                for _ in range(freq[complement]): #add the pair as many times as the complement appears in arr2
                    pair.append([y, complement])
        return pair
    
a = Solution()
print(a.allPairs(5, [1, 2, 3, 4,1,2], [1, 2, 3, 4,3,2]))