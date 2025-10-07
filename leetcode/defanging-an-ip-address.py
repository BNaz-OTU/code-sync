class Solution:
    def defangIPaddr(self, address: str) -> str:
        # return address.replace(".", "[.]")

        final = ""
        
        for val in address:
            if (val != "."):
                final += val
            else:
                final += "[.]"
        
        return final