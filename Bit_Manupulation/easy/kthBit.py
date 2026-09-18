class Solution:
    def checkKthBit(self, n, k):        #n-->integer , k---->index
        bit = []
        while n:
            bit.append(n%2)
            n = n//2
        if k < len(bit) and bit[k] == 1:
            return True
        return False

s = Solution()
print(s.checkKthBit(4,0))

def checkbit2(n,k):
    return (n and (1<<k)) != 0
print(checkbit2(4,0))