class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # USED SOLN: https://www.youtube.com/watch?v=FZe0UqISmUw
        if (len(nums) == 0):
            return [[]]
        
        perms = self.permute(nums[1:])
        n_perm = []

        for p in perms:
            for idx in range(len(p) + 1): # Included '+ 1' so I can insert a number at the end
                # Create a copy, if you don't the previous appended permutations will also be modified
                p_copy = p.copy() 

                # Insert the current number to all possible positions
                p_copy.insert(idx, nums[0])

                # After completing the insert for current permutation, add it to new perm list.
                # This new perm list will get called recursively so more numbers get added
                n_perm.append(p_copy)
        
        # OTHER BASE CASE
        return n_perm