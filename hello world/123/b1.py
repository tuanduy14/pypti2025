n=int(input())
num=list(map(int,input().split()))
with open('DaySoINP.txt','w') as file:
    file_in.write(f'{n}\n')
    file_in.write(''.join(map(str,num))+'\n')
with open('DaySoINP.txt','r') as file:
    n= int(file_in.readline().strip())
    num=list(map(int,file_in.readline().strip().split()))
evnum= [N for N in num if num % 2 ==0]
with open('DaySoOUT.txt','w') as file_out:
    file_out.write(''.join(map(str,evnum)))