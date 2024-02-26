# Проверка для ладьи
def is_rook_move(a, b, c, d):
    return a == c or b == d

# Проверка для слона
def is_bishop_move(a, b, c, d):
    return abs(a - c) == abs(b - d)

# Проверка для ферзя (ферзь может ходить как ладья и слон)
def is_queen_move(a, b, c, d):
    return is_rook_move(a, b, c, d) or is_bishop_move(a, b, c, d)

# Проверка для коня
def is_knight_move(a, b, c, d):
    return (abs(a - c) == 1 and abs(b - d) == 2) or (abs(a - c) == 2 and abs(b - d) == 1)

a, b = map(int, input("Введите координаты точки (a, b): ").split())
c, d = map(int, input("Введите координаты точки (c, d): ").split())

if is_rook_move(a, b, c, d):
    print("Ладья может совершить ход из точки (a, b) в точку (c, d).")

if is_bishop_move(a, b, c, d):
    print("Слон может совершить ход из точки (a, b) в точку (c, d).")

if is_queen_move(a, b, c, d):
    print("Ферзь может совершить ход из точки (a, b) в точку (c, d).")

if is_knight_move(a, b, c, d):
    print("Конь может совершить ход из точки (a, b) в точку (c, d).")
