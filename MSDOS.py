import random

# Welcome text
print("Hey Welcome To MS DOS!")
print("We Are So Excited To See You Here!")
print("Please Complete The Setup Process To Use The OS.\n")

# Working with variables
name = input("What's Your Name? ")
time.sleep(0.5)
print("Nice To Meet You! " + name + "")
time.sleep(0.5)
age = input("What's Your Age? ")
time.sleep(0.5)
print("Oh You Are " + age + ". It's Just A Small Information To Help You And Find Stuff That Might Be Interesting To You.")
time.sleep(0.5)
computer = input("Are You New To Computers? Yes/No ")
if computer.lower() == "yes":
    time.sleep(1)
    print("It's Fine I Am Always Ready To Help You!")
    time.sleep(2)
elif computer.lower() == "no":
    time.sleep(0.5)
    print("Nice! But Don't Be Afraid To Ask For Help.")
    time.sleep(2)
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
    exit()



# The MS DOS

print("You Finished The Setup Process! \n\n\n\n\n\n\n\n\n\n\n\n")
time.sleep(3)
print("You Have Two Games And Three Quizzes")
apps = input ("Do You Want To Play Games Or Do Quizzes, Enter 'Games' Or 'Quiz' To Open: ")

# Options
if apps.lower() == "games":
    time.sleep(0.5)
    game_options = input("You Have Two Games Tic-Tac-Toe And Tetris, Enter 'TTT' For Tic-Tac-Toe Or 'Tetris' For Tetris To Open: ")
    time.sleep(2)
elif apps.lower() == "quiz":
    time.sleep(0.5)
    quiz_options = input("You have three Quizzes: Science, Math, and History. Enter 'Science' or 'Math' or 'History' to open: ")
    time.sleep(2)
else:
    print("Invalid input. Please enter 'Games' or 'Quiz'.")
    exit()

# The Games
if game_options.lower == "TTT":
    time.sleep(0.5)


    board = [' '] * 9


    def display_board():
        print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' ')
        print('---|---|---')
        print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' ')
        print('---|---|---')
        print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' ')


    def player_input():
        marker = ''
        while not (marker == 'X' or marker == 'O'):
            marker = input("Player 1, choose X or O: ").upper()

        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')


    def place_marker(board, marker, position):
        board[position - 1] = marker


    def win_check(board, mark):
        return ((board[0] == mark and board[1] == mark and board[2] == mark) or
                (board[3] == mark and board[4] == mark and board[5] == mark) or
                (board[6] == mark and board[7] == mark and board[8] == mark) or
                (board[0] == mark and board[3] == mark and board[6] == mark) or
                (board[1] == mark and board[4] == mark and board[7] == mark) or
                (board[2] == mark and board[5] == mark and board[8] == mark) or
                (board[0] == mark and board[4] == mark and board[8] == mark) or
                (board[2] == mark and board[4] == mark and board[6] == mark))


    def choose_first():
        if random.randint(0, 1) == 0:
            return 'Player 2'
        else:
            return 'Player 1'


    def space_check(board, position):
        return board[position - 1] == ' '


    def full_board_check(board):
        return ' ' not in board


    def player_choice(board):
        position = 0
        while position not in range(1, 10) or not space_check(board, position):
            position = int(input('Choose your next position: (1-9) '))
        return position


    def replay():
        return input("Do you want to play again? Enter 'Yes' or 'No': ").lower().startswith('y')


    print('Welcome to Tic Tac Toe!')
    while True:
        board = [' '] * 9
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')
        play_game = input("Are you ready to play? Enter 'Yes' or 'No'.")
        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                display_board()
                position = player_choice(board)
                place_marker(board, player1_marker, position)
                if win_check(board, player1_marker):
                    display_board()
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board()
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'
            else:
                display_board()
                position = player_choice(board)
