#py -3.11 攻擊ok.py
import pygame
import sys
import random
import time

def 更新金錢():
    global 錢, 錢文字
    if 錢 < 1000:
        if 金幣倉鼠數量 > 0:
            錢 = 錢 + 1 + 金幣倉鼠數量
        else:
            錢 += 1  # 这里假设每次更新增加 1 金钱
    # 重新渲染金钱文本
    錢文字 = font.render(str(錢) + "/" + "1000", True, "black")
    
# 将 start_time 的值设为当前时间
start_time = time.time()

# 變數定義
按下標誌 = 0
金幣按下標誌 = 0
盾牌按下標誌 = 0
編號 = 0
倉鼠座標 = pygame.Rect(722, 280, 0, 0)
我方城堡_生命值 = 10000
敵方城堡_生命值 = 10000
金幣倉鼠數量 = 0
錢 = 50
勝利 = "You Win!!"
失敗 = "You Lose..."
結束 = 0

# pygame 初始化
pygame.init()

# 設置視窗大小
視窗寬度 = 922
視窗高度 = 499
屏幕 = pygame.display.set_mode((視窗寬度, 視窗高度))
屏幕.fill("white")

# 加載圖片

背景 = pygame.image.load("image/背景.jpg")
背景 = pygame.transform.scale(背景, (視窗寬度, 視窗高度))  # 調整背景圖片尺寸
敵人城堡 = pygame.image.load("image/敵堡.png")
城堡 = pygame.image.load("image/我堡.png")
倉鼠按鈕 = pygame.image.load("image/倉鼠按鈕.png")
金幣倉鼠按鈕 = pygame.image.load("image/金幣按鈕.png")
盾牌倉鼠按鈕 = pygame.image.load("image/盾牌按鈕.png")
金幣 = pygame.image.load("image/coin.png")


走動1 = pygame.image.load("image/normal_walk1.png")
走動2 = pygame.image.load("image/normal_walk2.png")
走動3 = pygame.image.load("image/normal_walk3.png")
走動4 = pygame.image.load("image/normal_walk4.png")
金幣走動1 = pygame.image.load("image/coin_walk1.png")
金幣走動2 = pygame.image.load("image/coin_walk2.png")
金幣走動3 = pygame.image.load("image/coin_walk3.png")
金幣走動4 = pygame.image.load("image/coin_walk4.png")
盾牌走動1 = pygame.image.load("image/defense_walk1.png")
盾牌走動2 = pygame.image.load("image/defense_walk2.png")
盾牌走動3 = pygame.image.load("image/defense_walk3.png")
盾牌走動4 = pygame.image.load("image/defense_walk4.png")
貓走動1 = pygame.image.load("image/cat_walk1.png")
貓走動2 = pygame.image.load("image/cat_walk2.png")
貓走動3 = pygame.image.load("image/cat_walk3.png")
貓走動4 = pygame.image.load("image/cat_walk2.png")
狗走動1 = pygame.image.load("image/dog_walk1.png")
狗走動2 = pygame.image.load("image/dog_walk2.png")
狗走動3 = pygame.image.load("image/dog_walk3.png")
狗走動4 = pygame.image.load("image/dog_walk2.png")

攻擊1 = pygame.image.load("image/normal_attack1.png")
攻擊2 = pygame.image.load("image/normal_attack2.png")
攻擊3 = pygame.image.load("image/normal_attack3.png")
金幣攻擊1 = pygame.image.load("image/coin_attack1.png")
金幣攻擊2 = pygame.image.load("image/coin_attack2.png")
金幣攻擊3 = pygame.image.load("image/coin_attack3.png")
盾牌攻擊1 = pygame.image.load("image/defense_attack1.png")
盾牌攻擊2 = pygame.image.load("image/defense_attack2.png")
盾牌攻擊3 = pygame.image.load("image/defense_attack3.png")
貓攻擊1 = pygame.image.load("image/cat_attack1.png")
貓攻擊2 = pygame.image.load("image/cat_attack2.png")
狗攻擊1 = pygame.image.load("image/dog_attack1.png")
狗攻擊2 = pygame.image.load("image/dog_attack2.png")

