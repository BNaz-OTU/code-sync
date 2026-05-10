class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        insert = 0
        group = 1

        while idx < len(chars):
            group = 1
            while (group + idx) < len(chars) and chars[group + idx] == chars[idx]:
                group += 1
            
            chars[insert] = chars[idx]
            insert += 1

            if group > 1:
                    str_val = str(group)
                    chars[insert : insert + len(str_val)] = list(str_val)
                    insert += len(str_val)
            
            idx += group
            
        return insert