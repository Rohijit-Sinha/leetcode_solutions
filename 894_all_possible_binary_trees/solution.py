from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # tree_map will allow us to store the already solved combinations
        tree_map = {}
        def helper(n):
            # It is impossible to build full binary tree with even number 
            # of nodes 
            if n % 2 == 0:
                return []
            if n == 1:
                return [TreeNode()]
            if n in tree_map:
                return tree_map[n]
            res = []
            for l in range(n):
                r = n - l - 1
                # we will recurse for values of l and r
                leftTrees, rightTrees = helper(l), helper(r)

                # if eg.n==5, 2 lefttrees and two righttrees are possible
                # we have to try out each possibility
                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0,t1,t2))
            tree_map[n]=res
            return res
        return helper(n)