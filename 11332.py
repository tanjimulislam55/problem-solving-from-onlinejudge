while True:
    n = input()
    if n == '0':
        break;

    while len(n) > 1:   #'123'
        n = list(n)     #['1', '2', '3']
        conv = [int(a) for a in n] #[1, 2, 3]
        num = sum(conv) #6
        n = str(num)    #'6'
    if len(n) == 1:
        print(n)
    else:
        print(num)