爆炸1 = pygame.image.load("image/neko.png")
爆炸2 = pygame.image.load("image/neko.png")
爆炸3 = pygame.image.load("image/neko.png")
爆炸4 = pygame.image.load("image/neko.png")
爆炸5 = pygame.image.load("image/neko.png")
爆炸6 = pygame.image.load("image/neko.png")
爆炸7 = pygame.image.load("image/neko.png")
爆炸8 = pygame.image.load("image/neko.png")
爆炸9 = pygame.image.load("image/neko.png")
爆炸10 = pygame.image.load("image/neko.png")
爆炸11 = pygame.image.load("image/neko.png")
爆炸12 = pygame.image.load("image/neko.png")
爆炸13 = pygame.image.load("image/neko.png")

# 更改圖片大小
敵人城堡 = pygame.transform.scale(敵人城堡, (180, 320))
城堡 = pygame.transform.scale(城堡, (180, 320))

倉鼠按鈕 = pygame.transform.scale(倉鼠按鈕, (100, 80))
金幣倉鼠按鈕 = pygame.transform.scale(金幣倉鼠按鈕, (100, 80))
盾牌倉鼠按鈕 = pygame.transform.scale(盾牌倉鼠按鈕, (100, 80))
金幣 = pygame.transform.scale(金幣, (40, 40))

走動1 = pygame.transform.scale(走動1, (150, 150))
走動2 = pygame.transform.scale(走動2, (150, 150))
走動3 = pygame.transform.scale(走動3, (150, 150))
走動4 = pygame.transform.scale(走動4, (150, 150))

金幣走動1 = pygame.transform.scale(金幣走動1, (150, 150))
金幣走動2 = pygame.transform.scale(金幣走動2, (150, 150))
金幣走動3 = pygame.transform.scale(金幣走動3, (150, 150))
金幣走動4 = pygame.transform.scale(金幣走動4, (150, 150))

盾牌走動1 = pygame.transform.scale(盾牌走動1, (150, 150))
盾牌走動2 = pygame.transform.scale(盾牌走動2, (150, 150))
盾牌走動3 = pygame.transform.scale(盾牌走動3, (150, 150))
盾牌走動4 = pygame.transform.scale(盾牌走動4, (150, 150))

貓走動1 = pygame.transform.scale(貓走動1, (150, 150))
貓走動2 = pygame.transform.scale(貓走動2, (150, 150))
貓走動3 = pygame.transform.scale(貓走動3, (150, 150))
貓走動4 = pygame.transform.scale(貓走動4, (150, 150))

狗走動1 = pygame.transform.scale(狗走動1, (150, 150))
狗走動2 = pygame.transform.scale(狗走動2, (150, 150))
狗走動3 = pygame.transform.scale(狗走動3, (150, 150))
狗走動4 = pygame.transform.scale(狗走動4, (150, 150))

攻擊1 = pygame.transform.scale(攻擊1, (150, 150))
攻擊2 = pygame.transform.scale(攻擊2, (150, 150))
攻擊3 = pygame.transform.scale(攻擊3, (150, 150))

金幣攻擊1 = pygame.transform.scale(金幣攻擊1, (150, 150))
金幣攻擊2 = pygame.transform.scale(金幣攻擊2, (150, 150))
金幣攻擊3 = pygame.transform.scale(金幣攻擊3, (150, 150))

盾牌攻擊1 = pygame.transform.scale(盾牌攻擊1, (150, 150))
盾牌攻擊2 = pygame.transform.scale(盾牌攻擊2, (150, 150))
盾牌攻擊3 = pygame.transform.scale(盾牌攻擊3, (150, 150))

貓攻擊1 = pygame.transform.scale(貓攻擊1, (150, 150))
貓攻擊2 = pygame.transform.scale(貓攻擊2, (150, 150))

狗攻擊1 = pygame.transform.scale(狗攻擊1, (150, 150))
狗攻擊2 = pygame.transform.scale(狗攻擊2, (150, 150))

爆炸1 = pygame.transform.scale(爆炸1, (60, 66))
爆炸2 = pygame.transform.scale(爆炸2, (60, 66))
爆炸3 = pygame.transform.scale(爆炸3, (60, 66))
爆炸4 = pygame.transform.scale(爆炸4, (60, 66))
爆炸5 = pygame.transform.scale(爆炸5, (60, 66))
爆炸6 = pygame.transform.scale(爆炸6, (60, 66))
爆炸7 = pygame.transform.scale(爆炸7, (60, 66))
爆炸8 = pygame.transform.scale(爆炸8, (60, 66))
爆炸9 = pygame.transform.scale(爆炸9, (60, 66))
爆炸10 = pygame.transform.scale(爆炸10, (60, 66))
爆炸11 = pygame.transform.scale(爆炸11, (60, 66))
爆炸12 = pygame.transform.scale(爆炸12, (60, 66))
爆炸13 = pygame.transform.scale(爆炸13, (60, 66))

