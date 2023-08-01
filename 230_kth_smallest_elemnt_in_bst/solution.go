type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {
	stack := make([]*TreeNode, 0)
	cnt := 1
	var val int
	for len(stack) > 0 || root != nil {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		if len(stack) > 1 {
			stack = stack[:len(stack)-1]
		}
		if cnt == k {
			val = root.Val
			break
		}
		root = root.Right
		cnt++
	}
	return val
}