while True:
    ch = list(map(int, input().split()))

    if ch[0] == ch[1] == -1:
        break
    if ch[1] > ch[0]:
        ch_from = ch[0]
        ch_to = ch[1]
        ping_pos = ch_to - ch_from

        if ch_from > 0:
            ping_down = ch_from
        else:
            ping_down = 0
        pin_up = 100 - ch_to
        ping_neg = pin_up + ping_down

    if ch[0] > ch[1]:
        ch_from = ch[0]
        ch_to = ch[1]
        ping_pos = ch_to - ch_from

        if ch_from > 0:
            ping_down = ch_from
        else:
            ping_down = 0
        pin_up = 100 - ch_to
        ping_neg = pin_up + ping_down

    print(min(abs(ping_pos), abs(ping_neg)))




# # # accepted solution (unexpected wrong ans of mine, so)
# while True:
#     ch_from, ch_to = list(map(int, input().split()))
#
#     if ch_from == ch_to == -1:
#       break
#
#     ping_up = ch_to - ch_from
#     ping_down = ch_from - ch_to
#
#     if ping_up < 0:
#       ping_up += 100
#
#     if ping_down < 0:
#       ping_down += 100
#
#     print(min(ping_down, ping_up))
