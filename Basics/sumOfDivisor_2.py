class Solution:
    def sumOfDivisors(self, n):
        result = 0
        for i in range(1, n+1):
            # i is a divisor of i, 2*i, 3*i, ... up to n
            # So i contributes to (n//i) numbers
            result += i * (n // i) #result = number(i) x with how many numbers it divides with(n//i)
        return result
    

    #n=4
    #i=1,result=1*4=4
    #i=2,result=4+(2*2)=8
    #i=3,result=8+(3*1)=11
    #i=4,result=11+(4*1)=15