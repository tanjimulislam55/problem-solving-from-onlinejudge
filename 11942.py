test_cases = int(input())
print("Lumberjacks:")

for x in range(test_cases):
    nums = list(map(int, input().split()))
    m = n = 0
    to_be_looped = len(nums) - 1

    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            m += 1
        if nums[i + 1] < nums[i]:
            n += 1

    print("Ordered" if m == to_be_looped or n == to_be_looped else "Unordered")
