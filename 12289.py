test_case = int(input())

for test in range(test_case):
    word = input()

    if len(word) == 5:
        print("3")
    else:
        match_w_1 = match_w_2 = 0

        if word[0] == 'o':
            match_w_1 += 1
        if word[1] == 'n':
            match_w_1 += 1
        if word[2] == 'e':
            match_w_1 += 1

        if word[0] == 't':
            match_w_2 += 1
        if word[1] == 'w':
            match_w_2 += 1
        if word[2] == 'o':
            match_w_2 += 1

        if match_w_1 >= 2:
            print("1")
        elif match_w_2 >= 2:
            print("2")
