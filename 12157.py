from math import ceil
test_cases = int(input())

for x in range(test_cases):
    test = int(input())
    duration = list(map(int, input().split()))

    def mile_cost(value):
        return ceil((value+1)/30) * 10   #value+1 because when value is 30 it should be 31 to get greater value of 0 to make costing for 10 cents of 30 seconds and so on
    mile = sum(map(mile_cost, duration))

    juice = sum(map(lambda value: ceil((value+1)/60) * 15, duration)) #less code than mile

    if mile < juice:
        print(f"Case {x+1}: Mile {mile}")
    elif juice < mile:
        print(f"Case {x+1}: Juice {juice}")
    else:
        print(f"Case {x+1}: Mile Juice {mile}")
