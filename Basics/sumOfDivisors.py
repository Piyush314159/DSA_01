class Solution:
    def sumOfDivisors(self, n):
        dict_sum={}
        for i in range(1,n+1):
            F=0
            for j in range(1, int(i**0.5)+1): #after sqrt(i) the divisors starts reapeting thats why upto that 
                #suppose i = 4
                #then, first divisor j=1 and the paired divisor is i//j=4 so
                # j=1,4(first Pair)
                # j=2,2(second Pair)
                #then again reapets after j=sqrt(4)=2
                if i % j == 0:
                    F += j
                    if j != (i // j): #this specially if in a pair both divisor are not same
                        F += (i // j)
            dict_sum[i]=F
        return sum(dict_sum.values())

a=Solution()
print(a.sumOfDivisors(4)) 