# import random
# with open('Файл 9.1.txt', 'w') as f:
#     for _ in range(50):
#         f.write('random number is ' + str(random.randint(10, 10000)) + '\n')
#
def CreateFile(file):
    with open(file, 'r') as f:
        with open('Файл 9.1 з.txt', 'w') as f2:
            first = f.readline()
            for line in f:
                if len(line) < len(first):
                    first = line
            f.seek(0)
            for line in f:
                if len(line) == len(first):
                    f2.write(line)
                    first = line
if __name__ == '__main__':
    CreateFile('Файл 9.1.txt')


