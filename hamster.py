import pygame
import sys
import subprocess

start = 0
help = 0
choose = 0

pygame.init()

視窗寬度 = 922
視窗高度 = 499
屏幕 = pygame.display.set_mode((視窗寬度, 視窗高度))
屏幕.fill("white")

點擊 = pygame.mixer.Sound("audio/button_click.mp3")
翻頁 = pygame.mixer.Sound("audio/page.mp3")
選擇 = pygame.mixer.Sound("audio/choose.mp3")

封面 = pygame.image.load("image/封面.jpg")
背景 = pygame.image.load("image/背景.jpg")
無限金錢背景 = pygame.image.load("image/coin_bg.jpg")
練習背景 = pygame.image.load("image/hp_bg.jpg")
幫助1 = pygame.image.load("image/help1.jpg")
幫助2 = pygame.image.load("image/help2.jpg")
幫助3 = pygame.image.load("image/help3.jpg")
幫助4 = pygame.image.load("image/help4.jpg")
開始按鈕 = pygame.image.load("image/button_start.png")
幫助按鈕 = pygame.image.load("image/button_help.png")
退出按鈕 = pygame.image.load("image/button_exit.png")
一般按鈕 = pygame.image.load("image/button_normal.png")
練習按鈕 = pygame.image.load("image/button_no_hp.png")
無限金錢按鈕 = pygame.image.load("image/button_no_coin.png")
上一個 = pygame.image.load("image/previous.png")
下一個 = pygame.image.load("image/next.png")

封面 = pygame.transform.scale(封面, (視窗寬度, 視窗高度))
背景 = pygame.transform.scale(背景, (視窗寬度, 視窗高度))
無限金錢背景 = pygame.transform.scale(無限金錢背景, (視窗寬度, 視窗高度))
練習背景 = pygame.transform.scale(練習背景, (視窗寬度, 視窗高度))
幫助1 = pygame.transform.scale(幫助1, (視窗寬度, 視窗高度))
幫助2 = pygame.transform.scale(幫助2, (視窗寬度, 視窗高度))
幫助3 = pygame.transform.scale(幫助3, (視窗寬度, 視窗高度))
幫助4 = pygame.transform.scale(幫助4, (視窗寬度, 視窗高度))

開始按鈕 = pygame.transform.scale(開始按鈕, (210, 70))
幫助按鈕 = pygame.transform.scale(幫助按鈕, (210, 70))
退出按鈕 = pygame.transform.scale(退出按鈕, (150, 60))
一般按鈕 = pygame.transform.scale(一般按鈕, (240, 80))
練習按鈕 = pygame.transform.scale(練習按鈕, (240, 80))
無限金錢按鈕 = pygame.transform.scale(無限金錢按鈕, (240, 80))

