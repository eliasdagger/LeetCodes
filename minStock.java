class MinStack {

    public MinStack() {
        static int top = 0;
        int[] arr = new int[0];

    }
    
    public void push(int val) {
        top++;

        int[] temp = new int[top];

        for (i = 0; i < temp.length; i++){
            temp[i] = arr[i];
        }

        temp[temp.length - 1] = val;

        arr = temp;
    }
    
    public void pop() {
        top--;

        int[] temp = new int[top];

        for (i = 0; i < top; i++){
            temp[i] = arr[i];
        }

        arr = temp;
    }
    
    public int top() {
        return arr[top];
    }
    
    public int getMin() {
        if (top == 0){
            return null;
        }


        int min = arr[i];

        for (i = 0; i < top; i++){
            if (arr[i] < min){
                min = arr[i];
            }
        }

        return min;
    }

    public static void main(String[] args){
        MinStack minStack = new MinStack();
        minStack.push(1);
        minStack.push(2);
        minStack.push(0);
        minStack.getMin(); // return 0
        minStack.pop();
        minStack.top();    // return 2
        minStack.getMin(); // return 1
    }
}
