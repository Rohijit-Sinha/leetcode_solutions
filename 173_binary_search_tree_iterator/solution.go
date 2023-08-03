// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

type Stack[T any] struct {
	list []*T
}

func (this *Stack[T]) Push(data *T) {
	this.list = append(this.list, data)
}

func (this *Stack[T]) Pop() *T {
	if len(this.list) > 0 {
		data := this.list[len(this.list)-1]

		this.list = this.list[:len(this.list)-1]

		return data
	}

	return nil
}

func (this *Stack[T]) Empty() bool {
	return len(this.list) == 0
}

type BSTIterator struct {
	root    *TreeNode
	curNode *TreeNode
	stack   Stack[TreeNode]
}

func Constructor(root *TreeNode) BSTIterator {
	return BSTIterator{
		root:    root,
		curNode: root,
		stack: Stack[TreeNode]{
			list: make([]*TreeNode, 0, 1),
		},
	}
}

func (this *BSTIterator) Next() int {
	nextVal := 0

	if this.curNode != nil {
		for this.curNode != nil {
			if this.curNode.Left != nil {
				this.stack.Push(this.curNode)
				this.curNode = this.curNode.Left
				continue
			}

			nextVal = this.curNode.Val
			this.curNode = this.curNode.Right
			break
		}
	} else {
		this.curNode = this.stack.Pop()
		nextVal = this.curNode.Val
		this.curNode = this.curNode.Right
	}

	return nextVal
}

func (this *BSTIterator) HasNext() bool {
	if this.curNode == nil && this.stack.Empty() {
		return false
	}

	return true
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
