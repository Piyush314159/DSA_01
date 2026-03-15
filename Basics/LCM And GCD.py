class Solution:
    def lcmAndGcd(self, a : int, b : int):

        int_len = len(str(a)) if len(str(a))>len(str(b)) else len(str(b))
        dict_array_gcd_lcm={}
        for i in range(2,10**int_len):
            if a%i==0 and b%i==0:
                a_rem = int(a/i)
                b_rem = int(b/i)
                dict_array_gcd_lcm[i*a_rem*b_rem]=[i*a_rem*b_rem,i]
            else:
                dict_array_gcd_lcm[1*a*b]=[1*a*b,1]
        return dict_array_gcd_lcm[min(dict_array_gcd_lcm)]
a=Solution()
print(a.lcmAndGcd(10,5))