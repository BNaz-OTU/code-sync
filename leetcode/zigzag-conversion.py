class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # Failed attempt
        final = ""

        if (numRows % 2 == 0):
            for idx in range(numRows):
                print(s[idx::numRows + 2])
                final += s[idx::numRows + 2]
        else:
            for idx in range(numRows):
                if (idx % 2 == 0):
                    print(s[idx::numRows + 1])
                    final += s[idx::numRows + 1]
                else:
                    print(s[idx::numRows - 1])
                    final += s[idx::numRows - 1]
        
        return final


        pass
        # P Y A I H R N
        # A P L S I I G

        # Even Up by 2
        # Odd up by 1