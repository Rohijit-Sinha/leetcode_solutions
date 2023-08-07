https://leetcode.com/problems/implement-trie-prefix-tree

In a Trie, each node has multiple children.
For eg. if "apple" is saved in trie, The path will be "a" -> "p" -> "p" -> "l" -> "e".
If a new word "ape" is stored, it will use the existing "a" and "p" nodes and continue with new "e" node which would be a child of first "p" of "apple".

Thus, for every node we will have multiple children.
We will also keep track of endOfWord at every node, so that we know if a word has terminated on that node.