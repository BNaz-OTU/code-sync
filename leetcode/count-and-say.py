class Solution:
    def countAndSay(self, n: int) -> str:
        
        def function(val):
            if (val == "1"):
                return "11"
            
            new_str = ""
            count = 1
            for idx in range(len(val) - 1):
                if (val[idx] == val[idx + 1]):
                    count += 1
                else:
                    new_str += str(count) + val[idx]
                    count = 1
            
            new_str += str(count) + val[idx + 1]
            return new_str
        
        val = "1"
        for _ in range(n - 1):
            val = function(val)
        
        return val