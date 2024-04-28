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
        self.word = self.word_list[random.randint(0, 5657)]
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
            if self.current.col != 4:
                self.current = self.board[self.current.row][self.current.col + 1]
            else:
                self.loss = True

    def delete(self):
        if self.current.letter != "":
            self.current.letter = ""
            if self.current.col != 0:
                self.current = self.board[self.current.row][self.current.col - 1]