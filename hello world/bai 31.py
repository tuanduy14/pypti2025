a,k,n = map(int,input().split())
b = []
st = k-(a%k)
end = n-a
while st<=end:
    b.append(str(st))
    st+=k
if(len(b)==0):
    print(-1)
else:
    print(' '.join(b))