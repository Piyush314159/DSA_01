num = "5231"

for i in range(len(num) - 1, -1, -1):
    if int(num[i]) % 2 == 1:
        print(num[0:i+1])
        break 
