'''
Boyer-Moore Majority Vote Algorithm:
        * Selecting 2 candidates (Boyer-Moore) → O(n)
        * Verifying candidates → O(n)
        * Space → O(1)
'''
class Solution:                     #[2, 2, 3, 1, 3, 2, 1, 1]
    def findMajority(self, arr):
        c1, c2 = None, None
        cnt1, cnt2 = 0, 0

        for el in arr: # Iterate through the array to find potential majority candidates
            if el==c1:
                cnt1+=1
            elif el==c2:
                cnt2+=1
            elif cnt1==0:
                c1, cnt1 = el, 1
            elif cnt2==0:
                c2, cnt2 = el, 1
            else:
                cnt1-=1
                cnt2-=1
            
        majority = [] # Verify the candidates by counting their occurrences in the array and checking if they occur more than n/3 times
        for c in [c1, c2]:
            if arr.count(c) > len(arr) // 3:
                majority.append(c)
        
        return majority
    
a = Solution()
print(a.findMajority([2, 2, 3, 1, 3, 2, 1, 1]))
