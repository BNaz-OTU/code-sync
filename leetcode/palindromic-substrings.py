class Solution:
    def countSubstrings(self, s: str) -> int:
        # USED SOLN: https://www.youtube.com/watch?v=4RACzI5-du8
        count = 0
        for idx in range(len(s)):
            # EVEN
            count += self.countPali(s, idx, idx + 1)
            
            # ODD
            count += self.countPali(s, idx, idx)
        
        return count

    def countPali(self, s, left, right):
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
                # print(f"Left IDX: {left} -- Left Val: {s[left]} | Right IDX: {right} -- Right Val: {s[right]} | Word: {s[left : right + 1]}")
                res += 1
                left -= 1
                right += 1
        return res