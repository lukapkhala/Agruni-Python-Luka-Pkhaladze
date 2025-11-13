def is_natural(n):
    return n > 0 and n % 1 == 0

while True:
    user_input = input("Enter a natural number: ")
    if user_input.isdigit():
        n = int(user_input)
        if is_natural(n):
            break
        else:
            print("Please enter a valid natural number.")
    
    else:
        print("Please enter a valid natural number.")

if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    print("Yes")
else:
    print("No")