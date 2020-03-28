MAX = 1e9

def minJumps(arr, N): 
      
    fib = [0 for i in range(30)] 
    fib[0] = 0
    fib[1] = 1
    for i in range(2, 30): 
        fib[i] = fib[i - 1] + fib[i - 2] 

    DP = [0 for i in range(N + 2)] 
  
    # Base case (Steps to reach source is) 
    DP[0] = 0
  
    for i in range(1, N + 2):  
        for j in range(1, 30): 
            if ((arr[i - 1] == 1 or i == N + 1) and 
                                    i - fib[j] >= 0): 
                DP[i] = min(DP[i], 1 + DP[i - fib[j]]) 
    if (DP[N + 1] != MAX): 
        return DP[N + 1] 
    else: 
        return -1
        
arr = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0] 
n = len(arr) 
  
print(minJumps(arr, n - 1)) 
