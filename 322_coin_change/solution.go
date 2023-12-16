func coinChange(coins []int, amount int) int {
    dp:=make([][]int,0)
    for i:=0;i<len(coins);i++{
        tmp:=make([]int,amount+1)
        for j:=0;j<amount+1;j++{
            tmp[j]=-1
        }
        dp=append(dp,tmp)
    }
    for t:=0;t<amount+1;t++{
        if t % coins[0] == 0{
            dp[0][t] = t/coins[0]
        }else{
            dp[0][t]=int(1e9)
        }
    }
    for i:=1;i<len(coins);i++{
        for t:=0;t<amount+1;t++{
            nottake:=0+dp[i-1][t]
            take:=int(1e8)
            if coins[i]<=t{
                take=1+dp[i][t-coins[i]]
            }
            dp[i][t] = min(nottake,take)
        }
    }
    if dp[len(coins)-1][amount] > amount{
        return -1
    }else{
        return dp[len(coins)-1][amount] 
    }
}


func helper(idx int, tgt int,coins *[]int, dp *[][]int) int{
    if (*dp)[idx][tgt] != -1{
        return (*dp)[idx][tgt]
    }
    if idx == 0{
        if tgt % (*coins)[0] == 0{
            return tgt / (*coins)[0]
        }else{
            return 1e8
        }
    }
    nottake:=0+helper(idx-1,tgt,coins,dp)
    take:=int(1e8)
    if (*coins)[idx]<=tgt{
        take=1+helper(idx,tgt-(*coins)[idx],coins,dp)
    }
    (*dp)[idx][tgt] = min(nottake,take)
    return (*dp)[idx][tgt]
}

func min(a,b int)int{
    if a<b{
        return a
    }else{
        return b
    }
}