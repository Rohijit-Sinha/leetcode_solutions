https://leetcode.com/problems/coin-change/

We can solve using recursion with index and target.
If we take a coin, the next recursion will be on same index since we can take a coin any number of time.
For base case, we have to make sure a remaining target is divisble by coin[0].
