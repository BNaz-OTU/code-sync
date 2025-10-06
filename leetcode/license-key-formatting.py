class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        final = []
        new_s = s[::-1]
        temp = ""

        print("0".isalnum())

        for val in new_s:
            if (len(temp) == k):
                final.append(temp[::-1])
                temp = ""
            
            if (val.isalpha()):
                temp += val.upper()
            
            elif (val.isalnum()):
                temp += val
        
        if (len(temp) != 0):
            final.append(temp[::-1])

        return "-".join(final[::-1])

        # num_groups = len(s) // k
        # firstDash = False
        # temp = ""

        # for idx in range(len(s)):
        #     print(idx, firstDash)

        #     if (firstDash == False and s[idx] == "-"):
        #         firstDash = True
        #         final.append(temp)
        #         temp = ""
        #         print('here1')

        #     elif (len(temp) == k):
        #         final.append(temp)
        #         temp = ""
        #         print('here')

            
        #     if (s[idx].isalpha()):
        #         temp += s[idx].upper()
            
        #     elif (s[idx] != "-"):
        #         temp += s[idx]
            
        #     print(temp)