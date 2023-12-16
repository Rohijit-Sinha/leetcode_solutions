func canPartition(nums []int) bool {
    target := sum(nums)
    if target % 2 == 1{
        return false
    }
    dp := make([][]int,0)
    for i:=0;i<len(nums);i++{
        tmp := make([]int,target)
        for i:=range(tmp){
            tmp[i]=-1
        }
        dp = append(dp,tmp)
    }
    return targetSum(len(nums)-1,&nums,target/2,&dp)
}

func targetSum (idx int,arr *[]int,target int,dp *[][]int) bool {
    if target==0{
        return true
    }
    if idx == 0{
        return (*arr)[0] == target
    }
    if (*dp)[idx][target] != -1 {
        return (*dp)[idx][target] != 0
    }
    nottake := targetSum(idx-1,arr,target,dp)
    take:=false
    if (*arr)[idx] < target {
        take = targetSum(idx-1,arr,target-(*arr)[idx],dp)
    }
    if nottake || take {
        (*dp)[idx][target] = 1
    }else{
        (*dp)[idx][target] = 0
    }
    return (*dp)[idx][target] != 0
}

func sum(nums []int) int{
    tot := 0
    for _,num:=range(nums) {
        tot = tot+num
    }
    return tot
}