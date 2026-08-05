def genarateStringRecurs(n, current = "", count = 0):

    if n == len(current):
        print(current, end = " ")
        return count + 1

    count = genarateStringRecurs(n, current + '0', count)

    if current == '' or current[-1] != '1':
        count = genarateStringRecurs(n, current + '1', count)

    return count

print(genarateStringRecurs(4, "", 0))