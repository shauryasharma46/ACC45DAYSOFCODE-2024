def determine_rank(dragon_scores, sloth_scores):
    dragon_total = sum(dragon_scores)
    sloth_total = sum(sloth_scores)
    
    if dragon_total > sloth_total:
        return "Dragon"
    elif sloth_total > dragon_total:
        return "Sloth"
    
    if dragon_scores[0] > sloth_scores[0]:
        return "Dragon"
    elif sloth_scores[0] > dragon_scores[0]:
        return "Sloth"
    
    if dragon_scores[1] > sloth_scores[1]:
        return "Dragon"
    elif sloth_scores[1] > dragon_scores[1]:
        return "Sloth"
    
    return "Tie"

T = int(input())

for _ in range(T):
    dragon_scores = list(map(int, input().split()))
    sloth_scores = list(map(int, input().split()))
    
    result = determine_rank(dragon_scores, sloth_scores)
    print(result)

