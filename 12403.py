test_case = int(input())
funds = 0

for x in range(test_case):
    donate = input().split()

    if len(donate) == 2:
        funds += int(donate[1])
    else:
        print(funds)
