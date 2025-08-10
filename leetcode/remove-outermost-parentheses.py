class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        countOpen = 0
        # stack = []
        final = ""

        for bracket in s:
            if (bracket == '(' and countOpen == 0):
                countOpen += 1

            elif (bracket == '('):
                countOpen += 1
                final += bracket

            elif (bracket == ')' and countOpen != 1):
                countOpen -= 1
                final += bracket

            elif (bracket == ')' and countOpen == 1):
                countOpen = 0

        return final