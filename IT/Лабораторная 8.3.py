def reversed_digits(n):
    if n < 10:
        print(n)
    else:
        print(n%10 , " ")
        reversed_digits(n//10)
print(reversed_digits(1234567))