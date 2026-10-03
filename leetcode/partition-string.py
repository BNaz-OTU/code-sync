class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        arr = []
        current = ""

        for char in s:
            current += char
            if (current not in seen):
                arr.append(current)
                seen.add(current)
                current = ""
        
        return arr