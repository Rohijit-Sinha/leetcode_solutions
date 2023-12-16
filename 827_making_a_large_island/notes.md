https://leetcode.com/problems/making-a-large-island

We use a Disjoint set.
Go through each grid with value 1 and connect it to nearby grids with val 1.
Go through each grid with val 0 get the nearby grids with val 1. Get their parents and keep a set. This is because multiple neighbors could be from same component.
Add up the sizes of all parents in the set and add 1.
Keep max.
If final res == 0, it means there was no 0 to be flipped.