https://leetcode.com/problems/minimum-path-sum/

We use a recursive solution with DP.
Get minimum of paths to get to a cell and store its sum with cell value in a dp ds.

For tabulation, we can just start from [0][0].

For space optimization, we just need to store current row and previous row.