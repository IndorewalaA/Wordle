import pygame
import sys
from pygame.locals import *
from board import Board
from letter import Letter


def main_menu(screen: pygame.Surface):
    screen.fill((18, 18, 19))
    title_font = pygame.font.Font("fonts\OPTIStymie-BoldCondensed.otf", 70)
    play_font = pygame.font.Font("fonts\FranklinGothic.ttf", 30)

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
    board = Board(screen)
    clock = pygame.time.Clock()
    while True:
        stymie = pygame.font.Font("fonts\OPTIStymie-BoldCondensed.otf", 35)
        small_title = stymie.render("Wordle", True, (255, 255, 255))
        title_card = small_title.get_rect(center=(200, 50))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            screen.fill((18, 18, 19))
            screen.blit(small_title, title_card)
            board.draw()
            if event.type == pygame.KEYDOWN:
                if pygame.K_a <= event.key <= pygame.K_z:
                    board.type(chr(event.key - pygame.K_a + ord('A')))
                if event.key == pygame.K_BACKSPACE:
                    board.delete()
                if event.key == pygame.K_RETURN:
                    if board.board[board.current.row][4].letter != "":
                        if board.check_real():
                            board.submit()
                        else:
                            print("Not a real letter!")
                    else:
                        print("Print 5 letters!!!")
            pygame.display.update()


if __name__ == "__main__":
    main()
