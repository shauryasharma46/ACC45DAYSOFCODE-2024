def total_working_hours(X, Y):

    return 4 * X + Y


T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    print(total_working_hours(X, Y))

