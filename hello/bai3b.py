def combinations(n, k):
    x = [0] * (k + 1)  # x[1..k], x[0] dùng làm mốc

    def backtrack(i):
        for v in range(x[i-1] + 1, n - k + i + 1):
            x[i] = v
            if i == k:
                print(x[1:k+1])
            else:
                backtrack(i + 1)

    backtrack(1)
