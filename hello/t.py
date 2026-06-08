def tohop(n,k):
    x=[0]*(k+1)

    def quayLui(i, x=None):
        for r in range(x[i-1],n-k+i+1):
            x=[r]
            if r == k:
                print(x[1:k+1])
            else:
                quayLui(i+1)

    quayLui(1)