t = int(input())

for i in range(t):
    n = int(input())

    n *= 567
    n //= 9
    n += 7492
    n *= 235
    n //= 47
    n -= 498
    #the question was unclear about the second digit choice
    if n < 0:
        n *= -1

    n //= 10
    n %= 10

    print(n)
