from letter import Letter
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
        self.loss = True

    def draw(self):
        for row in self.board:
            for element in row:
                element.draw()

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