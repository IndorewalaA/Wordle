import pygame


class Key:
    def __init__(self, letter: str, col: int):
        self.color = "gray"
        self.letter = letter
        self.col = col
        if letter == "Q" or letter == "W" or letter == "E" or letter == "R" or letter == "T" or letter == "Y" or \
                letter == "U" or letter == "I" or letter == "O" or letter == "P":
            self.row = 1
            self.rect = pygame.Rect(22 + ((self.col - 1) * 31) + ((self.col - 1) * 5),
                                    500 + ((self.row - 1) * 5) + ((self.row - 1) * 50)
                                    , 31, 50)
        elif letter == "A" or letter == "S" or letter == "D" or letter == "F" or letter == "G" or letter == "H" or \
                letter == "J" or letter == "K" or letter == "L":
            self.row = 2
            self.rect = pygame.Rect(40 + ((self.col - 1) * 31) + ((self.col - 1) * 5),
                                    500 + ((self.row - 1) * 5) + ((self.row - 1) * 50)
                                    , 31, 50)
        elif letter == "Z" or letter == "X" or letter == "C" or letter == "V" or letter == "B" or letter == "N" or \
                letter == "M":
            self.row = 3
            self.rect = pygame.Rect(76 + ((self.col - 1) * 31) + ((self.col - 1) * 5),
                                    500 + ((self.row - 1) * 5) + ((self.row - 1) * 50)
                                    , 31, 50)

    def draw(self, screen: pygame.Surface):
        font = pygame.font.Font("fonts\FranklinGothic.ttf", 25)
        if self.color == "gray":
            pygame.draw.rect(screen, (129, 131, 132), self.rect, 0, 3)
        elif self.color == "black":
            pygame.draw.rect(screen, (58, 58, 60), self.rect, 0, 3)
        letter_card = font.render(self.letter, True, (255, 255, 255))
        if self.row == 1:
            letter_block = letter_card.get_rect(center=(37 + ((self.col - 1) * 31) + ((self.col - 1) * 5), 525 +
                                                        ((self.row - 1) * 5) + ((self.row - 1) * 50)))
            screen.blit(letter_card, letter_block)
        elif self.row == 2:
            letter_block = letter_card.get_rect(center=(55 + ((self.col - 1) * 31) + ((self.col - 1) * 5), 525 +
                                                        ((self.row - 1) * 5) + ((self.row - 1) * 50)))
            screen.blit(letter_card, letter_block)
        elif self.row == 3:
            letter_block = letter_card.get_rect(center=(91 + ((self.col - 1) * 31) + ((self.col - 1) * 5), 525 +
                                                        ((self.row - 1) * 5) + ((self.row - 1) * 50)))
            screen.blit(letter_card, letter_block)
