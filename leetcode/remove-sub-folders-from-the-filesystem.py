class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        visit = set()
        final = []

        def checker(temp_str, fold):
            for idx, char in enumerate(fold):
                temp_str += char

                if temp_str in visit and ((idx + 1 == len(fold)) or (fold[idx + 1] == "/")):
                    return False
            
            visit.add(fold)
            return True

        for fold in folder:
            if (checker("", fold)):
                final.append(fold)
        
        return final