test_case = int(input())

for x in range(test_case):
    my_list = input().split()

    length = len(my_list)
    i = 0
    j = 1
    while length > 1:
        if my_list[i][1] != my_list[j][0]:
            temp = 1
        else:
            temp = 0
            break
        i += 1
        j += 1
        length -= 1
    for each_element in my_list:
        if each_element == my_list[-1]:
            if each_element[1] == my_list[0][1]:
                temp = 0
                break
    for each in range(len(my_list)):
        if each == len(my_list)
    print("LOOP" if temp == 1 else "NO LOOP")




# test_case = int(input())
#
# for test in range(test_case):
#     my_string = input().split()
#     i = 0
#     j = -1
#     for x in range(len(my_string)):
#         if my_string[i][0] != my_string[j][1]:
#             temp = 0
#         else:
#             temp = 1
#         i += 1
#         j += 1
#     print("LOOP" if temp == 0 else "NO LOOP")



# test_case = int(input())
#
# for test in range(test_case):
#     f_cntr = 0
#     m_cntr = 0
#     my_list = str(input()).split()
#     my_string = ''.join(my_list)
#
#     for x in my_string:
#         if x == "F":
#             f_cntr += 1
#         if x == "M":
#             m_cntr += 1
#     print("LOOP" if f_cntr == m_cntr else "NO LOOP")




# # # accepted solution
# test_cases = int(input())
#
#
# for test in range(test_cases):
#   diff = 0
#   num_tracks = 0
#
#   tracks = list(map(str, input().split()))
#   for track in tracks:
#     if track == "MM":
#       diff += 1
#     elif track == "FF":
#       diff -= 1
#     num_tracks += 1
#
#   print("LOOP" if diff == 0 and num_tracks > 1 else "NO LOOP")
