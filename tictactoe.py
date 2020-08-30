cells = list(' ' * 9)
count = 0


def game_board():
    print('-' * 9)
    print(f'| {cells[0]} {cells[1]} {cells[2]} |')
    print(f'| {cells[3]} {cells[4]} {cells[5]} |')
    print(f'| {cells[6]} {cells[7]} {cells[8]} |')
    print('-' * 9)


def game():
    global cells
    global count
    coordinates = ['13', '23', '33', '12', '22', '32', '11', '21', '31']
    while True:
        wins = cells[:3], cells[3:6], cells[6:9], cells[:7:3], cells[1:8:3], cells[2:9:3], cells[::4], cells[2:7:2]
        turn = 'X' if count % 2 == 0 else 'O'

        if ['X', 'X', 'X'] in wins:
            print('X wins')
            break
        elif ['O', 'O', 'O'] in wins:
            print('O wins')
            break
        elif ' ' not in [x for x in cells]:
            print('Draw')
            break

        coordinate = input("Enter the coordinate: ").replace(' ', '')
        coord_index = coordinates.index(coordinate) if coordinate in coordinates else None

        if coordinate[0].isalpha() or coordinate[1].isalpha():
            print("You should enter numbers!")
            return game()
        elif len([int(x) for x in coordinate if int(x) < 4]) != 2:
            print("Coordinates should be from 1 to 3!")
            return game()
        elif cells[coord_index] in ('X', 'O'):
            print("This cell is occupied! Choose another one!")
            return game()
        else:
            cells[coord_index] = turn
            game_board()
            count += 1


game_board()
game()
