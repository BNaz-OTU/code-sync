class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashMap = {}
        final = []

        for num in nums:
            if num in hashMap:
                final.append(num)

                if (len(final) == 2):
                    return final

            else:
                hashMap[num] = 0