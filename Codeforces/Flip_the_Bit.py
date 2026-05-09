c = int(input()) #number of test cases
out_arr=[]
for _ in range(c):
    n, k = map(int, input().split()) #n-binary array, k-special indices
    bit_arr = list(map(int,input().split()))
    spcl = int(input())
    x = bit_arr[spcl-1]
    left_side = bit_arr[0:spcl-1]
    right_side = bit_arr[spcl:n]

    prev = x  # assume element before the side is "good" (equal to x)
    count = 0
    for el in  left_side:
        if el != x and prev == x:
            count += 1
        prev = el #setting current element as prev

    prev = x
    for el in  right_side:
        if el != x and prev == x:
            count += 1
        prev = el
    out_arr.append(count)
print('\n'.join(map(str,out_arr)))