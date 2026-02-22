class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x_col = []
        y_col = []
        z_col = []

        for triplet in triplets:
            if (triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]):
                continue
            else:
                x_col.append(triplet[0])
                y_col.append(triplet[1])
                z_col.append(triplet[2])
        
        if (target[0] in x_col and target[1] in y_col and target[2] in z_col):
            return True
        else:
            return False