# 倉鼠的走動圖片列表
倉鼠列表 = [走動1, 走動2, 走動3, 走動4]
金幣倉鼠列表 = [金幣走動1, 金幣走動2, 金幣走動3, 金幣走動4]
盾牌倉鼠列表 = [盾牌走動1, 盾牌走動2, 盾牌走動3, 盾牌走動4]
貓列表 = [貓走動1, 貓走動2, 貓走動3, 貓走動4]
狗列表 = [狗走動1, 狗走動2, 狗走動3, 狗走動4]

攻擊列表 = [攻擊1, 攻擊2, 攻擊3]
金幣攻擊列表 = [金幣攻擊1, 金幣攻擊2, 金幣攻擊3]
盾牌攻擊列表 = [盾牌攻擊1, 盾牌攻擊2, 盾牌攻擊3]
貓攻擊列表 = [貓攻擊1, 貓攻擊2]
狗攻擊列表 = [狗攻擊1, 狗攻擊2]

爆炸列表 = [爆炸1, 爆炸2, 爆炸3, 爆炸4, 爆炸5, 爆炸6, 爆炸7, 爆炸8, 爆炸9, 爆炸10, 爆炸11, 爆炸12, 爆炸13]

倉鼠座標列表 = []
金幣倉鼠座標列表 = []
盾牌倉鼠座標列表 = []
貓座標列表 = []
狗座標列表 = []



倉鼠血量列表 = []
金幣血量列表 = []
盾牌血量列表 = []
貓血量列表 = []
狗血量列表 = []


倉鼠攻擊力 = 0.3
金幣攻擊力 = 0.1 
盾牌攻擊力 = 0.2
貓攻擊力 = 0.3
狗攻擊力 = 0.5

# 加載字體
font = pygame.font.Font("C:/USERS/USER/APPDATA/LOCAL/MICROSOFT/WINDOWS/FONTS/K12X8.TTF", 20)
敵方塔文字 = font.render(str(敵方城堡_生命值) + "/" + "10000", True, "black")
我方塔文字 = font.render(str(我方城堡_生命值) + "/" + "10000", True, "black")

current_time = time.time()


def 倉鼠出擊():
    座標 = pygame.Rect(722, 280, 0, 0)
    倉鼠座標列表.append(座標)
    血量 = 100
    倉鼠血量列表.append(血量)
    
def 金幣倉鼠出擊():
    座標 = pygame.Rect(722, 280, 0, 0)
    金幣倉鼠座標列表.append(座標)
    血量 = 50
    金幣血量列表.append(血量)
    
def 盾牌倉鼠出擊():
    座標 = pygame.Rect(722, 280, 0, 0)
    盾牌倉鼠座標列表.append(座標)
    血量 = 150
    盾牌血量列表.append(血量)
    
def 貓出擊():
    座標 = pygame.Rect(180, 280, 0, 0)
    貓座標列表.append(座標)
    血量 = 50
    貓血量列表.append(血量)
    
def 狗出擊():
    座標 = pygame.Rect(180, 280, 0, 0)
    狗座標列表.append(座標)
    血量 = 100
    狗血量列表.append(血量)

