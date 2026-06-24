def dailyTemperatures(temperatures):
    res = []
    s = []
    for i in range(len(temperatures)):
        if temperatures[-i - 1] < temperatures[i]:
            s.append(temperatures.pop())
        
            
        

