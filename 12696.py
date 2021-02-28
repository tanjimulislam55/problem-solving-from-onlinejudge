test_cases = int(input())
total_allowed = 0

for x in range(test_cases):
    values = list(map(float, input().split()))

    if (values[0] <= 56 and values[1] <= 45 and values[2] <= 25 or (values[0] + values[1] + values[2]) <= 125) and values[3] <= 7:
        print("1")
        total_allowed += 1
    else:
        print("0")

print(total_allowed)
