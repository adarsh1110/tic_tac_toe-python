# Two Player Tic-Tac-Toe game using only function.
'''
We have make the tic-tac-toe board using with dictinary
Basically board has work as keyboard keypad
7|8|9
-+-+-
4|5|6
-+-+-
1|2|3

so the starting board accept blank value
'''
player1 = 'X'
player2 = 'O'
player1 = input("Player-1 Enter your name:")
print(player1, "You are \'X\' ")
# p1_key = input("Choice your key \'X\' or \'O\': " )
player2= input("Player-2 Enter your name:")
print(player2,"You \'O\' ")


Board =     {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in Board:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(Board)
        if turn == 'X':
            print(f"It's your turn {player1} you are {turn}, Move to which place?")
        elif turn == 'O':
            print(f"It's your turn {player2} you are {turn}, Move to which place?")

        move = input()

        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ':  # across the top
                printBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ':  # across the middle
                printBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ':  # across the bottom
                printBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ':  # down the left side
                printBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ':  # down the middle
                printBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ':  # down the right side
                printBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['7'] == Board['5'] == Board['3'] != ' ':  # diagonal
                printBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ':  # diagonal
                printBoard(Board)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            break

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            Board[key] = " "

        game()


if __name__ == "__main__":
    game()