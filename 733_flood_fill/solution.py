from typing import List
import collections

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initColor = image[sr][sc]

        def check(i,j):
            nonlocal initColor
            if i<0 or j<0 or i>=len(image) or j>=len(image[0]):
                return False
            if image[i][j] != initColor:
                return False
            return True

        def dfs(i,j):
            image[i][j] = color
            if check(i-1,j):
                dfs(i-1,j)
            if check(i+1,j):
                dfs(i+1,j)
            if check(i,j-1):
                dfs(i,j-1)
            if check(i,j+1):
                dfs(i,j+1)
        
        dfs(sr,sc)
        return image