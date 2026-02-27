# import random as r
# with open('Файл 9.2', 'w') as f:
#     for _ in range(700):
#         f.write(f'{r.randint(1,9)} * {r.randint(1,9)}.{r.randint(1,9)}\n')

def Multiply(file):
    with open(file, 'r') as f_in:
        with open('Файл 9.2 з.txt', 'a') as f_out:
            for line in f_in:

                answer = str(int(line[0]) * int(line[4])) + '.' + str(int(line[0]) * int(line[6]))
                f_out.write(answer + '\n')
if __name__ == '__main__':
    Multiply('Файл 9.2')

