t = int(input())
for i in range(0,t):
    N = int(input())
    S = list(map(int,input().split()))
    temp = 0
    for j in range(N-1):
        temp += (abs(S[j]-S[j+1])-1)
    print(temp)
