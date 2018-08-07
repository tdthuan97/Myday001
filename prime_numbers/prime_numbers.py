def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


x = int(input("Let's print the prime numbers up to? "))
for i in range(2, x+1):
    if bool(is_prime(i)):
        print(i)
