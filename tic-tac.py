def check_winner():
    if area[0][0] == "X" and area[0][1] == "X" and area[0][2] == "X":
        return "X"
    if area[0][0] == "0" and area[0][1] == "0" and area[0][2] == "0":
        return "0"

def draw_area():
    # игровое поле
    for i in area:
        print(*i)
    print()

area = [["*","*","*"],["*","*","*"],["*","*","*"]]
print("Игра крестики нолики")
draw_area()
for turn in range(1,10):
    print(f'ход {turn}')
    if turn % 2 == 0:
        turn_char = "0"
        print("ходят ноилки")
    else:
        turn_char = "X"
        print("ходят крестики")
    row = int(input("Введите номер строки (1,2,3) ")) - 1
    column = int(input("Введите номер столбца (1,2,3) ")) - 1
    if area[row][column] == "*":
        area[row][column] = turn_char
    else:
        print("Ячейка занята")
        draw_area()
        continue

    draw_area()
    if check_winner() == "X":
        print("Победа крестика")
        break
    if check_winner() == "0":
        print("Победа ноликов")
        break
    if check_winner() == "*" and turn == 9:
        print("Ничья")
        break