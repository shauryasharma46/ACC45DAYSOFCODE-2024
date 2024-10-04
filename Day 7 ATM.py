def atm_withdrawals(test_cases):
    for case in test_cases:
        N, K = case['N'], case['K']
        withdrawals = case['withdrawals']
        result = ""
        for withdrawal in withdrawals:
            if K >= withdrawal:
                result += "1"
                K -= withdrawal
            else:
                result += "0"
        print(result)

T = int(input())  
test_cases = []

for _ in range(T):
    N, K = map(int, input().split())
    withdrawals = list(map(int, input().split()))
    test_cases.append({'N': N, 'K': K, 'withdrawals': withdrawals})

atm_withdrawals(test_cases)

