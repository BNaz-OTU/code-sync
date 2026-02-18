class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # ANOTHER SOLN: https://www.youtube.com/watch?v=kShkQLQZ9K4

        x_col_arr = []
        y_col_arr = []
        z_col_arr = []

        if (len(triplets) == 1 and triplets[0] == target):
            return True

        for idx in range(len(triplets)):
            flag = False
            for jdx in range(len(triplets[idx])):

                if (triplets[idx][jdx] > target[jdx]):
                    flag = True
            
            if (flag == False):
                x_col_arr.append(triplets[idx][0])
                y_col_arr.append(triplets[idx][1])
                z_col_arr.append(triplets[idx][2])
        
        if (len(x_col_arr) >= 2 and target[0] in x_col_arr and target[1] in y_col_arr and target[2] in z_col_arr):
            return True
        else:
            return False

        print(f"X's: {x_col_arr}")
        print(f"Y's: {y_col_arr}")
        print(f"Z's: {z_col_arr}")