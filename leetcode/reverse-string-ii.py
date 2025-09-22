class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)

        for idx in range(0, len(s) - 1, 2 * k):
            left = idx
            right = idx + k - 1

            if (right >= len(s)):
                right = len(s) - 1

            while left < right:
                print(f"Left: {left} | Right: {right}")
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return "".join(s_list)