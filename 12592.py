N = int(input())
slogans = {}

for x in range(N):
    first = input()
    second = input()
    slogans[first] = second

Q = int(input())

for i in range(Q):
    ditc_item = input()
    print(f"{slogans[ditc_item]}")
