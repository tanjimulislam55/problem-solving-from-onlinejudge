lines = int(input())

frequency = {} #empty dictionary
for x in range(lines):
    sentense = input()
    sentense = sentense.split()
    country = sentense[0]
    # woman = ' '.join(sentense[1:]) #converting list into string
    if country in frequency:
        frequency[country] += 1
    else:
        frequency[country] = 1

for each in sorted(frequency):
    print(f"{each} {frequency[each]}")