上一個 = pygame.transform.scale(上一個, (50, 50))
下一個 = pygame.transform.scale(下一個, (50, 50))
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
                    點擊.play(0)
                    choose = 1
            if help == 0 and 356 <= x <= 566 and 310 <= y <= 380:  # "START"
                點擊.play(0)
                choose = 1
            if 356 <= x <= 566 and 400 <= y <= 470:
                點擊.play(0)
                help = 1
                help_page = 1
            if help == 1:
                if choose == 1:
                    if 10 <= x <= 60 and 10 <= y <= 60:  # help back
                        help_page = 5
                if 10 <= x <= 60 and 10 <= y <= 60:
                    if help_page > 1:
                        翻頁.play(0)
                        help_page -= 1
                    else:
                        翻頁.play(0)
                        help = 0
                if 862 <= x <= 912 and 10 <= y <= 60:
                    翻頁.play(0)
                    help_page = min(4, help_page + 1)
            if choose == 1:
                if 10 <= x <= 60 and 10 <= y <= 60:
                    choose = 0
                elif 82 <= x <= 322 and 200 <= y <= 280:
                    選擇.play(0)
                    pygame.time.delay(300)
                    pygame.quit()
                    subprocess.run(["python", "normal.py"])
                    sys.exit()
                elif 341 <= x <= 581 and 200 <= y <= 280:
                    選擇.play(0)
                    pygame.time.delay(300)
                    pygame.quit()
                    subprocess.run(["python", "no_hp.py"])
                    sys.exit()
                elif 600 <= x <= 840 and 200 <= y <= 280:
                    選擇.play(0)
                    pygame.time.delay(300)
                    pygame.quit()
                    subprocess.run(["python", "no_coin.py"])
                    sys.exit()
            if 770 <= x <= 920 and 400 <= y <= 470:
                選擇.play(0)
                pygame.time.delay(300)
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if 341 <= x <= 581 and 200 <= y <= 280:
                current_background = 練習背景
            elif 600 <= x <= 840 and 200 <= y <= 280:
                current_background = 無限金錢背景
            else:
                current_background = 背景
        

    屏幕.blit(封面, (0, 0))
    屏幕.blit(開始按鈕, (356, 310))
    屏幕.blit(幫助按鈕, (356, 400))
    屏幕.blit(退出按鈕, (770, 400))
    屏幕.blit(font_30.render("START", True, "white"), (405, 330))
    屏幕.blit(font_30.render("HELP", True, "white"), (420, 420))
    屏幕.blit(font.render("EXIT", True, "white"), (820, 422))

    if help == 1:
        if help_page == 1:
            屏幕.blit(幫助1, (0, 0))
            屏幕.blit(上一個, (10, 10))
            屏幕.blit(下一個, (862, 10))
            屏幕.blit(font.render("Hamster", True, "orange"), (290, 140))
            屏幕.blit(font.render("Boring Hamster", True, "black"), (150, 230))
            屏幕.blit(font.render("Normal HP", True, "black"), (150, 260))
            屏幕.blit(font.render("Normal Power", True, "black"), (150, 290))

            屏幕.blit(font.render("Working", True, "brown"), (650, 130))
            屏幕.blit(font.render("Hamster", True, "brown"), (650, 150))
            屏幕.blit(font.render("Earn Money", True, (240, 229, 84)), (510, 230))
            屏幕.blit(font.render("Low HP", True, "black"), (510, 260))
            屏幕.blit(font.render("Low Power", True, "black"), (510, 290))
        elif help_page == 2:
            屏幕.blit(幫助2, (0, 0))
            屏幕.blit(上一個, (10, 10))
            屏幕.blit(下一個, (862, 10))
            屏幕.blit(font.render("Defense", True, (86, 184, 219)), (290, 130))
            屏幕.blit(font.render("Hamster", True, (86, 184, 219)), (290, 150))
            屏幕.blit(font.render("Defense!!!", True, (86, 184, 219)), (150, 230))
            屏幕.blit(font.render("High HP", True, "black"), (150, 260))
            屏幕.blit(font.render("Low Power", True, "black"), (150, 290))
            
            屏幕.blit(font.render("Cupid", True, (232, 165, 160)), (650, 140))
            屏幕.blit(font.render("Support Only", True, "red"), (510, 205))
            屏幕.blit(font.render("Charm The Bird", True, (232, 165, 160)), (510, 230))
            屏幕.blit(font.render("Only one Cupid or", True, "orange"), (510, 260))
            屏幕.blit(font.render("Archer can be", True, "orange"), (510, 290))
            屏幕.blit(font.render("present at a time.", True, "orange"), (510, 320))
            
        elif help_page == 3:
            屏幕.blit(幫助3, (0, 0))
            屏幕.blit(上一個, (10, 10))
            屏幕.blit(下一個, (862, 10))
            屏幕.blit(font.render("Archer", True, "purple"), (290, 140))
            屏幕.blit(font.render("Support Only", True, "red"), (150, 205))
            屏幕.blit(font.render("Shooting The Bird", True, "black"), (150, 230))
            屏幕.blit(font.render("Only one Cupid or", True, "orange"), (150, 260))
            屏幕.blit(font.render("Archer can be", True, "orange"), (150, 290))
            屏幕.blit(font.render("present at a time.", True, "orange"), (150, 320))

            
            屏幕.blit(font.render("Cat", True, "gray"), (650, 140))
            屏幕.blit(font.render("Boring Enemy", True, "black"), (510, 230))
            屏幕.blit(font.render("Low HP", True, "black"), (510, 260))
            屏幕.blit(font.render("Normal Power", True, "black"), (510, 290))
        elif help_page == 4:
            屏幕.blit(幫助4, (0, 0))
            屏幕.blit(上一個, (10, 10))
            
            屏幕.blit(font.render("Dog", True, (92, 92, 92)), (290, 140))
            屏幕.blit(font.render("Danger", True, "red"), (150, 230))
            屏幕.blit(font.render("Strong HP", True, "black"), (150, 260))
            屏幕.blit(font.render("Strong Power", True, "black"), (150, 290))
            
            屏幕.blit(font.render("Bird", True, (240, 229, 84)), (650, 140))
            屏幕.blit(font.render("Clear All", True, "black"), (510, 230))
            屏幕.blit(font.render("If Charmed:", True, (232, 165, 160)), (510, 260))
            屏幕.blit(font.render("Kill Enemy Only", True, "black"), (510, 290))
            

            屏幕.blit(開始按鈕, (356, 400))
            屏幕.blit(font_30.render("START", True, "white"), (405, 420))
    if choose == 1:
        屏幕.blit(current_background, (0, 0))
        屏幕.blit(上一個, (10, 10))
        屏幕.blit(一般按鈕, (82, 200))
        屏幕.blit(練習按鈕, (341, 200))
        屏幕.blit(無限金錢按鈕, (600, 200))

        屏幕.blit(font_25.render("Normal", True, "white"), (150, 227.5))
        屏幕.blit(font_25.render("Practice", True, "white"), (387.5, 227.5))
        屏幕.blit(font_25.render("∞Coin", True, "white"), (660, 227.5))
        pygame.display.update()


    pygame.display.update()
