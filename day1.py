
def is_easy_to_pronounce(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consecutive_consonants = 0

    for char in word:
        if char not in vowels:  
            consecutive_consonants += 1
            if consecutive_consonants >= 4:   
                return "NO"
        else:
            consecutive_consonants = 0  
    return "YES"

def main():
    T = int(input())  
    for _ in range(T):
        N = int(input())  
        S = input().strip()  
        print(is_easy_to_pronounce(S))

if __name__ == "__main__":
    main()
