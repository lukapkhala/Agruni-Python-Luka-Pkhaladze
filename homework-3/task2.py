input1 = input("Enter first string: ").lower()
input2 = input("Enter second string: ").lower()

dict1 = {}
dict2 = {}

for char in input1:
    dict1[char] = dict1.get(char, 0) + 1

for char in input2:
    dict2[char] = dict2.get(char, 0) + 1

answer = True
for char in dict2:
    if (not char in dict1) or (dict2[char ] > dict1[char]):
        answer = False
        break

if answer:
    print("Yes")
else:
    print("No")

        