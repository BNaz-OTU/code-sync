class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordSplit = s.split(" ")
        wordToLet = {}
        letToWord = {}

        if (len(wordSplit) != len(pattern)):
            return False

        # Mapping letters (from pattern) to the words
        for idx in range(len(pattern)):
            val = pattern[idx]

            if (val in letToWord):
                if (letToWord[val] == wordSplit[idx]):
                    continue
                else:
                    return False
            else:
                letToWord[val] = wordSplit[idx]
        
        # Mapping words to the letters (from pattern)
        for idx in range(len(pattern)):
            val = wordSplit[idx]

            if (val in wordToLet):
                if (wordToLet[val] == pattern[idx]):
                    continue
                else:
                    return False

            else:
                wordToLet[val] = pattern[idx]
        
        print(f"Word to Letter: {wordToLet}")
        print(f"Letter to Word:{letToWord}")
        
        return True