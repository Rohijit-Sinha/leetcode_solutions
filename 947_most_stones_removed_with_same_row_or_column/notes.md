https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

We use a disjoint set.
We will set u as row of stone and v as col of a stone.
col will start from last row + 1. So a col will be col + maxRow + 1.
eg. row = 5 and cols 4, the nodes will be
    0,1,2,3,4|5,6,7,8
This is because, 

(1,1) and (1,3). Since both stones are on same row, pushing into disjoint set will result in (1,6) first and then (1,8).
Col values 6 and 8 will become related by row node 1.