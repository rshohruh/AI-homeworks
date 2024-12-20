def is_prime(n: int) -> bool:
    a = [1 for i in range(2, n) if n % i == 0]
    return len(a) == 0

# print(is_prime(int(input())))