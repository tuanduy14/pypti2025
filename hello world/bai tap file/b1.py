with open('DaySoINP.txt', 'r') as file:
    N = int(file.readline().strip())
    num = list(map(int, file.readline().strip().split()))

evnum = [N for N in num if N % 2 == 0]

with open('DaySoOUT.txt', 'w') as file_out:
    file_out.write(' '.join(map(str, evnum)))