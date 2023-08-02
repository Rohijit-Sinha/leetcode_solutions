type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findBottomLeftValue(root *TreeNode) int {
	queue := []*TreeNode{root}
	var left_most *TreeNode
	var queue_len int
	for len(queue) > 0 {
		count := len(queue)
		var node *TreeNode
		for i := 0; i < count; i++ {
			node = queue[i]
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
		}
		queue_len = len(queue)
		left_most = queue[queue_len-1]
		queue = queue[count:queue_len]
	}
	return left_most.Val
}