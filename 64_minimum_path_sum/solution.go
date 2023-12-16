func minPathSum(grid [][]int) int {
    m,n := len(grid), len(grid[0])
    dp := make([][]int,0)
    for i:=0;i<m;i++ {
        dp = append(dp, make([]int,n))
    }
    dp[0][0] = grid[0][0]
    for i:=0;i<m;i++{
        for j:=0;j<n;j++ {
            if i==0 && j==0{
                continue
            }
            minimum := min(helper(i-1,j,&dp),helper(i,j-1,&dp))
            dp[i][j]= grid[i][j] + minimum
        }
    }
    return dp[m-1][n-1]
}

func helper(i int,j int,dp *[][]int) int {
    if i < 0 || j<0 {
        m := ^uint(0)
        return int(m>>1)
    }
    return (*dp)[i][j]
}

func min(a, b int) int{
    if a<b{
        return a
    }else{
        return b
    }
}