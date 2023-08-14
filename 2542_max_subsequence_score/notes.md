https://leetcode.com/problems/maximum-subsequence-score/

First sort the pairs of (num1,num2) according to num2.
We have to multiply sum from first arr with min of second array for given subseq of indexes.
It doesnt matter what the values in second arr are, since the minimum will remain same.
That means, we depend on having max sum from first arr.
eg. nums1 = [14, 2, 1, 12]
    nums2 = [13, 11, 7, 6]
Go through each and add num1 to total sum. If subseq reaches length k, pop smallest one and remove from sum.
This way total sum will always have elements count < k.
Use a heap for that.