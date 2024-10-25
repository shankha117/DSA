// https://leetcode.com/problems/min-stack/description/

type MinStack struct {

    st []int
    minSt []int

}


func Constructor() MinStack {

    return MinStack{
        st : []int{},
        minSt: []int{},
    }
}

func (this *MinStack) Push(val int)  {

    this.st = append(this.st, val)

    if len(this.minSt) == 0 || val <= this.GetMin() {
        this.minSt = append(this.minSt, val)
    }
}

func (this *MinStack) Pop()  {

    // Pop the top element from the stack
	topElement := this.st[len(this.st)-1]
	this.st = this.st[:len(this.st)-1]

    if topElement == this.minSt[len(this.minSt) -1 ]{
        this.minSt = this.minSt[:len(this.minSt)-1]
    }

}

func (this *MinStack) Top() int {
    return this.st[len(this.st) -1]
}

func (this *MinStack) GetMin() int {
    return this.minSt[len(this.minSt) -1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
