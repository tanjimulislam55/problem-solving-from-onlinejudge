#incomplete
while True:
    length = int(input())
    if length == 0:
        break

    s = input()
    if "Z" in s:
        print(0)

    else:
        # r_found = 0
        # d_found = 0

        distance = 1
        positional_value_of_d = 0
        positional_value_of_r = 0

        for x in range(len(s)):

            if s[x] == "R":
                positional_value_of_r = x
                if positional_value_of_d > positional_value_of_r:
                    distance = positional_value_of_d - positional_value_of_r
                else:
                    distance = positional_value_of_r - positional_value_of_d
                # if distance < min_distance:
                min_distance = distance
                # r_found += 1
                # last_r = s[i]
            if s[x] == "D":
                positional_value_of_d = x
                if positional_value_of_r > positional_value_of_d:
                    distance = positional_value_of_r - positional_value_of_d
                else:
                    distance = positional_value_of_d - positional_value_of_r
                # if distance < min_distance:
                min_distance = distance
                # d_found += 1
                # last_d = s[j]
                # print(distance)

        print(min_distance)



# # # solution
# while True:
#   length = int(input())
#   if length == 0:
#     break
#
#   s = input()
#   r = -1
#   d = -1
#
#   min_distance = 2000000
#   for i, ch in enumerate(s):
#     if ch == 'Z':
#       min_distance = 0
#       break
#     if ch == 'R':
#       r = i
#       if d != -1:
#         if i - d < min_distance:
#           min_distance = i - d
#     if ch == 'D':
#       d = i
#       if r != -1:
#         if i - r < min_distance:
#           min_distance = i - r
#
#   print(min_distance)
