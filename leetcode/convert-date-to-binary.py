class Solution:
    def convertDateToBinary(self, date: str) -> str:
        split_date = date.split("-")
        final = []

        for val in split_date:
            binary = bin(int(val))[2:]
            final.append(binary)
        
        return "-".join(final)