def factoriz(n, k=2, r=[]):
    if n == 1:
        result = '*'.join(map(str, r))
        return f"{num} = {result}"
    if n % k == 0:
        return factoriz(n // k, k, r + [k])
    else:
        return factoriz(n, k + 1, r)

num = int(input("Введите натуральное число: "))
result = factoriz(num)
print(result)
