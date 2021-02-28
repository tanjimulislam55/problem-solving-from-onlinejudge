test_cases = int(input())

for test in range(test_cases):
    text = input()
    text = list(text)   #converting string to list

    a = text.count('A')
    i = text.count('I')
    t = text.count('T')
    r = text.count('R')
    m = text.count('M')
    g = text.count('G')

    print(min(a//3, r//2, g, i, t, m))
