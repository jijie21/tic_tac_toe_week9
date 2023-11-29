import csv
import os
from datetime import datetime
from logic import check_winner, get_empty_board, print_board, get_player_input, switch_player
from bot import Bot
import logging

class TicTacToeGame:
    def __init__(self, mode):
        self.current_player = "X"
        self.board = get_empty_board()
        self.winner = None
        self.mode = mode
        self.bot = Bot()
        self.moves_played_X = 0  # Initialize moves played by Player X
        self.moves_played_O = 0  # Initialize moves played by Player O

    def play_game(self):
        while self.winner is None:
            print_board(self.board)
            
            if self.mode == "single" and self.current_player == "O":
                row, col = self.bot.get_bot_move(self.board)
                self.moves_played_O += 1
            else:
                try:
                    row, col = get_player_input(self.current_player)
                    if self.current_player == "X":
                        self.moves_played_X += 1
                    else:
                        self.moves_played_O += 1
                except ValueError:
                    print("Invalid input, try again")
                    continue
                except IndexError:
                    print("Invalid input, try again")
                    continue

            self.board[row][col] = self.current_player
            self.winner = check_winner(self.board)
            self.current_player = switch_player(self.current_player)

        print_board(self.board)
        print(f"Winner is {self.winner}")
        logging.info(f'Player {self.current_player} made a move')

        # Log the game data
        self.log_game_data()

    def log_game_data(self):
        if not os.path.exists('logs'):
            os.makedirs('logs')

        game_id = datetime.now().strftime("%Y%m%d%H%M%S")
        timestamp = datetime.now()
        start_time = timestamp
        duration = 0

        with open('logs/game_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)

            # Write header if the file is empty
            if os.path.getsize('logs/game_data.csv') == 0:
                writer.writerow(['Game_ID', 'Timestamp', 'Winner', 'Player_X', 'Player_O', 'Mode', 'Moves_Played_X', 'Moves_Played_O'])

            end_time = datetime.now()
            duration = (end_time - start_time).seconds

            player_X_type = "Human" if self.mode == "two" or (self.mode == "single" and self.current_player == "X") else "Bot"
            player_O_type = "Human" if self.mode == "two" or (self.mode == "single" and self.current_player == "O") else "Bot"

            writer.writerow([game_id, timestamp, self.winner, player_X_type, player_O_type, self.mode, self.moves_played_X, self.moves_played_O])

if __name__ == '__main__':
    logging.basicConfig(
        filename='logs/msg.log',
        level=logging.INFO
    )

    game_mode = input("Enter game mode (single or two): ").lower()

    if game_mode not in ["single", "two"]:
        print("Invalid game mode. Exiting.")
        exit()

    game = TicTacToeGame(game_mode)
    game.play_game()
