if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    unique_scores = list(set(arr))
    unique_scores.remove(max(unique_scores))
    print(max(unique_scores))