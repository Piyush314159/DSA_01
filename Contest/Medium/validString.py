"""
* Backtracking / DFS over all positions     → O(2^n) worst case
* Pruning on cost > k                       → cuts off invalid branches early
* String concatenation at each step         → O(n) per valid string
* Overall                                   → O(2^n * n)
* Space (recursion depth + result storage)  → O(n) per call stack, O(2^n * n) total for result
"""

class Solution:
    def validString(self, n, k):
        result = []

        def backtrack(index, currString, lastChar, currCost):

            # base case : when string length is n
            if index == n:
                if currCost <= k:
                    result.append(currString)
                return
            
            # pruning
            if currCost > k:
                return

            # case 1: add '0' (always allowed)
            backtrack(index+1, currString + '0', '0', currCost)

            # case 2: add '1' (only allowed when last character is not '1')
            if lastChar != '1':
                backtrack(index+1, currString + '1', '1', currCost + 1)
        
        backtrack(0, "", '0', 0)
        return result

a = Solution()
print(a.validString(10, 5))

'''
backtrack(0, "", '0', 0)
│
├── place '0' → backtrack(1, "0", '0', 0)
│   │
│   ├── place '0' → backtrack(2, "00", '0', 0)
│   │   │
│   │   ├── place '0' → backtrack(3, "000", '0', 0)
│   │   │       index==3, cost=0<=1 ✓ → result.append("000")
│   │   │
│   │   └── place '1' → backtrack(3, "001", '1', 0+2=2)
│   │           index==3, cost=2>1 ✗ → not added
│   │
│   └── place '1' → backtrack(2, "01", '1', 0+1=1)
│       │
│       ├── place '0' → backtrack(3, "010", '0', 1)
│       │       index==3, cost=1<=1 ✓ → result.append("010")
│       │
│       └── lastChar=='1', so '1' branch SKIPPED entirely
│
└── place '1' → backtrack(1, "1", '1', 0+0=0)
    │
    ├── place '0' → backtrack(2, "10", '0', 0)
    │   │
    │   ├── place '0' → backtrack(3, "100", '0', 0)
    │   │       index==3, cost=0<=1 ✓ → result.append("100")
    │   │
    │   └── place '1' → backtrack(3, "101", '1', 0+2=2)
    │           index==3, cost=2>1 ✗ → not added
    │
    └── lastChar=='1', so '1' branch SKIPPED entirely
'''