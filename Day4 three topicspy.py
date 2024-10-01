def can_win(A, B, C, X):
    
    if X == A or X == B or X == C:
        return "Yes"
    else:
        return "No"

A, B, C, X = map(int, input().split())

print(can_win(A, B, C, X))
