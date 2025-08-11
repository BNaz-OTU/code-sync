class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        reverseWord = ""
        endpoint = None

        for idx in range(len(word)):
            if (word[idx] == ch):
                reverseWord += word[idx]
                endpoint = idx
                break
            else:
                stack.append(word[idx])
        
        if (reverseWord == ""):
            return word
    
        while len(stack) != 0:
            reverseWord += stack.pop()
        
        return reverseWord + word[endpoint + 1:]