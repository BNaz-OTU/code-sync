class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_let = {}

        for val in s:
            if (val in count_let):
                count_let[val] += 1
            else:
                count_let[val] = 1
        
        sumVal = 0
        oddFound = False
        # maxOdd = 0
        # listEven = []

        print(count_let)

        for key in count_let:
            if (count_let[key] % 2 == 0):
                # listEven.append(key)
                sumVal += count_let[key]
            else:
                oddFound = True

                sumVal += (count_let[key] - 1)
                # maxOdd = max(maxOdd, count_let[key])
        
        if (oddFound):
            return sumVal + 1
        else:
            return sumVal

        print(listEven)
        print(maxOdd)
        
        return sumVal + maxOdd