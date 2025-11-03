class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        left_answer = []
        right_answer = []
        final = []

        s_reverse = s[::-1]

        fast = 0
        slow = 0
        while fast < len(s):
            if (s[fast] == c):
                while slow <= fast:
                    left_answer.append(abs(slow - fast))
                    slow += 1
            
            fast += 1
        
        while len(left_answer) < len(s):
            left_answer.append(-1)

        fast = 0
        slow = 0

        while fast < len(s):
            # print(s_reverse[fast])
            if (s_reverse[fast] == c):
                while slow <= fast:
                    # print(f"Inner: {s_reverse[slow]} | R_Ans: {right_answer}")
                    right_answer.append(abs(slow - fast))
                    slow += 1
            fast += 1
        
        while len(right_answer) < len(s):
            right_answer.append(-1)

        right_answer = right_answer[::-1]

        print(f"Left Len: {len(left_answer)} | Right Len: {len(right_answer)}")

        for idx in range(len(s)):
            print(idx)
            if (right_answer[idx] == -1):
                final.append(left_answer[idx])
            elif (left_answer[idx] == -1):
                final.append(right_answer[idx])
            else:
                print(f"Left: {left_answer[idx]}")
                print(f"Right: {right_answer[idx]}")
                final.append(min(left_answer[idx], right_answer[idx]))
        
        return final


        # print(f"Left First: {left_answer} \nRight First: {right_answer[::-1]}")
        # return answer