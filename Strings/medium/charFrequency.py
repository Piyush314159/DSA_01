class Solution:
    def frequencySort(self, s: str) -> str:

        # making the hash table to store the frequency of each character
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # sorting the hash table based on the frequancy of each character
        bucket = [[] for _ in range(len(s)+1)]
        for ch, count in freq.items():
            bucket[count].append(ch)

        # creating the result string based on the sorted hash table
        result = []
        for count in range(len(bucket) -1, 0, -1) :
            for ch in bucket[count]:
                result.append(ch*count)
        return "".join(result)

a = Solution()
print(a.frequencySort("tree"))  # "eert"
print(a.frequencySort("cccaaa"))  # "aaaccc"
print(a.frequencySort("Aabb"))  # "bbAa"