test_cases = int(input())

for x in range(test_cases):
  nums = list(map(int, input().split()))
  print(f"Case {x + 1}: {max(nums)}")
