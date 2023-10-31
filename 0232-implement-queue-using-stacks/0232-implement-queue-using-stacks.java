class MyQueue {
    Stack<Integer> left = new Stack();
    Stack<Integer> right = new Stack();
    public MyQueue() {
    }
    
    public void push(int x) {
        left.push(x);
    }
    
    public int pop() {
        int temp = peek();
        right.pop();
        return temp;
    }
    
    public int peek() {
        if(right.isEmpty()) {
            while(!left.isEmpty()) {
                right.push(left.pop());
            }
        }
        return right.peek();
    }
    
    public boolean empty() {
        return left.empty() && right.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */