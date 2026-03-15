

def twoSum(nums,target):

    sub_list=[]
    index=[]
    
    for i,num in enumerate(nums):

        subs=(num-target)
        sub_list.append(subs)

        for j,sub in enumerate(sub_list):
            if num==(-sub):
                if i<j:
                    index.append(i)
                    index.append(j)
                if i>j:
                    index.append(j)
                    index.append(i)
    return index
