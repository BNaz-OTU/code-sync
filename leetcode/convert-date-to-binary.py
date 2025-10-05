class Solution:
    def convertDateToBinary(self, date: str) -> str:
        split_date = date.split("-")
        final = []

        for val in split_date:
            part = ""
            curr_val = int(val)

            while curr_val != 0:
                quotient = curr_val // 2
                carry = curr_val % 2

                curr_val = quotient
                part += str(carry)
            
            final.append(part[::-1])
        
        return "-".join(final)