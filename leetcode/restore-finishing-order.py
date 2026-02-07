class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        final = [0] * len(friends)
        dictFriend = {}

        count = 0
        for idx in range(len(order)):
            if (order[idx] in friends):
                dictFriend[order[idx]] = count
                count += 1
        
        for key in dictFriend:
            idx = dictFriend[key]
            final[idx] = key
        
        return final