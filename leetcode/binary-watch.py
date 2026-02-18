class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # USED SOLN: http://youtube.com/watch?v=P4baJqamOAk
        final = []

        for hour in range(12):
            for minute in range(60):
                if (bin(hour).count("1") + bin(minute).count("1") == turnedOn):
                    final.append(f"{hour}:{minute:02d}")
        
        return final