# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        final = []

        def dfs(root):
            if (root is None):
                final.append("N")
                return
            
            final.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        final_string = ",".join(final)
        return final_string
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        idx = 0

        def dfs():
            nonlocal idx
            # if (idx >= len(data)):
            #     return None

            if (vals[idx] == "N"):
                idx += 1
                return None

            root = TreeNode(int(vals[idx]))
            idx += 1

            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()
         
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))