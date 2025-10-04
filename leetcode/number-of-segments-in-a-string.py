class Solution:
    def countSegments(self, s: str) -> int:
        new_s = s.split(" ")
        counter = 0

        for val in new_s:
            if (val == ""):
                continue
            counter += 1
        
        return counter