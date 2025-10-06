class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        copy_s = s
        s_list = list(s)

        for idx in range(len(s)):
            s_list[idx] = copy_s[(idx + k) % len(s)]
        
        return "".join(s_list)

        # s_list[0] = 'b'

        # print(f"OG: {s} | COPY: {copy_s} | LIST: {s_list}")