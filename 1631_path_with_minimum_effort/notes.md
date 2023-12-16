https://leetcode.com/problems/path-with-minimum-effort/

We will use djikstra's algo.
Instead of distance array, we will maintain effort grid. We will store max of efforts we have encountered so far.
If we reach the end, return the effort at the end.