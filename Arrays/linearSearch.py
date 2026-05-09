class Sollution:
    def linearSearch(self, arr, k):
        n = len(arr)
        idx = -1

        for i in range(n):
            if arr[i]==k:
                idx=i

        return idx
            
a = Sollution()
print(a.linearSearch([1, 2, 3, 6, 3,5], 6))