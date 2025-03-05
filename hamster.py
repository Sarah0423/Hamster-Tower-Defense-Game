import pygame
import sys
import subprocess

start = 0
help = 0
choose = 0

pygame.init()

width = 922
height = 499
game_window = pygame.display.set_mode((width, height))
game_window.fill("white")

click = pygame.mixer.Sound("audio/button_click.mp3")
page = pygame.mixer.Sound("audio/page.mp3")
select = pygame.mixer.Sound("audio/choose.mp3")

main_page = pygame.image.load("image/封面.jpg")
bg = pygame.image.load("image/背景.jpg")
no_coin_bg = pygame.image.load("image/coin_bg.jpg")
no_hp_bg = pygame.image.load("image/hp_bg.jpg")
help1 = pygame.image.load("image/help1.jpg")
help2 = pygame.image.load("image/help2.jpg")
help3 = pygame.image.load("image/help3.jpg")
help4 = pygame.image.load("image/help4.jpg")
start_button = pygame.image.load("image/button_start.png")
help_button = pygame.image.load("image/button_help.png")
exit_button = pygame.image.load("image/button_exit.png")
normal_button = pygame.image.load("image/button_normal.png")
no_hp_button = pygame.image.load("image/button_no_hp.png")
no_coin_button = pygame.image.load("image/button_no_coin.png")
previous = pygame.image.load("image/previous.png")
next = pygame.image.load("image/next.png")

main_page = pygame.transform.scale(main_page, (width, height))
bg = pygame.transform.scale(bg, (width, height))
no_coin_bg = pygame.transform.scale(no_coin_bg, (width, height))
no_hp_bg = pygame.transform.scale(no_hp_bg, (width, height))
help1 = pygame.transform.scale(help1, (width, height))
help2 = pygame.transform.scale(help2, (width, height))
help3 = pygame.transform.scale(help3, (width, height))
help4 = pygame.transform.scale(help4, (width, height))

start_button = pygame.transform.scale(start_button, (210, 70))
help_button = pygame.transform.scale(help_button, (210, 70))
exit_button = pygame.transform.scale(exit_button, (150, 60))
normal_button = pygame.transform.scale(normal_button, (240, 80))
no_hp_button = pygame.transform.scale(no_hp_button, (240, 80))
no_coin_button = pygame.transform.scale(no_coin_button, (240, 80))

