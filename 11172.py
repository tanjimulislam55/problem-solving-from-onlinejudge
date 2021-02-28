t = int(input())
for test in range(t):
    num1, num2 = input().split()
    num1 = int(num1) #converting str into int
    num2 = int(num2) #converting str into int
    # num1, num2 = list(map(int, input().split())) #instead we could write this
    print("<" if num1 < num2 else ">" if num1 > num2 else "=")
