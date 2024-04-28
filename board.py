import pygame
from letter import Letter

class Board:
    word: list[Letter]

    def __init__(self, screen, attempt_num: int):
        self.screen = screen
