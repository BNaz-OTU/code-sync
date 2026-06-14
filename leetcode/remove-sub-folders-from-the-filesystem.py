class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        final = set()

        def found(fold):
            nonlocal word
            for idx in range(len(fold)):
                char = fold[idx]
                word += char
                if (word in final and ((idx + 1) > len(fold) or fold[idx + 1] == "/")):
                    return False
            
            return True

        for fold in folder:
            word = ""

            if (found(fold)):
                print("here")
                final.add(word)                

        return list(final)