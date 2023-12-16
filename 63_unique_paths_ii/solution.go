func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    m,n := len(obstacleGrid), len(obstacleGrid[0])
    dp := make([][]int,0)
    for i:=0;i<m;i++ {
        dp = append(dp, make([]int,n))
    }
    for i:=0;i<m;i++ {
        for j:=0;j<n;j++ {
            if i==0 && j==0 {
                if obstacleGrid[0][0] == 0{
                    dp[0][0]=1
                }else{
                    break
                }
            }else if obstacleGrid[i][j] == 1{
                dp[i][j] = 0
            }else{
                dp[i][j]=helper(i,j-1,&dp) + helper(i-1,j,&dp)
            }
        }
    }
    return dp[m-1][n-1]
}

func helper(i int,j int,dp *[][]int) int {
    if i < 0 || j<0 {
        return 0
    }
    return (*dp)[i][j]
}