previous = pygame.transform.scale(previous, (50, 50))
next = pygame.transform.scale(next, (50, 50))
font_30 = pygame.font.Font("k12x8.ttf", 30)
font_25 = pygame.font.Font("k12x8.ttf", 25)
font = pygame.font.Font("k12x8.ttf", 20)
help_page = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if help == 1 and help_page == 4:
                if 356 <= x <= 566 and 400 <= y <= 470:  # help"START"
                    click.play(0)
                    choose = 1
            if help == 0 and 356 <= x <= 566 and 310 <= y <= 380:  # "START"
                click.play(0)
                choose = 1
            if 356 <= x <= 566 and 400 <= y <= 470:
                click.play(0)
                help = 1
                help_page = 1
            if help == 1:
                if choose == 1:
                    if 10 <= x <= 60 and 10 <= y <= 60:  # help back
                        help_page = 5
                if 10 <= x <= 60 and 10 <= y <= 60:
                    if help_page > 1:
                        page.play(0)
                        help_page -= 1
                    else:
                        page.play(0)
                        help = 0
                if 862 <= x <= 912 and 10 <= y <= 60:
                    page.play(0)
                    help_page = min(4, help_page + 1)
            if choose == 1:
                if 10 <= x <= 60 and 10 <= y <= 60:
                    choose = 0
                elif 82 <= x <= 322 and 200 <= y <= 280:
                    select.play(0)
                    pygame.time.delay(300)
                    pygame.quit()
                    subprocess.run(["python", "normal.py"])
                    sys.exit()
                elif 341 <= x <= 581 and 200 <= y <= 280:
                    select.play(0)
                    pygame.time.delay(300)
                    pygame.quit()
                    subprocess.run(["python", "no_hp.py"])
                    sys.exit()
                elif 600 <= x <= 840 and 200 <= y <= 280:
                    select.play(0)
                    pygame.time.delay(300)
                    pygame.quit()
                    subprocess.run(["python", "no_coin.py"])
                    sys.exit()
            if 770 <= x <= 920 and 400 <= y <= 470:
                select.play(0)
                pygame.time.delay(300)
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if 341 <= x <= 581 and 200 <= y <= 280:
                current_background = no_hp_bg
            elif 600 <= x <= 840 and 200 <= y <= 280:
                current_background = no_coin_bg
            else:
                current_background = bg
        

    game_window.blit(main_page, (0, 0))
    game_window.blit(start_button, (356, 310))
    game_window.blit(help_button, (356, 400))
    game_window.blit(exit_button, (770, 400))
    game_window.blit(font_30.render("START", True, "white"), (405, 330))
    game_window.blit(font_30.render("HELP", True, "white"), (420, 420))
    game_window.blit(font.render("EXIT", True, "white"), (820, 422))

    if help == 1:
        if help_page == 1:
            game_window.blit(help1, (0, 0))
            game_window.blit(previous, (10, 10))
            game_window.blit(next, (862, 10))
            game_window.blit(font.render("Hamster", True, "orange"), (290, 140))
            game_window.blit(font.render("Boring Hamster", True, "black"), (150, 230))
            game_window.blit(font.render("Normal HP", True, "black"), (150, 260))
            game_window.blit(font.render("Normal Power", True, "black"), (150, 290))

            game_window.blit(font.render("Working", True, "brown"), (650, 130))
            game_window.blit(font.render("Hamster", True, "brown"), (650, 150))
            game_window.blit(font.render("Earn Money", True, (240, 229, 84)), (510, 230))
            game_window.blit(font.render("Low HP", True, "black"), (510, 260))
            game_window.blit(font.render("Low Power", True, "black"), (510, 290))
        elif help_page == 2:
            game_window.blit(help2, (0, 0))
            game_window.blit(previous, (10, 10))
            game_window.blit(next, (862, 10))
            game_window.blit(font.render("Defense", True, (86, 184, 219)), (290, 130))
            game_window.blit(font.render("Hamster", True, (86, 184, 219)), (290, 150))
            game_window.blit(font.render("Defense!!!", True, (86, 184, 219)), (150, 230))
            game_window.blit(font.render("High HP", True, "black"), (150, 260))
            game_window.blit(font.render("Low Power", True, "black"), (150, 290))
            
            game_window.blit(font.render("Cupid", True, (232, 165, 160)), (650, 140))
            game_window.blit(font.render("Charm The Bird", True, (232, 165, 160)), (510, 230))
            game_window.blit(font.render("Support Only", True, "red"), (510, 260))
        elif help_page == 3:
            game_window.blit(help3, (0, 0))
            game_window.blit(previous, (10, 10))
            game_window.blit(next, (862, 10))
            game_window.blit(font.render("Archer", True, "purple"), (290, 140))
            game_window.blit(font.render("Shooting The Bird", True, "black"), (150, 230))
            game_window.blit(font.render("Support Only", True, "red"), (150, 260))

            game_window.blit(font.render("Cat", True, "gray"), (650, 140))
            game_window.blit(font.render("Boring Enemy", True, "black"), (510, 230))
            game_window.blit(font.render("Low HP", True, "black"), (510, 260))
            game_window.blit(font.render("Normal Power", True, "black"), (510, 290))
        elif help_page == 4:
            game_window.blit(help4, (0, 0))
            game_window.blit(previous, (10, 10))
            
            game_window.blit(font.render("Dog", True, (92, 92, 92)), (290, 140))
            game_window.blit(font.render("Danger", True, "red"), (150, 230))
            game_window.blit(font.render("Strong HP", True, "black"), (150, 260))
            game_window.blit(font.render("Strong Power", True, "black"), (150, 290))
            
            game_window.blit(font.render("Bird", True, (240, 229, 84)), (650, 140))
            game_window.blit(font.render("Clear All", True, "black"), (510, 230))
            game_window.blit(font.render("If Charmed:", True, (232, 165, 160)), (510, 260))
            game_window.blit(font.render("Kill Enemy Only", True, "black"), (510, 290))
            

            game_window.blit(start_button, (356, 400))
            game_window.blit(font_30.render("START", True, "white"), (405, 420))
    if choose == 1:
        game_window.blit(current_background, (0, 0))
        game_window.blit(previous, (10, 10))
        game_window.blit(normal_button, (82, 200))
        game_window.blit(no_hp_button, (341, 200))
        game_window.blit(no_coin_button, (600, 200))

        game_window.blit(font_25.render("Normal", True, "white"), (150, 227.5))
        game_window.blit(font_25.render("Practice", True, "white"), (387.5, 227.5))
        game_window.blit(font_25.render("∞Coin", True, "white"), (660, 227.5))
        pygame.display.update()


    pygame.display.update()
