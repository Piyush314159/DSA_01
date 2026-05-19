class Solution:
    def longestConsecutive(self,arr):
        longest = 1
        n = len(arr)
        arr_set = set(arr) #create a set from the input array to allow for O(1) lookups when checking for consecutive elements

        for el in arr_set:
            if el - 1 not in arr_set: #check if the current element is the start of a new sequence by checking if the previous element (el - 1) is not in the set.
                x = el
                count = 1
                while x+1 in arr_set:#if the next element (x + 1) is in the set, it means we have found a consecutive element, so we increment x and count to keep track of the length of the current sequence.
                    x += 1
                    count += 1
                longest = max(longest , count) #update longest if the current sequence is longer than the previously recorded longest sequence.

        return longest
    
a = Solution()
print(a.longestConsecutive([1, 9, 3, 10, 4, 20, 2]))