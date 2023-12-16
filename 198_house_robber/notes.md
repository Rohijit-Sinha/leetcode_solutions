https://leetcode.com/problems/house-robber

We will use the simple recursive method of pick/non-pick.

For tabulation, we can just start from base case of dp[0]=arr[0] and then move forward index by index.

For space optimisation, we notice that for calculating dp[i], we only need dp[i-1] and dp[i-1].
Yhus, we can just store dp[i-1] and dp[i-2] and discard the rest.