def 攻擊(攻擊者座標列表, 攻擊者血量列表, 攻擊者索引, 攻擊者攻擊力, 攻擊者攻擊列表, 被攻擊者座標列表, 被攻擊者血量列表, 被攻擊者索引, 被攻擊者攻擊力, 被攻擊者攻擊列表):
    # 確認雙方都還有血量
    if 攻擊者血量列表[攻擊者索引] > 0 and 被攻擊者血量列表[被攻擊者索引] > 0:
        # 進入戰鬥模式，直到一方血量歸零
        戰鬥結束 = False
        攻擊編號 = 0
        while not 戰鬥結束:
            攻擊者座標 = 攻擊者座標列表[攻擊者索引]
            被攻擊者座標 = 被攻擊者座標列表[被攻擊者索引]
            # 顯示攻擊動畫、更新螢幕
            屏幕.blit(背景, (0, 0))
            屏幕.blit(敵人城堡, (40, 100))
            屏幕.blit(城堡, (722, 100))
            屏幕.blit(攻擊者攻擊列表[攻擊編號 % len(攻擊者攻擊列表)], (攻擊者座標.x, 攻擊者座標.y))
            屏幕.blit(被攻擊者攻擊列表[攻擊編號 % len(被攻擊者攻擊列表)], (被攻擊者座標.x, 被攻擊者座標.y))
            屏幕.blit(敵方塔文字, (45, 90))
            屏幕.blit(我方塔文字, (722, 90))
            屏幕.blit(錢文字, (750, 30))
            屏幕.blit(金幣, (700, 20))
            攻擊編號 += 1
            # 互相攻擊
            被攻擊者血量列表[被攻擊者索引] -= 攻擊者攻擊力
            攻擊者血量列表[攻擊者索引] -= 被攻擊者攻擊力
            
            移動量 = (-1) ** 攻擊編號 * 6  # 交替移動5像素
            攻擊者座標.x += 移動量
            被攻擊者座標.x -= 移動量
            
            pygame.display.update()  # 更新顯示以反映戰鬥狀態
            #pygame.time.Clock().tick(30)  # 控制戰鬥速度
            # 檢查血量
            if 攻擊者血量列表[攻擊者索引] <= 0 or 被攻擊者血量列表[被攻擊者索引] <= 0:
                戰鬥結束 = True
        # 清理死亡的角色
        if 攻擊者血量列表[攻擊者索引] <= 0:
            del 攻擊者座標列表[攻擊者索引]
            del 攻擊者血量列表[攻擊者索引]
        if 被攻擊者血量列表[被攻擊者索引] <= 0:
            del 被攻擊者座標列表[被攻擊者索引]
            del 被攻擊者血量列表[被攻擊者索引]

# 處理遊戲結束
def 結束():
    global 編號
    if 敵方城堡_生命值 == 0:
        for i in range(26):
            編號 = 編號 + 1
            爆炸x = random.randint(90, 120)
            爆炸y = random.randint(250, 350)
            # 以下的 .blit 是為了消除爆炸圖片
            屏幕.blit(背景, (0, 0))
            屏幕.blit(敵人城堡, (40, 100))  
            屏幕.blit(城堡, (722, 100))
            屏幕.blit(爆炸列表[編號 % 13], (爆炸x, 爆炸y))
            屏幕.blit(敵方塔文字, (45, 90))
            屏幕.blit(我方塔文字, (722, 90))
            屏幕.blit(錢文字, (750, 30))
            屏幕.blit(金幣, (700, 20))
       
            pygame.display.update()
            pygame.time.Clock().tick(5)      
        time.sleep(1)
    if 我方城堡_生命值 == 0:
        for i in range(26):
            編號 = 編號 + 1
            爆炸x = random.randint(90, 120)
            爆炸y = random.randint(250, 350)
            # 以下的 .blit 是為了消除爆炸圖片
            屏幕.blit(背景, (0, 0))
            屏幕.blit(敵人城堡, (40, 100))  
            屏幕.blit(城堡, (722, 100))
            屏幕.blit(爆炸列表[編號 % 13], (爆炸x, 爆炸y))
            屏幕.blit(敵方塔文字, (45, 90))
            屏幕.blit(我方塔文字, (722, 90))
            屏幕.blit(錢文字, (750, 30))
            屏幕.blit(金幣, (700, 20))
       
            pygame.display.update()
            pygame.time.Clock().tick(5)      
        time.sleep(1)
   
    while True:
        # display.update 是為了避免殘留畫面
        pygame.display.update()
        屏幕.blit(背景, (0, 0))
        屏幕.blit(敵人城堡, (40, 100))
        屏幕.blit(城堡, (722, 100))
        
        if 敵方城堡_生命值 == 0:
            屏幕.blit(font.render(勝利, True, "yellow"), (381, 250))
        if 我方城堡_生命值 == 0:
            屏幕.blit(font.render(失敗, True, "black"), (381, 250))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# 主循环
