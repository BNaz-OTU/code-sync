class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # USED SOLN: https://leetcode.com/problems/shortest-distance-to-a-character/solutions/2854034/python-99-92-faster-two-pointers-o-n-solution
        carr = [index for index, value in enumerate(s) if value == c]
        ans = []
        j = 0
        # Since we inc 'i' every time, we can just use for loop
        for i in range(len(s)):
            # Only increment if next occurrence is closer than current one
            if j < len(carr) - 1:
                if abs(carr[j + 1] - i) < abs(carr[j] - i):
                    j += 1
            ans.append(abs(carr[j] - i))
        return ans