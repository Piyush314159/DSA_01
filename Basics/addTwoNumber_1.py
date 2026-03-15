import numpy as np
a=[2,4,3]
b=[5,6,4]
def addTwoNumber(list1,list2):
    sum=np.array(list1)+np.array(list2)
    i=0
    for i in range(-1,len(sum)):
        if sum[i]>=10:
            sum[i]=sum[i]-10
            sum[i+1]=sum[i+1]+1
        else:
            sum[i]=sum[i]
        i-=1
    return sum
print(addTwoNumber(a,b))