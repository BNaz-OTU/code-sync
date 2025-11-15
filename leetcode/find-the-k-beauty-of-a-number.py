class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        substr = ""
        k_beauty = 0

        str_num = str(num)

        for idx in range(k):
            substr += str_num[idx]
        
        if (num % int(substr) == 0 and int(substr) != 0):
            k_beauty += 1

        for idx in range(k, len(str_num)):
            substr = substr[1:]
            substr += str_num[idx]

            if (int(substr) != 0 and num % int(substr) == 0):
                k_beauty += 1
        
        return k_beauty