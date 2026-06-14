class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        final = set()

        def checker(fold):
            word = ""
            for idx in range(len(fold)):
                word += fold[idx]

                if (word in final and (idx + 1 < len(fold) and fold[idx + 1] == "/")):
                    return False
            
            return True

        for fold in folder:
            if (checker(fold)):
                final.add(fold)
        
        return list(final)