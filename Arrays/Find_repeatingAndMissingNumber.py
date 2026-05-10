class Sollution:
    def missingRepeatingNumber(self, arr):
        n = len(arr)
        sn = (n*(n+1))//2
        sn_2 = (n*(n+1)*(2*n+1))//6
        s = 0
        s_2 = 0

        for el in arr:
            s+=el
            s_2+=el**2

        val1 = s-sn #x-y
        val2 = s_2 - sn_2 #x^2-y^2
        
        val3 = val2//val1 #x+y
        x = (val1 + val3) // 2   # repeating
        y = x - val1 

        return x,y
    
a = Sollution()
print(a.missingRepeatingNumber([3, 1, 2, 5, 4, 6, 7, 6]))

