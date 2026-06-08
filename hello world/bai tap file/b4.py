with open('TBCINP.txt', 'r') as file:
    n=int(file.readline().strip())

    num = []
    for i in file:
        num.append(int(i.strip()))

tb =  sum(num) / n

with open('TBCOUT.txt', 'w') as file_out:
    file_out.write(str(tb))