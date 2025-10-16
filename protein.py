T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    protein = 0
    day = -1
    A = list(map(int, input().split()))
    for i in range(N):
        if day == -1:
            protein += A[i]
            if protein < K:
                day = i + 1
            else:
                protein -= K
    if day == -1:
        print("YES")
    else:
        print("NO", day)
