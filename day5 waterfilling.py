
T = int(input())

for _ in range(T):
  
    B1, B2, B3 = map(int, input().split())
    
    empty_bottles = 3 - (B1 + B2 + B3)
    
    if empty_bottles >= 2:
        print("Water filling time")
    else:
        print("Not now")
