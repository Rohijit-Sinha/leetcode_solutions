https://leetcode.com/problems/find-bottom-left-tree-value/

At first look, we can tell that this is a BFS problem.
One thing to note is that if we traverse left -> right, we will have to keep track of first element in every traversal.
We can solve it by traversing right -> left.