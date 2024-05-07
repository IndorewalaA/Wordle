import pygame
import sys
from pygame.locals import *
from board import Board
from key import Key


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
    pygame.init()
    screen = pygame.display.set_mode((400, 700))
    main_menu(screen)
    board = Board(screen)
    clock = pygame.time.Clock()
    draw_word_error = False
    draw_five_error = False
    hide_text_time = 0
    stymie = pygame.font.Font("fonts\OPTIStymie-BoldCondensed.otf", 35)
    error_font = pygame.font.Font("fonts\FranklinGothic.ttf", 15)
    key = Key("Q", 1)
    key1 = Key("P", 10)
    key2 = Key("A", 1)
    key3 = Key("L", 9)
    key4 = Key("Z", 1)
    key5 = Key("M", 7)
    while True:
        small_title = stymie.render("Wordle", True, (255, 255, 255))
        title_card = small_title.get_rect(center=(200, 50))
        screen.fill((18, 18, 19))
        screen.blit(small_title, title_card)
        board.draw()
        board.draw_keys()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if pygame.K_a <= event.key <= pygame.K_z:
                    board.type(chr(event.key - pygame.K_a + ord('A')))
                elif event.key == pygame.K_BACKSPACE:
                    board.delete()
                elif event.key == pygame.K_RETURN:
                    if board.board[board.current.row][4].letter != "":
                        if board.check_real():
                            board.submit()
                            board.update_keys()
                        else:
                            hide_text_time = pygame.time.get_ticks() + 1000
                            draw_word_error = True
                    else:
                        hide_text_time = pygame.time.get_ticks() + 1000
                        draw_five_error = True
        if draw_word_error:
            word_error = error_font.render("Not in word list", True, (0, 0, 0))
            word_error_rect = word_error.get_rect(center=(screen.get_width()/2, 550))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(140, 535, 121, 30), 0, 2)
            screen.blit(word_error, word_error_rect)
            if pygame.time.get_ticks() > hide_text_time:
                draw_word_error = False
        if draw_five_error:
            letter_error = error_font.render("Not enough letters", True, (0, 0,0))
            letter_error_rect = letter_error.get_rect(center=(screen.get_width()/2, 550))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(130, 535, 140, 30), 0, 2)
            screen.blit(letter_error, letter_error_rect)
            if pygame.time.get_ticks() > hide_text_time:
                draw_five_error = False
        pygame.display.update()
        clock.tick(144)


if __name__ == "__main__":
    main()
