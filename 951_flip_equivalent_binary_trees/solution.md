https://leetcode.com/problems/flip-equivalent-binary-trees/

Takning example root1 = [1,2,3,4,5,6,null,null,null,7,8] and root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
We can make a few observations:
- If at any point both root are nil, we can return True since nil trees are equiv.
- If value if the current root in both trees is not same, they cannot be flip eqiv.
- We can say two node is equivalent when is children are also equivalent.
- Check that either (root.left and root.right are same for both root1 and root2) OR (root1.left with root2.right and root1.right with root2.left).