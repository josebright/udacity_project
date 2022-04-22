#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random


moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None
        self.my_move = None

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.last_move = None

    def move(self):
        move = None
        if self.last_move is None:
            move = Player.move(self)
        else:
            index = moves.index(self.last_move) + 1
            if index >= len(moves):
                index = 0
            move = moves[index]
        self.last_move = move
        return move


class HumanPlayer(Player):
    def move(self):
        player_move = input("Rock, paper, scissors? ").lower()
        while player_move not in moves:
            if player_move == "quit":
                exit()
            player_move = input("Rock, paper, scissors? ").lower()
        return player_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    player_one_score = 0
    player_two_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player One: {move1}  Player Two: {move2}")
        if beats(move1, move2):
            self.player_one_score += 1
            print(f"** PLAYER One WINS **")
            print(f"Score: Player One {self.player_one_score}, "
                  f"Player Two {self.player_two_score}\n")
        elif move1 == move2:
            print(f"** TIE **")
            print(f"Score: Player One {self.player_one_score}, "
                  f"Player Two {self.player_two_score}\n")
        else:
            self.player_two_score += 1
            print(f"** PLAYER TWO WINS **")
            print(f"Score: Player One {self.player_one_score}, "
                  f"Player Two {self.player_two_score}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self, n):
        round = 0
        print("Game start!")
        while True:
            for i in range(n):
                print(f"Round {round}:")
                if self.player_one_score >= self.player_two_score + 3:
                    print("Game Over!\n Player One Wins")
                    print(f"Score: Player One {self.player_one_score}, "
                          f"Player Two {self.player_two_score}\n")
                    exit()
                elif self.player_one_score >= self.player_two_score + 3:
                    print("Game Over!\n Player Two Wins")
                    print(f"Score: Player One {self.player_one_score}, "
                          f"Player Two {self.player_two_score}\n")
                    exit()
                self.play_round()
                round += 1
            print("Game over!")
            exit()


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game(10)
