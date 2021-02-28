case = 1
while True:
    word = input()
    if word == "*":
        break
    print(f"Case {case}: ", end='')
    print("Hajj-e-Akbar" if word == "Hajj" else "Hajj-e-Asghar")
    case += 1
