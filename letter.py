import math, random
import pygame


class Letter:
    def __init__(self, col: int, row: int, screen: pygame.Surface):
        self.letter = ""
        self.color = "black"
        self.row = row
        self.col = col
        self.screen = screen
        self.submitted = False
        self.current = False
        self.rect = pygame.Rect(40 + (self.col * 60) + (self.col * 5), 90 + (self.row * 5) + (self.row * 60)
                                , 60, 60)

    def set_color(self, color: str):
        self.color = color

    def set_submission(self, submitted: bool):
        self.submitted = submitted

    def set_letter(self, letter: str):
        self.letter = letter.capitalize()

    def draw(self):
        font = pygame.font.Font("fonts\FranklinGothic.ttf", 40)
        if self.letter != "" and self.submitted:
            if self.color == "gray":
                pygame.draw.rect(self.screen, (86, 87, 88), self.rect)
            elif self.color == "yellow":
                pygame.draw.rect(self.screen, (181, 159, 59), self.rect)
            elif self.color == "green":
                pygame.draw.rect(self.screen, (83, 141, 78), self.rect)
        else:
            pygame.draw.rect(self.screen, (86, 87, 88), self.rect, width=2, border_radius=1)
        letter_card = font.render(self.letter, True, (255, 255, 255))
        letter_block = letter_card.get_rect(center=(70 + (self.col * 60) + (self.col * 5), 123 + (self.row * 5) +
                                                    (self.row * 60)))
        self.screen.blit(letter_card, letter_block)
