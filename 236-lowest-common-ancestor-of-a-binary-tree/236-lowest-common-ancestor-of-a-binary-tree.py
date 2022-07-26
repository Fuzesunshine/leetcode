# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
#         def findNode(node, val1, val2, res):
#             if val1 == val2:
#                 if node.val == val1:
#                     return True
#                 if node.left and findNode(node.left, val1, val1, res):
#                     return True
#                 if node.right and findNode(node.right, val1, val1, res):
#                     return True
#                 return False
#             else:
#                 if node.val != val1 and node.val != val2:
#                     found_right = False
#                     found_left = False
#                     if node.right:
#                         found_right = findNode(node.right, val1, val2, res)
#                     if node.left:
#                         found_left = findNode(node.left, val1, val2, res)
#                     if found_right and found_left:
#                         res.append(node)
#                         return True
#                     elif found_right or found_left:
#                         return True
#                     else:
#                         return False

#                 if node.val == val1:
#                     if node.right and findNode(node.right, val2, val2, res):
#                         res.append(node)
#                     if node.left and findNode(node.left, val2, val2, res):
#                         res.append(node)
#                     return True
                
#                 if node.val == val2:
#                     found_right = False
#                     found_left = False
#                     if node.right and findNode(node.right, val1, val1, res):
#                         res.append(node)
#                     if node.left and findNode(node.left, val1, val1, res):
#                         res.append(node)
#                     return True
                    

        
#         res = []
#         findNode(root, p.val, q.val, res)
        
#         return res[0]

        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        return left if left else right
                