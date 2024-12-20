num = int(input("Enter a positive integer: "))

[print(f"{i} is a factor of {num}") for i in range(1, num + 1) if num % i == 0]
