Assuming bst [1,2,3,4,5,6,7], and range(3,5), we can observe the following:
- at 4 (root of bst), val is between low and high, therefore root will be in final bst and may have left and right.
- at 2 (left of 4), it is < low. There is no way anything left of 2 will be in final tree, so we can discard 2.left.
- at 6 (right of 4), it is > high. Thus, anything right of it will not be in the final.
- At both 2 and 6, since they are outside (low,high), we will not include them but there children might be included in final. Therefore we call the function recursively on them and return that instead.