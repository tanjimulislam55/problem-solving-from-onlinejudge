###unfinished
import operator
lines = int(input())

alph_dict = {} #empty dictionary
for x in range(lines):
    # alphabets = list(map(str, 'QWERTYUIOPLKJHGFDSAZXCVBNM'))
    alphabets = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
    sentence = input().upper().replace(" ", "") #replacing spaces by no spaces

    for x in sentence:
        if x in alph_dict:
            alph_dict[x] += 1
        else:
            alph_dict[x] = 1

# for i in sorted(alph_dict):
#     if i in alphabets:
#         print(i, alph_dict[i])


# sorted_alph_dict = sorted(alph_dict.items(), key = operator.itemgetter(1), reverse=True)
# for i in sorted_alph_dict:
#     print(sorted_alph_dict)
#     if i in alphabets:
#         print(i, alph_dict[i])

# sorted_alph_dict = sorted(alph_dict.items(), key = operator.itemgetter(1), reverse=True)
# t = 0
# for i in sorted_alph_dict:
#     if sorted_alph_dict[t][0] in alphabets:
#         print(sorted_alph_dict[t][0], sorted_alph_dict[t][1])
#     t += 1

# sorted_alph_dict = sorted(alph_dict.items(), key = lambda x: (x[1], ord(x[0])), reverse=True)
# t = 0
# for i in range(len(sorted_alph_dict)):
#     if sorted_alph_dict[t][0] in alphabets:
#         print(sorted_alph_dict[t][0], sorted_alph_dict[t][1])
#     t += 1


sorted_alph_dict = sorted(alph_dict.items(), key = lambda x: x[1], reverse=True)
t = 0
for i in range(len(sorted_alph_dict)):
    if sorted_alph_dict[t][0] in alphabets:
        print(sorted_alph_dict[t][0], sorted_alph_dict[t][1])
    t += 1
