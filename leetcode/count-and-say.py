class Solution:
    def countAndSay(self, n: int) -> str:
        def specialFunc(val):
            if (val == "1"):
                return "11"
            n_str = ""
            count = 1
            for idx in range(len(val) - 1):
                if (val[idx] == val[idx + 1]):
                    count += 1
                else:
                    n_str += (str(count) + val[idx])
                    count = 1
            
            n_str += (str(count) + val[idx + 1])
            return n_str
        
        val = "1"
        for idx in range(n - 1):
            val = specialFunc(val)
            print(val)
        
        return val