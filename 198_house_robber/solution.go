// Recursion
func rob(nums []int) int {
    var mem = map[int]int{}
    last := len(nums) - 1
    return helper(&nums, last, &mem)
}

func helper(arr_ptr *[]int,idx int, mem_ptr *map[int]int) int {
    if idx == 0 {
        return (*arr_ptr)[0]
    }else if idx < 0 {
        return 0
    }
    if val,ok:=(*mem_ptr)[idx];ok {
        return val
    }
    pick := (*arr_ptr)[idx] + helper(arr_ptr, idx-2, mem_ptr)
    no_pick := helper(arr_ptr, idx-1, mem_ptr)
    res := max(pick, no_pick)
    (*mem_ptr)[idx] = res
    return res
}

func max(num1, num2 int) int {
    if num1 > num2 {
        return num1
    }else {
        return num2
    }
}


// tabulation

func rob(nums []int) int {
    arr_len := len(nums)
    dp := make([]int, arr_len)
    dp[0] = nums[0]
    for i:=1;i<arr_len;i++ {
        pick := nums[i]
        if i>1 {
            pick = pick + dp[i-2]
        }
        no_pick := dp[i-1]
        dp[i] = max(pick,no_pick)
    }
    return dp[arr_len-1]
}


// Space optimised

func rob(nums []int) int {
    arr_len := len(nums)
	two_back := 0
	one_back := nums[0]
    for i:=1;i<arr_len;i++ {
        pick := nums[i]
        if i>1 {
            pick = pick + two_back
        }
        no_pick := one_back
		two_back = one_back
		one_back = max(pick,no_pick)
    }
    return one_back
}
