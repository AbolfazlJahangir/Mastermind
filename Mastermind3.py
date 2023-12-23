class Mastermind:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.countPlayer1 = 0
        self.countPlayer2 = 0

    def play_game(self):
        player1_set = input(f"{self.player1}, set the number: ")
        player1_digit_state = {}
        for digit in player1_set:
            player1_digit_state[digit] = 0

        player2_show_answer = ["X" for _ in range(len(player1_set))]
        while "X" in player2_show_answer:
            self.countPlayer2 += 1
            print("HINT! Guess a number that has {} digit(s).".format(len(player1_set)))
            player2_guess = input("{}, guess the number: ".format(self.player2))

            while len(player2_guess) != len(player1_set):
                print("Consider the hint! :)")
                player2_guess = input("{}, guess the number: ".format(self.player2))

            for i in range(len(player1_set)):
                if player1_set[i] == player2_guess[i]:
                    player1_digit_state[player1_set[i]] = 1
                    player2_show_answer[i] = player2_guess[i]

            count_correct_guess = list(player1_digit_state.values()).count(1)

            if count_correct_guess != len(player1_set):
                print("Not quite the number. You got {} digits correct.".format(count_correct_guess))
                print("")
                print(" ".join(player2_show_answer))

            print("")

        print("{} did it after {} time(s)!".format(self.player2, self.countPlayer2))

        
        player2_set = input(f"{self.player2}, set the number: ")
        player2_digit_state = {}
        for digit in player2_set:
            player2_digit_state[digit] = 0

        player1_show_answer = ["X" for _ in range(len(player2_set))]
        while "X" in player1_show_answer:
            self.countPlayer1 += 1
            print("HINT! Guess a number that has {} digit(s).".format(len(player2_set)))
            player1_guess = input("{}, guess the number: ".format(self.player1))

            while len(player1_guess) != len(player2_set):
                print("Consider the hint! :)")
                player1_guess = input("{}, guess the number: ".format(self.player1))

            for i in range(len(player2_set)):
                if player2_set[i] == player1_guess[i]:
                    player2_digit_state[player2_set[i]] = 1
                    player1_show_answer[i] = player1_guess[i]

            count_correct_guess = list(player2_digit_state.values()).count(1)

            if count_correct_guess != len(player2_set):
                print("Not quite the number. You got {} digits correct.".format(count_correct_guess))
                print("")
                print(" ".join(player1_show_answer))

            print("")

        print("{} did it after {} time(s)!".format(self.player1, self.countPlayer1))

    def display_winner(self):
        if self.countPlayer1 > self.countPlayer2:
            print(f"Alright! {self.player2} is a Mastermind! It took you only {self.countPlayer2} tries!")
        elif self.countPlayer2 > self.countPlayer1:
            print(f"Alright! {self.player1} is a Mastermind! It took you only {self.countPlayer1} tries!")
        else:
            print(f"Tie! Both of you guessed correctly. It took you only {self.countPlayer1} tries.")

if __name__ == "__main__":
    player1 = input("Player1, name: ")
    player2 = input("Player2, name: ")
    game = Mastermind(player1, player2)
    game.play_game()
    game.display_winner()
