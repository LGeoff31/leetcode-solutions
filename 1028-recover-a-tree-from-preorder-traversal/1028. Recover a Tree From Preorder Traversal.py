# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def dfs(string):
            if not string:
                return
            if string.count("-") == 0:
                return TreeNode(int(string))
            num = ""
            i = 0
            while i < len(string) and string[i].isdigit():
                num += string[i]
                i += 1
    
            root = TreeNode(int(num))
            numberDashes = 0
            idx = -1
            for i in range(i, len(string)):
                if string[i] != "-": 
                    idx = i
                    break
                numberDashes += 1
            nextOccurence = -1
            curr = 0
            idx2 = -1
            for i in range(idx, len(string)):
                if string[i] == "-":
                    curr += 1
                else:
                    curr = 0
                if curr == numberDashes and (i+1==len(string) or string[i+1]!="-"):
                    idx2 = i+1
                    break
            print(idx, idx2)
            print(string[idx : idx2 - numberDashes])
            print(string[idx2:])
            if idx2 != -1:
                root.left = dfs(string[idx : idx2 - numberDashes])
                root.right = dfs(string[idx2:])
            else:
                root.left = dfs(string[idx:])
            return root
        
        return dfs(traversal)