import pygame
from Sudoku import Sudoku
from Interface_Manager import *

def main():
    print("Welcome to Sudoku's game")

    win = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    board = Sudoku()
    key = None
    run = True
    start = time.time()
    strikes = 0
    board.create_table()
    board.eliminate_numbers()
    play_time = round(time.time() - start)
    redraw_window(win, board, play_time, strikes)
    pygame.display.update()
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0 and board.cubes[i][j].value==0: #Check that is a temporal number when it is pressed enter
                        if board.place(board.cubes[i][j].temp): #Check if it is correct the number
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                            if strikes>4:
                                print("Game over")
                                run =False
                        key = None

                        if board.check_finished():
                            print("Congratulation")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)
        pygame.display.update()

main()
pygame.quit()
