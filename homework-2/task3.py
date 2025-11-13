import random as rand

random_list = []

for i in range(5):
    random_list.append(rand.randint(1,4))

output_list = []

for number in random_list:
    for _ in range(number):
        output_list.append(number)

print("Random List:", random_list)
print("Output List:", output_list)
