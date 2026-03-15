nums_1=[2,7,11,15]
target_1=9
seen={}
def twoSum(nums,target):
    for i,num in enumerate(nums):

        remaining=(target-num)#calculates the remaining
        if remaining in seen: #if it is in the dictionary 'seen' then it returns the index in dictionary and its real index
            return[seen[remaining],i]
        seen[num]=i #if not in dictionary seen then it wiil store the number and its index
    
a=twoSum(nums_1,target_1)
print(a)