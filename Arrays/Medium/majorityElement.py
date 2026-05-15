class Solution:
    def majorityElement(self, arr):
        count = 0
        hashmap = {}

        for el in arr:
            if el in hashmap:
                hashmap[el]+=1
            else:
                hashmap[el] = 1
        
        for el,count in hashmap.items():  # hashmap.items() returns a list of tuples (key,value) pairs, we can unpack them into el and count.
            if float(count) > len(arr)/2:
                return el
            
a = Solution()
print(a.majorityElement([2,3,5,2,3,4,5,4,5,5,5,5,5]))