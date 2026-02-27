def AddLeftDigit(D,K):
    if D > 9 or D < 1:
        print('Введи нормально, брат')
    else:
        K = str(D) + str(K)
        return K
d1 = int(input('Введите d1 '))
d2 = int(input('Введите d2 '))
k = int(input('Введите число K '))

answer = AddLeftDigit(d1,k)
print(answer, AddLeftDigit(d2,answer))
