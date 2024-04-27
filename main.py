import pygame
import sys
from pygame.locals import *


def main_menu(screen: pygame.Surface):
    screen.fill((18, 18, 19))
    title_font = pygame.font.Font("fonts\FranklinGothic.ttf",70)
    play_font = pygame.font.Font("fonts\QUICK-ZIP.otf",30)
    title_card = title_font.render("Wordle", True, (255, 255, 255))
    title_block = title_card.get_rect(center=(200, 100))
    play_card = play_font.render("Play", True, (121, 121, 135))
    play_block = play_card.get_rect(center=(200, 300))
    screen.blit(title_card, title_block)
    screen.blit(play_card, play_block)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == BUTTON_LEFT:
                    if play_block.collidepoint(event.pos):
                        return


def main():
    screen = pygame.display.set_mode((400, 600))
    pygame.init()
    main_menu(screen)
    while True:
        franklin_gothic = pygame.font.Font("fonts\FranklinGothic.ttf",30)


if __name__ == "__main__":
    main()
