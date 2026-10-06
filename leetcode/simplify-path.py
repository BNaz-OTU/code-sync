class Solution:
    def simplifyPath(self, path: str) -> str:
        final = []

        split_path = path.split("/")
        split_path = [val for val in split_path if val != ""]
        print(split_path)

        for cdir in split_path:
            if (cdir == "." or (len(final) == 0 and cdir == "..")):
                continue

            if (len(final) > 0 and cdir == ".."):
                final.pop()
                continue
            
            final.append(cdir)
        
        return "/" + "/".join(final)