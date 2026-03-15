class Solution:
    def lcmAndGcd(self, a : int, b : int):#lcm x gcd = a x b
        if a==0 and b==0:
            return [0,0]
        
        def gcd(x,y): #GCD(a, b) = GCD(b, a % b)
            i=1
            i_arr=[]
            while i<= min(x, y):
                if x%i==0 and y%i==0:
                    i_arr.append(i)
                i+=1

            return max(i_arr)
        g=gcd(a,b)

        lcm=(a*b)//g
        return [lcm,g]
a=Solution()
print(a.lcmAndGcd(5,10))