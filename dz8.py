def aln(n):
    if n == 1:
        return 1
    else:
        a = 0
        for i in range(1, n + 1):
            a += aln(n - i)
        return a

N = int(input("Введите натуральное число: "))
print(f"Количество разложений: {aln(N)}")
