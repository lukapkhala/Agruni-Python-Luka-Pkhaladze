n = int(input("Enter natural number (<= 1000): "))

while n > 1000:
    n = int(input("Enter natural number (<= 1000): "))

s = ""
for i in range(1, n + 1):
    if n % i == 0:
        s += str(i) + ", "

s = s[:-2]  # Remove the trailing comma and space
print(f"Divisors of {n}: {s}") 

