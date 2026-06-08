with open('UOCINO.txt','r') as file:
    n=int(file.readline().strip())

i=list(range(1,n+1))

with open('UOCOUT.txt','w') as file_out:
    file_out.write(' '.join(map(str,i)))
