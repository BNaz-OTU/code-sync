class Solution:
    def maximumTime(self, time: str) -> str:
        final = ""

        # if (time[0] == "?" and time[1] == "?"):
        #     time = "23" + time[2:]

        for idx in range(len(time)):
            if (idx == 0 and time[idx] == "?"):
                if (time[idx + 1] == "?" or int(time[idx + 1]) < 4):
                    final += "2"
                elif (int(time[idx + 1]) >= 4):
                    final += "1"
            
            elif (idx == 1 and time[idx] == "?"):
                if (int(final[idx - 1]) <= 1):
                    final += "9"
                elif (final[idx - 1] == "2"):
                    final += "3"
            

            elif (idx == 3 and time[idx] == "?"):
                final += "5"
            elif (idx == 4 and time[idx] == "?"):
                final += "9"
            else:
                final += time[idx]
        
        return final