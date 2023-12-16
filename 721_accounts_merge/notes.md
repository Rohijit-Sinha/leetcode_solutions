https://leetcode.com/problems/accounts-merge

Use a disjoint set.
We will check if a mail in current index of account has already been encountered(keep a mapping of mail->idx). If it has, union in disjoint set.
Once this is done, go through each mail->idx map and add mail to its parent in a new map.
Once that is done, go through new map to create a res list.

This solution works because we create a graph with Disjoint set to assign a mail as parent if it was already encountered, 
forming connected components in the process.