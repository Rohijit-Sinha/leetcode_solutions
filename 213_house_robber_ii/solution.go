func rob(nums []int) int {
    if len(nums) < 2 {
        return nums[0]
    }
    tmp_slice := nums[0:len(nums)-1]
    with_first := helper(tmp_slice)
    tmp_slice = nums[1:len(nums)]
    with_last:=helper(tmp_slice)
    return max(with_first,with_last) 
}

func helper(nums []int) int {
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

func max(num1, num2 int) int {
    if num1 > num2 {
        return num1
    }else {
        return num2
    }
}