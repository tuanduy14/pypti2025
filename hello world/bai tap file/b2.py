with open('DaySoINP2.txt', 'r') as file:
    N = int(file.readline().strip())
    num = list(map(int, file.readline().strip().split()))

evnum = [N for N in num if N % 3 == 0]
kq= sum(evnum)

with open('DaySoOUT2.txt', 'w') as file_out:
    file_out.write(str(kq))