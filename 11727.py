test_case = int(input())

for x in range(test_case):
    wages = list(map(int, input().split()))
    total = sum(wages)

    max_wage = 0
    if wage[0] > wage[1] and wage[0] > wage[2]:
        max_wage = wage[0]
    elif wage[1] > wage[2]:
        max_wage = wage[1]
    else:
        max_wage = wage[2]

    min = 0
    if wage[0] < wage[1] and wage[0] < wage[2]:
        min = wage[0]
    elif wage[1] < wage[2]:
        min = wage[1]
    else:
        min = wage[2]

    # max_wage = max(wages)
    # min_wage = min(wages)

    print(f"Case {x + 1}: {total - min_wage - max_wage}")
