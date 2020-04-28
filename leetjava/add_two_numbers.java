class MyQueue {
    
    // initialize stack
    Stack stack;
    // initialize counter
    int start = 0;

    /** Initialize your data structure here. */
    public MyQueue() {
        
        // instanciate stack
        stack = new Stack<Integer>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        stack.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        return (int)stack.get(start++);
    }
    
    /** Get the front element. */
    public int peek() {
        return (int)stack.get(start);
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stack.size() == start + 1 ? false:true;
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