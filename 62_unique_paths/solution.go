func uniquePaths(m int, n int) int {
    dp := make([][]int,0)
    for i:=0;i<m;i++ {
        dp = append(dp, make([]int,n))
    }
    dp[0][0] = 1
    for i :=0;i<m;i++ {
        for j:=0;j<n;j++ {
            if i==0 && j==0{
                continue
            }
            dp[i][j]=helper(i,j-1,&dp) + helper(i-1,j,&dp)
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