with open('TBCINP2.txt', 'r') as file:
    n=int(file.readline().strip())

    with open('TBCOUT2.txt', 'w') as file_out:
        for i in range(n):
            day_so = list(map(int, file.readline().strip().split()))
            kq = sum(day_so) / len(day_so)
            file_out.write(f'{kq}\n')




