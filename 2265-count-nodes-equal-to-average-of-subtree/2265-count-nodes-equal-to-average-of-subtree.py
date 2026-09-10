# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                # Returns: (total_sum, node_count, valid_matches)
                return 0, 0, 0
            
            l_sum, l_cnt, l_match = dfs(node.left)
            r_sum, r_cnt, r_match = dfs(node.right)
            
            curr_sum = node.val + l_sum + r_sum
            curr_cnt = 1 + l_cnt + r_cnt
            
            # 1 if current node matches its subtree average, else 0
            is_match = 1 if (curr_sum // curr_cnt) == node.val else 0
            
            return curr_sum, curr_cnt, l_match + r_match + is_match

        return dfs(root)[2]






# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def averageOfSubtree(self, root: TreeNode) -> int:
#         if not root:
#             return 0

#         matching_nodes = 0
        
#         # Dictionary to store (sum, count) for each subtree rooted at `node`
#         # Default for None child is (0, 0)
#         subtree_info = {None: (0, 0)}
        
#         # Stack for iterative post-order traversal: (node, processed_flag)
#         stack = [(root, False)]
        
#         while stack:
#             node, processed = stack.pop()
            
#             if not node:
#                 continue
                
#             if processed:
#                 # Both children have been processed; combine their statistics
#                 left_sum, left_count = subtree_info[node.left]
#                 right_sum, right_count = subtree_info[node.right]
                
#                 total_sum = node.val + left_sum + right_sum
#                 total_count = 1 + left_count + right_count
                
#                 if total_sum // total_count == node.val:
#                     matching_nodes += 1
                
#                 # Cache the results for parent nodes to access
#                 subtree_info[node] = (total_sum, total_count)
#             else:
#                 # Push back in reverse order for Post-Order Traversal (Left -> Right -> Root)
#                 stack.append((node, True))
#                 if node.right:
#                     stack.append((node.right, False))
#                 if node.left:
#                     stack.append((node.left, False))

#         return matching_nodes



# # # Definition for a binary tree node.
# # # class TreeNode:
# # #     def __init__(self, val=0, left=None, right=None):
# # #         self.val = val
# # #         self.left = left
# # #         self.right = right
# # class Solution:
# #     def averageOfSubtree(self, root: TreeNode) -> int:
# #         self.count_matching = 0
        
# #         def dfs(node):
# #             if not node:
# #                 return (0, 0)  # (sum, count)
            
# #             left_sum, left_count = dfs(node.left)
# #             right_sum, right_count = dfs(node.right)
            
# #             total_sum = node.val + left_sum + right_sum
# #             total_count = 1 + left_count + right_count
            
# #             # Use integer division (//) for rounding down to the nearest integer
# #             if total_sum // total_count == node.val:
# #                 self.count_matching += 1
                
# #             return (total_sum, total_count)
        
# #         dfs(root)
# #         return self.count_matching