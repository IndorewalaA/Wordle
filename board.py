from letter import Letter
from key import Key
import pygame
import random

class Board:
    board: list[list[Letter]]

    def __init__(self, screen):
        self.word_list = []
        self.screen = screen
        self.board = [[] for _ in range(6)]
        with open("words_list.txt", 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                self.word_list.extend(words)
        self.word = self.word_list[random.randint(0, 5656)]
        print(self.word)
        for i in range(6):
            for j in range(5):
                self.board[i].append(Letter(j, i, self.screen))
        self.current = self.board[0][0]
        self.loss = False
        self.win = False
        self.key_dict = {}
        self.add_keys()
        self.turn_num = 0

    def add_keys(self):
        self.key_dict["Q"] = Key("Q", 1)
        self.key_dict["W"] = Key("W", 2)
        self.key_dict["E"] = Key("E", 3)
        self.key_dict["R"] = Key("R", 4)
        self.key_dict["T"] = Key("T", 5)
        self.key_dict["Y"] = Key("Y", 6)
        self.key_dict["U"] = Key("U", 7)
        self.key_dict["I"] = Key("I", 8)
        self.key_dict["O"] = Key("O", 9)
        self.key_dict["P"] = Key("P", 10)
        self.key_dict["A"] = Key("A", 1)
        self.key_dict["S"] = Key("S", 2)
        self.key_dict["D"] = Key("D", 3)
        self.key_dict["F"] = Key("F", 4)
        self.key_dict["G"] = Key("G", 5)
        self.key_dict["H"] = Key("H", 6)
        self.key_dict["J"] = Key("J", 7)
        self.key_dict["K"] = Key("K", 8)
        self.key_dict["L"] = Key("L", 9)
        self.key_dict["Z"] = Key("Z", 1)
        self.key_dict["X"] = Key("X", 2)
        self.key_dict["C"] = Key("C", 3)
        self.key_dict["V"] = Key("V", 4)
        self.key_dict["B"] = Key("B", 5)
        self.key_dict["N"] = Key("N", 6)
        self.key_dict["M"] = Key("M", 7)

    def update_keys(self):
        for i in range(5):
            letter = self.board[self.current.row - 1][i].letter.upper()
            if self.board[self.current.row - 1][i].color == "green":
                self.key_dict[letter].color = "green"
            else:
                self.key_dict[letter].color = "black"

    def draw(self):
        for row in self.board:
            for element in row:
                element.draw()

    def draw_keys(self):
        for key in self.key_dict.values():
            key.draw(self.screen)

    def select(self, row: int, col: int):
        self.current = self.board[row][col]

    def type(self, key: str):
        if self.current.letter == "":
            self.current.letter = key
        if self.current.col < 4:
            self.current = self.board[self.current.row][self.current.col + 1]

    def delete(self):
        if 0 < self.current.col < 4:
            delete = self.board[self.current.row][self.current.col - 1]
            delete.letter = ""
            self.current = self.board[self.current.row][self.current.col - 1]
        if self.current.col == 4:
            if self.current.letter == "":
                delete = self.board[self.current.row][self.current.col - 1]
                delete.letter = ""
                self.current = self.board[self.current.row][self.current.col - 1]
            else:
                self.current.letter = ""

    def check_real(self):
        attempted_word = ""
        for i in range(5):
            attempted_word += self.board[self.current.row][i].letter.lower()
        for word in self.word_list:
            if attempted_word == word:
                return True

    def submit(self):
        self.turn_num += 1
        checkWin = True
        matched_letters = set()
        for i in range(5):
            guess_letter = self.board[self.current.row][i].letter.lower()
            target_letter = self.word[i]
            if guess_letter == target_letter:
                self.board[self.current.row][i].color = "green"
                matched_letters.add(guess_letter)
            else:
                if guess_letter.lower() in matched_letters:
                    self.board[self.current.row][i].color = "gray"
                elif guess_letter.lower() in self.word.lower():
                    self.board[self.current.row][i].color = "yellow"
                else:
                    self.board[self.current.row][i].color = "gray"
                checkWin = False
            self.board[self.current.row][i].set_submission(True)
        if checkWin:
            self.win = True
        elif self.turn_num == 6:
            self.loss = True
        if self.current.row < 5:
            self.current = self.board[self.current.row + 1][0]
