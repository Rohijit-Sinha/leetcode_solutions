https://leetcode.com/problems/all-possible-full-binary-trees/

Assuming a tree [0,1,2,3,4,5,6]. Let us start with the assumption that we are at node 3.
- On the left we have the possibility of using 3 nodes in any config that makes it full binary tree.
- On the right we have the possibility of using 3 nodes in any config that makes it full binary tree.
- That means, if we have two possible combination on the left and two on the right, ([t1,t2] and [t3,t4]), our current node can have them in any possible config nd it will be a full binary tree.
eg. 
```
        root          root            root              root
         / \           / \             / \               / \
        t1  t3        t2  t4          t1  t4            t2  t3
```
- The total number of combination would be l_comb x r_comb.
- If we want all possible combination, we will have to go through each possible combination of left and right for a given number of nodes and see if they can form a full binary tree.
- We will then have to get possible combination of left and right for each combination of number of nodes.