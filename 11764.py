test_cases = int(input())

for x in range(test_cases):
    num_walls = int(input()) #8
    walls = list(map(int, input().split())) #1 4 2 2 3 5 3 4
    high = low = 0

    if len(walls) >= 2:
        for i in range(len(walls) - 1):
            if walls[i+1] > walls[i]:
                high += 1
            elif walls[i+1] < walls[i]:
                low += 1

    print(f"Case {x + 1}: {high} {low}")
