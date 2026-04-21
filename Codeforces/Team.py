n = int(input())
solution = 0
for i in range(n):
    a,b,c = map(int,input().split()) #input().split()---->list , int---->function , map(function,list)
    if a+b+c>=2:
        solution+=1
print(solution)