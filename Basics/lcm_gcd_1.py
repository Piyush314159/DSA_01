class Solution:
    def lcmAndGcd(self, a : int, b : int):#lcm x gcd = a x b
        if a==0 and b==0:
            return [0,0]
        
        def gcd(x,y): #GCD(a, b) = GCD(b, a % b)
            while y:
                x,y = y, x%y
            return x
        g=gcd(a,b)

        lcm=(a*b)//g
        return [lcm,g]
a=Solution()
print(a.lcmAndGcd(5,10))