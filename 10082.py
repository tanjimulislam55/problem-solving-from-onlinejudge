rows = [
  "`1234567890-=",
  "QWERTYUIOP[]\\",
  "ASDFGHJKL;'",
  "ZXCVBNM,./"
]

# typed = []
# # typed = input()
# space = [" "]
# will_type = []

# def check_strings(argument):
#     for times in range(len(rows)): #looping in 0, 1, 2, 3
#         count = 0
#         for each in rows[times]:   #iterating every elements of specific block to each
#             count += 1
#             if each == argument:
#                 will_type.append(rows[times][count-2])
#
# for x in typed:
#     if " " == x:
#         will_type.append(" ")
#     check_strings(x)

# for i in will_type:
#     print(i, end='')

while True:
    try:
        typed = []
        typed = input()
        space = [" "]
        will_type = []
        def check_strings(argument):
            for times in range(len(rows)): #looping in 0, 1, 2, 3
                count = 0
                for each in rows[times]:   #iterating every elements of specific block to each
                    count += 1
                    if each == argument:
                        if each == 'A' or each == 'Z' or each == 'Q':
                            will_type.append(" ")
                        else:
                            will_type.append(rows[times][count-2])

        for x in typed:
            if " " == x:
                will_type.append(" ")
            check_strings(x)
        for i in will_type:
            print(i, end='')
        print('')
    except EOFError:
        break
