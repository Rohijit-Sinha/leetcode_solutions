func minimumTotal(triangle [][]int) int {
    rows := len(triangle)
    dp:=make([][]int,0)
    for i:=0;i<rows;i++ {
        dp = append(dp,make([]int,i+1))
    }
    dp[0][0]=triangle[0][0]
    for i:=1;i<rows;i++{
        for j:=0;j<len(triangle[i]);j++ {
            sum := min(helper(i-1,j,&dp,&triangle),helper(i-1,j-1,&dp,&triangle))
            dp[i][j] = triangle[i][j] + sum
        }
    }
    res := int(1e9)
    for _,num := range dp[rows-1] {
        res = min(res,num)
    }
    return res
}

func helper(i int, j int, dp *[][]int, tri * [][]int) int{
    curLen := len((*tri)[i])
    if j < 0 || j >= curLen {
        return 1e9
    }else{
        return (*dp)[i][j]
    }
}

func min (a,b int)int {
    if a<b{
        return a
    }else{
        return b
    }
}