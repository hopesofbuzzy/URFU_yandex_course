# game.py
from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def save_result(s: str):
    with open('results.txt', mode='a', encoding='utf-8') as file:
        file.write(s + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:
        print(f'Ход делают {current_player}')
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()

        winner_message = ''
        if game.check_win(current_player):
            winner_message = f'Победили {current_player}!'
            running = False
        elif game.is_board_full():
            winner_message = 'Ничья!'
            running = False

        if winner_message:
            print(winner_message)
            save_result(winner_message)

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