while True:
    
    # 检查是否已经过了 0.5 秒
    if current_time - start_time >= 0.5:
        # 调用更新金钱函数
        更新金錢()
        #貓出擊()
        狗出擊()
        # 重置开始时间
        start_time = current_time

    # 獲取圖片信息
    倉鼠按鈕信息 = 屏幕.blit(倉鼠按鈕, (50, 400))
    金幣倉鼠按鈕信息 = 屏幕.blit(金幣倉鼠按鈕, (200, 400))
    盾牌倉鼠按鈕信息 = 屏幕.blit(盾牌倉鼠按鈕, (350, 400))  
    

    while True:
        更新金錢()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
       
        # 獲取滑鼠操作信息
        滑鼠點擊 = pygame.mouse.get_pressed()
        # 獲取滑鼠光標信息
        (mx, my) = pygame.mouse.get_pos()
       
        if 滑鼠點擊[0] and 倉鼠按鈕信息.collidepoint((mx, my)) and 按下標誌 == 0 and 錢 >= 50:
            倉鼠出擊()
            按下標誌 = 1
            錢 = 錢 - 50
            錢文字 = font.render(str(錢) + "/" + "1000", True, "black")
        elif 滑鼠點擊[0] and 金幣倉鼠按鈕信息.collidepoint((mx, my)) and 金幣按下標誌 == 0 and 錢 >= 100:
            金幣倉鼠出擊()
            金幣按下標誌 = 1
            金幣倉鼠數量 += 1
            錢 = 錢 - 100
            錢文字 = font.render(str(錢) + "/" + "1000", True, "black")
        elif 滑鼠點擊[0] and 盾牌倉鼠按鈕信息.collidepoint((mx, my)) and 金幣按下標誌 == 0 and 錢 >= 150:
            盾牌倉鼠出擊()
            盾牌按下標誌 = 1
            錢 = 錢 - 150
            錢文字 = font.render(str(錢) + "/" + "1000", True, "black")
        else:
            按下標誌 = 0
            金幣按下標誌 = 0
            盾牌按下標誌 = 0
        # 轉送
        屏幕.blit(背景, (0, 0))
        屏幕.blit(敵人城堡, (40, 100))
        屏幕.blit(城堡, (722, 100))
        
        if 錢 >= 150:
            屏幕.blit(倉鼠按鈕, (50, 400))
            屏幕.blit(金幣倉鼠按鈕, (200, 400))
            屏幕.blit(盾牌倉鼠按鈕, (350, 400))
        elif 錢 >= 100:
            屏幕.blit(倉鼠按鈕, (50, 400))
            屏幕.blit(金幣倉鼠按鈕, (200, 400))
        elif 錢 >= 50:
            屏幕.blit(倉鼠按鈕, (50, 400))
            
        屏幕.blit(敵方塔文字, (45, 90))
        屏幕.blit(我方塔文字, (722, 90))
        屏幕.blit(錢文字, (750,30))
        屏幕.blit(金幣, (700, 20))
       
   
        # 倉鼠的處理
        for i in reversed(range(len(倉鼠座標列表))):
            倉鼠 = 倉鼠座標列表[i]
            倉鼠血量 = 倉鼠血量列表[i]
    
            if 倉鼠.x > 180:
                倉鼠.x -= 6
                屏幕.blit(倉鼠列表[編號 % 4], 倉鼠)
        
                for j in reversed(range(len(貓座標列表))):
                    if j >= len(貓座標列表):
                        continue
                    貓 = 貓座標列表[j]
                    if abs(倉鼠.x - 貓.x) <= 60:
                        攻擊(倉鼠座標列表, 倉鼠血量列表, i, 倉鼠攻擊力, 攻擊列表, 貓座標列表, 貓血量列表, j, 貓攻擊力, 貓攻擊列表)
                    
                for j in reversed(range(len(狗座標列表))):
                    if j >= len(狗座標列表):
                        continue
                    狗 = 狗座標列表[j]
                    if abs(倉鼠.x - 狗.x) <= 60:
                        攻擊(倉鼠座標列表, 倉鼠血量列表, i, 倉鼠攻擊力, 攻擊列表, 狗座標列表, 狗血量列表, j, 狗攻擊力, 狗攻擊列表)

            else:
                if 敵方城堡_生命值 > 0:
                    攻擊x = random.randint(150, 180)
                    屏幕.blit(攻擊列表[編號 % 3], (攻擊x, 280, 0, 0))
                    敵方城堡_生命值 -= 1
                    敵方塔文字 = font.render(str(敵方城堡_生命值) + "/" + "10000", True, "black")
                else:
                    結束()
                    結束 = 1

        # 金幣倉鼠的處理
        for i in reversed(range(len(金幣倉鼠座標列表))):
            金幣倉鼠 = 金幣倉鼠座標列表[i]
            金幣倉鼠血量 = 金幣血量列表[i]
    
            if 金幣倉鼠.x > 180:
                金幣倉鼠.x -= 6
                屏幕.blit(金幣倉鼠列表[編號 % 4], 金幣倉鼠)
        
                for j in reversed(range(len(貓座標列表))):
                    if j >= len(貓座標列表):
                        continue
                    貓 = 貓座標列表[j]
                    if abs(金幣倉鼠.x - 貓.x) <= 60:
                        攻擊(金幣倉鼠座標列表, 金幣血量列表, i, 金幣攻擊力, 金幣攻擊列表, 貓座標列表, 貓血量列表, j, 貓攻擊力, 貓攻擊列表)
                    
                for j in reversed(range(len(狗座標列表))):
                    if j >= len(狗座標列表):
                        continue
                    狗 = 狗座標列表[j]
                    if abs(金幣倉鼠.x - 狗.x) <= 60:
                        攻擊(金幣倉鼠座標列表, 金幣血量列表, i, 金幣攻擊力, 金幣攻擊列表, 狗座標列表, 狗血量列表, j, 狗攻擊力, 狗攻擊列表)

            else:
                if 敵方城堡_生命值 > 0:
                    攻擊x = random.randint(150, 180)
                    屏幕.blit(金幣攻擊列表[編號 % 3], (攻擊x, 280, 0, 0))
                    敵方城堡_生命值 -= 1
                    敵方塔文字 = font.render(str(敵方城堡_生命值) + "/" + "10000", True, "black")
                else:
                    結束()
                    結束 = 1

        # 盾牌倉鼠的處理
        for i in reversed(range(len(盾牌倉鼠座標列表))):
            盾牌倉鼠 = 盾牌倉鼠座標列表[i]
            盾牌倉鼠血量 = 盾牌血量列表[i]
    
            if 盾牌倉鼠.x > 180:
                盾牌倉鼠.x -= 6
                屏幕.blit(盾牌倉鼠列表[編號 % 4], 盾牌倉鼠)
        
                for j in reversed(range(len(貓座標列表))):
                    if j >= len(貓座標列表):
                        continue
                    貓 = 貓座標列表[j]
                    if abs(盾牌倉鼠.x - 貓.x) <= 60:
                        攻擊(盾牌倉鼠座標列表, 盾牌血量列表, i, 盾牌攻擊力, 盾牌攻擊列表, 貓座標列表, 貓血量列表, j, 貓攻擊力, 貓攻擊列表)
                    
                for j in reversed(range(len(狗座標列表))):
                    if j >= len(狗座標列表):
                        continue
                    狗 = 狗座標列表[j]
                    if abs(盾牌倉鼠.x - 狗.x) <= 60:
                        攻擊(盾牌倉鼠座標列表, 盾牌血量列表, i, 盾牌攻擊力, 盾牌攻擊列表, 狗座標列表, 狗血量列表, j, 狗攻擊力, 狗攻擊列表)

            else:
                if 敵方城堡_生命值 > 0:
                    攻擊x = random.randint(150, 180)
                    屏幕.blit(盾牌攻擊列表[編號 % 3], (攻擊x, 280, 0, 0))
                    敵方城堡_生命值 -= 1
                    敵方塔文字 = font.render(str(敵方城堡_生命值) + "/" + "10000", True, "black")
                else:
                    結束()
                    結束 = 1

        # 貓的處理
        for i in reversed(range(len(貓座標列表))):
            貓 = 貓座標列表[i]
            貓血量 = 貓血量列表[i]

            if 貓.x < 722:  # 假設722是敵方城堡的位置
                貓.x += 6
                屏幕.blit(貓列表[編號 % 4], 貓)

                for j in reversed(range(len(倉鼠座標列表))):
                    if j >= len(倉鼠座標列表):
                        continue
                    倉鼠 = 倉鼠座標列表[j]
                    if abs(貓.x - 倉鼠.x) <= 60:
                        攻擊(貓座標列表, 貓血量列表, i, 貓攻擊力, 貓攻擊列表, 倉鼠座標列表, 倉鼠血量列表, j, 倉鼠攻擊力, 攻擊列表)

                for j in reversed(range(len(金幣倉鼠座標列表))):
                    if j >= len(金幣倉鼠座標列表):
                        continue
                    金幣倉鼠 = 金幣倉鼠座標列表[j]
                    if abs(貓.x - 金幣倉鼠.x) <= 60:
                        攻擊(貓座標列表, 貓血量列表, i, 貓攻擊力, 貓攻擊列表, 金幣倉鼠座標列表, 金幣血量列表, j, 金幣攻擊力, 金幣攻擊列表)

                for j in reversed(range(len(盾牌倉鼠座標列表))):
                    if j >= len(盾牌倉鼠座標列表):
                        continue
                    盾牌倉鼠 = 盾牌倉鼠座標列表[j]
                    if abs(貓.x - 盾牌倉鼠.x) <= 60:
                        攻擊(貓座標列表, 貓血量列表, i, 貓攻擊力, 貓攻擊列表, 盾牌倉鼠座標列表, 盾牌血量列表, j, 盾牌攻擊力, 盾牌攻擊列表)

            else:
                if 我方城堡_生命值 > 0:
                    攻擊x = random.randint(632, 662)
                    屏幕.blit(貓攻擊列表[編號 % 2], (攻擊x, 280, 0, 0))
                    我方城堡_生命值 -= 1
                    我方塔文字 = font.render(str(我方城堡_生命值) + "/" + "10000", True, "black")
                else:
                    結束()
                    結束 = 1

                        
        if 結束 == 1:
            break

        # 狗的處理
        for i in reversed(range(len(狗座標列表))):
            狗 = 狗座標列表[i]
            狗血量 = 狗血量列表[i]

            if 狗.x < 722:  # 假設722是敵方城堡的位置
                狗.x += 6
                屏幕.blit(狗列表[編號 % 4], 狗)

                for j in reversed(range(len(倉鼠座標列表))):
                    if j >= len(倉鼠座標列表):
                        continue
                    倉鼠 = 倉鼠座標列表[j]
                    if abs(狗.x - 倉鼠.x) <= 60:
                        攻擊(狗座標列表, 狗血量列表, i, 狗攻擊力, 狗攻擊列表, 倉鼠座標列表, 倉鼠血量列表, j, 倉鼠攻擊力, 攻擊列表)

                for j in reversed(range(len(金幣倉鼠座標列表))):
                    if j >= len(金幣倉鼠座標列表):
                        continue
                    金幣倉鼠 = 金幣倉鼠座標列表[j]
                    if abs(狗.x - 金幣倉鼠.x) <= 60:
                        攻擊(狗座標列表, 狗血量列表, i, 狗攻擊力, 狗攻擊列表, 金幣倉鼠座標列表, 金幣血量列表, j, 金幣攻擊力, 金幣攻擊列表)

                for j in reversed(range(len(盾牌倉鼠座標列表))):
                    if j >= len(盾牌倉鼠座標列表):
                        continue
                    盾牌倉鼠 = 盾牌倉鼠座標列表[j]
                    if abs(狗.x - 盾牌倉鼠.x) <= 60:
                        攻擊(狗座標列表, 狗血量列表, i, 狗攻擊力, 狗攻擊列表, 盾牌倉鼠座標列表, 盾牌血量列表, j, 盾牌攻擊力, 盾牌攻擊列表)

            else:
                if 我方城堡_生命值 > 0:
                    攻擊x = random.randint(632, 662)
                    屏幕.blit(狗攻擊列表[編號 % 2], (攻擊x, 280, 0, 0))
                    我方城堡_生命值 -= 1
                    我方塔文字 = font.render(str(我方城堡_生命值) + "/" + "10000", True, "black")
                else:
                    結束()
                    結束 = 1

                        
        if 結束 == 1:
            break
    
        錢文字 = font.render(str(錢) + "/" + "1000", True, "black")
        更新區域 = pygame.Rect(722, 0, 200, 50)  # 假設金錢顯示的位置在(722, 0)，並且文本大小不超過(200, 50)
        屏幕.blit(背景, 更新區域, 更新區域)
        屏幕.blit(錢文字, (750, 30))
        屏幕.blit(金幣, (700, 20))
    
        # 更新顯示
        pygame.display.update()
   
        # 處理速度
        pygame.time.Clock().tick(15)