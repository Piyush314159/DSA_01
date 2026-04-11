class Solution:
    def lcmAndGcd(self, a : int, b : int):
        range_ = a if a<b else b
        gcd = 0
        for i in range(1,range_+1):
            if a%i==0 and b%i==0:
                gcd = i

        lcm = (a*b)//gcd
        return [lcm,gcd]
    
a = Solution()
print(a.lcmAndGcd(12,16))