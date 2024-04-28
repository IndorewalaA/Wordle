import math, random
import pygame


class Letter:
    def __init__(self, color: str, col: int, row: int, screen: pygame.Surface):
        self.letter = ""
        self.color = color
        self.row = row
        self.col = col
        self.submitted = False
        self.screen = screen
        self.rect = pygame.Rect(40 + ((self.col - 1) * 60) + ((self.col - 1) * 5), 70 + (self.row * 5) + (self.row * 60)
                                , 60, 60)

    def set_color(self, color: str):
        self.color = color

    def set_submission(self, submitted: bool):
        self.submitted = submitted

    def draw(self, current):
        font = pygame.font.Font("fonts\QUICK-ZIP.otf", 50)
        pygame.draw.rect(self.screen, (86, 87, 88), self.rect, width=1, border_radius=1)
        if self.letter == "":
            return
        if self.letter != "":
            return