hello_dict = {
  "HELLO": "ENGLISH",
  "HOLA": "SPANISH",
  "HALLO": "GERMAN",
  "BONJOUR": "FRENCH",
  "CIAO": "ITALIAN",
  "ZDRAVSTVUJTE": "RUSSIAN"
}

case = 1
while True:
  word = input()

  if word == "#":
    break

  if word in hello_dict:
    print(f"Case {case}: {hello_dict[word]}")
  else:
    print(f"Case {case}: UNKNOWN")

  case += 1
