n = int(input("Enter natural number (<= 100): "))

while n > 100:
    n = int(input("Enter natural number (<= 100): "))

f1 = 0
f2 = 1

list = []

for i in range(n):
    list.append(f1)
    f_next = f1 + f2
    f1 = f2
    f2 = f_next


print(f"First {n} Fibonacci numbers: {list}")