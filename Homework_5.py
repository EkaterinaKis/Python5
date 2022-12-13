
def show_field(field):
    print("--" * 5)
    for i in range(0, len(field), 3):
        print(field[i], '|', field[i+1], '|', field[i+2])
        print("--" * 5)


field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
show_field(field)
count = 0
win_table = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

for i in range(1, len(field)):
    chosen_number = int(input('Введите выбранную вами ячейку для хода X: '))
    if (chosen_number < 1 or chosen_number > 9):
        print('Введено некорректное число')
        continue
    if (chosen_number >= 1 and chosen_number <= 9):
        if (str(field[chosen_number-1]) not in 'XO'):
            field[chosen_number-1] = 'X'
            count += 1
            if count == 9:
                print('Ничья')
                break
        else:
            print('Эта клетка занята')
            continue
        show_field(field)
    for i in win_table:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            print("X выиграл!")
        break
    chosen_number2 = int(input('Введите выбранную вами ячейку для хода O: '))
    if (chosen_number2 < 1 or chosen_number2 > 9):
        print('Введено некорректное число')
        continue
    if (chosen_number2 >= 1 and chosen_number2 <= 9):
        if (str(field[chosen_number2-1]) not in 'XO'):
            field[chosen_number2-1] = 'O'
            count += 1
            if count == 9:
                print('Ничья')
                break
        else:
            print('Эта клетка занята')
            continue
        show_field(field)
    for i in win_table:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            print('O выиграл')
        break
