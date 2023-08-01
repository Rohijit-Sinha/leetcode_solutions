Assuming
```
        3
       / \
      2   3
       \   \
        3   1
```
Thinking recursively,
If we include the money in a house, we cannot include money in a child house.
If we don't steal from a house, we can take money from its child.
Since we want to maximise, we will take the money from the left child and right child.
There can be two different amount from each branch, (with, without). We will return the total money stolen with or without current house.