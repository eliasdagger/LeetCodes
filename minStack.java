class MinStack {

    private int top;
    private int[] arr;
    private int[] minArr;

    public MinStack() {
        top = 0;
        arr = new int[30001];
        minArr = new int[30001];
    }
    
    public void push(int val) {
        arr[top] = val;
        if (top == 0) {
            minArr[top] = val;
        } else {
            minArr[top] = Math.min(val, minArr[top - 1]);
        }
        top++;
    }
    
    public void pop() {
        top--;
    }
    
    public int top() {
        return arr[top - 1];
    }
    
    public int getMin() {
        return minArr[top - 1];
    }
}

class MinStack {

    private int top;
	private int[] arr;

    public MinStack() {
        top = 0;
        arr = new int[0];

    }
    
    public void push(int val) {

        int[] temp = new int[top + 1];
        
        if (top == 0){
    		temp[top] = val;
    	}else {
    		for (int i = 0; i < temp.length - 1; i++){
                temp[i] = arr[i];
            }

            temp[temp.length - 1] = val;
    	}
        
        arr = temp;
        
        top++;
    }
    
    public void pop() {
        top--;

        int[] temp = new int[top];

        for (int i = 0; i < top; i++){
            temp[i] = arr[i];
        }

        arr = temp;
    }
    
    public int top() {
        return arr[top - 1];
    }
    
    public int getMin() {
        if (top == 0){
            return -1;
        }

        int min = arr[0];

        for (int i = 0; i < top; i++){
            if (arr[i] < min){
                min = arr[i];
            }
        }

        return min;
    }
}
