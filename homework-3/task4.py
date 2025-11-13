keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

def encrypt(char):
    for row in keyboard:
        if char in row:
            index = row.index(char)
            return row[(index + 1) % len(row)]
    return char

def decrypt(char):
    for row in keyboard:
        if char in row:
            index = row.index(char)
            return row[(index - 1) % len(row)]
    return char


while True:
    action = input("Enter action (e/d): ").lower()
    if action in ("e", "d"):
        break
    print("Invalid action, try again.")

text = input("Enter text: ")


result = ""

for ch in text:
    if action == "e":
        result += encrypt(ch)
    else:
        result += decrypt(ch)


print(result)