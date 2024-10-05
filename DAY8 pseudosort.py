def is_pseudo_sorted(arr, n):
    
    inversions = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            inversions += 1
            if inversions > 1:
                return False
   
    if inversions == 0:
        return True
    if inversions == 1:
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                return all(arr[j] <= arr[j + 1] for j in range(n - 1))
    return False

def process_test_cases():
    T = int(input()) 
    for _ in range(T):
        N = int(input())  
        A = list(map(int, input().split()))  
        
        if is_pseudo_sorted(A, N):
            print("YES")
        else:
            print("NO")

process_test_cases()
