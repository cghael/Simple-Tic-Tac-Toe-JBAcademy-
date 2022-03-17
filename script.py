# write your code here

rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def print_board():
    print("---------")
    for row in rows:
        print("| ", end="")
        for el in row:
            if el == 0:
                print("  ", end="")
            elif el == 1:
                print("X ", end="")
            else:
                print("O ", end="")
        print("|")
    print("---------")


def is_winner():
    columns = [[rows[x][y] for x in range(3)] for y in range(3)]
    diags = [[rows[0][0], rows[1][1], rows[2][2]], [rows[0][2], rows[1][1], rows[2][0]]]
    lines = rows + columns + diags
    return any(abs(n) == 3 for n in [sum(x) for x in lines])


def check_cords(first_player):
    is_valid = False
    cords = []
    while is_valid is not True:
        cords = input("Enter the coordinates: ").split()
        if len(cords) != 2:
            print("You should enter numbers!")
            continue
        if all(s.isdigit() for s in cords) is not True:
            print("You should enter numbers!")
            continue
        cords = [int(x) for x in cords]
        if all(x in [1, 2, 3] for x in cords) is not True:
            print("Coordinates should be from 1 to 3!")
            continue
        if rows[cords[0] - 1][cords[1] - 1] != 0:
            print("This cell is occupied! Choose another one!")
            continue
        is_valid = True
    rows[cords[0] - 1][cords[1] - 1] = (1 if first_player else -1)


def main():
    game = True
    first_player = True
    print_board()
    while game:
        check_cords(first_player)
        print_board()
        if is_winner() is True:
            game = False
            print("X" if first_player == 1 else "O", "wins")
        first_player = not first_player


if __name__ == "__main__":
    main()
