https://leetcode.com/problems/binary-search-tree-iterator

Simple solution is to do inorder traversal.
We can do so in constructor.

Another solution is to do iterative inorder in constructor.
In constructor, add to stack.
Again when getting val, if current node is not none, add to stack.