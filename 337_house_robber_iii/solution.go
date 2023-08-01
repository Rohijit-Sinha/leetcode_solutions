type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rob(root *TreeNode) int {
	val0, val1 := robImpl(root)
	return max(val0, val1)

}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func robFunc(root *TreeNode) (int, int) {
	if root == nil {
		return 0, 0
	}
	with_left, without_left := robImpl(root.Left)
	with_right, without_right := robImpl(root.Right)

	with := root.Val + left1 + right1
	without := max(with_left, without_left) + max(with_right, without_right)
	return with, without
}