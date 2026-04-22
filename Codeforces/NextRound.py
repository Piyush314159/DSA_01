n,k = map(int,input().split())
scores = list(map(int, input().split()))
adv_participant = 0
for i in range(n):
    if scores[i]>=scores[k - 1] and scores[i]>0:
        adv_participant+=1
print(adv_participant)