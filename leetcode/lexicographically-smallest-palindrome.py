class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        # Odd Number
        new_s = ""

        if (len(s) % 2 == 1):
            middle = len(s) // 2
            left = middle - 1
            right = middle + 1
            new_s += s[middle]

            while left >= 0:
                r_char = ord(s[right])
                l_char = ord(s[left])
                
                if (l_char < r_char):
                    r_char = l_char

                elif (r_char < l_char):
                    l_char = r_char


                left -= 1
                right += 1
                new_s += chr(l_char)
            print(new_s)
            return new_s[::-1] + new_s[1::]
        
        # Even Number
        else:
            right = len(s) // 2
            left = right - 1
            # new_s += middle

            while left >= 0:
                r_char = ord(s[right])
                l_char = ord(s[left])
                
                if (l_char < r_char):
                    r_char = l_char

                elif (r_char < l_char):
                    l_char = r_char


                left -= 1
                right += 1
                new_s += chr(l_char)
            
            # print(new_s)
            return new_s[::-1] + new_s[::]