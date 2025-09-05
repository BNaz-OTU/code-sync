class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        end = len(s) - 1
        list_s = list(s)

        for idx in range(0, end, 2 * k):
            left = idx
            right = idx + k - 1
            print(left, right)

            if (right > end):
                right = end

            while (left < right):
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left += 1
                right -= 1
        
        return "".join(list_s)