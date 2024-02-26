def is_perfect_number(num):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num

num = int(input("Введите натуральное число: "))
if is_perfect_number(num):
    print(f"Число {num} совершенное.")
else:
    print(f"Число {num} не совершенное.")
