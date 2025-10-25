import pygame
import sys
import random
import time
import subprocess
import cv2

def 更新金錢():
    global 錢, 錢文字
    if 錢 < 1000:
        if 金幣倉鼠數量 > 0:
            錢 = 錢 + 1 + 金幣倉鼠數量
        else:
            錢 += 1
    else:
        錢  = 1000
    錢文字 = font.render(str(錢) + "/" + "1000", True, "black")

def 更新按鈕():
    屏幕.blit(暫停按鈕, (10, 10))
    if 錢 >= 300:
        屏幕.blit(邱比特按鈕, (650, 400))
        屏幕.blit(font_15.render("$300", True, "black"), (695, 455))
    else:
        屏幕.blit(邱比特按鈕_灰階, (650, 400))
        屏幕.blit(font_15.render("$300", True, "black"), (695, 455))
    if 錢 >= 200:
        屏幕.blit(弓箭手按鈕, (500, 400))
        屏幕.blit(font_15.render("$200", True, "black"), (545, 455))
    else:
        屏幕.blit(弓箭手按鈕_灰階, (500, 400))
        屏幕.blit(font_15.render("$200", True, "black"), (545, 455))
    if 錢 >= 150:
        屏幕.blit(盾牌倉鼠按鈕, (350, 400))
        屏幕.blit(font_15.render("$150", True, "black"), (395, 455))
    else:
        屏幕.blit(盾牌倉鼠按鈕_灰階, (350, 400))
        屏幕.blit(font_15.render("$150", True, "black"), (395, 455))
    if 錢 >= 100:
        屏幕.blit(金幣倉鼠按鈕, (200, 400))
        屏幕.blit(font_15.render("$100", True, "black"), (245, 455))
    else:
        屏幕.blit(金幣倉鼠按鈕_灰階, (200, 400))
        屏幕.blit(font_15.render("$100", True, "black"), (245, 455))
    if 錢 >= 50:
        屏幕.blit(倉鼠按鈕, (50, 400))
        屏幕.blit(font_15.render("$50", True, "black"), (105, 455))
    else:
        屏幕.blit(倉鼠按鈕_灰階, (50, 400))
        屏幕.blit(font_15.render("$50", True, "black"), (105, 455))

start_time = time.time()
current_time = time.time()
last_cat_attack_time = time.time()
last_dog_attack_time = time.time()
last_bird_attack_time = time.time()


按下標誌 = 0
金幣按下標誌 = 0
盾牌按下標誌 = 0
弓箭手按下標誌 = 0
邱比特按下標誌 = 0

h_arrow = 0
h_cupid = 0

編號 = 0
倉鼠座標 = pygame.Rect(722, 280, 0, 0)
金幣倉鼠數量 = 0
錢 = 50
勝利 = "You Win!!"
失敗 = "You Lose..."
結束 = 0
暫停狀態 = False


pygame.init()


視窗寬度 = 922
視窗高度 = 499
屏幕 = pygame.display.set_mode((視窗寬度, 視窗高度))
屏幕.fill("white")


BGM=pygame.mixer.Sound("audio/bgm.wav")
BGM.play(-1)
選擇 = pygame.mixer.Sound("audio/choose.mp3")
爆炸 = pygame.mixer.Sound("audio/explosion.mp3")
塔被攻擊 = pygame.mixer.Sound("audio/tower_attack.mp3")
倉鼠出現 = pygame.mixer.Sound("audio/appear.mp3")
倉鼠攻擊 = pygame.mixer.Sound("audio/hamster_attack.mp3")
金幣攻擊 = pygame.mixer.Sound("audio/coin_attack.mp3")
盾牌攻擊 = pygame.mixer.Sound("audio/defense_attack.mp3")
射擊 = pygame.mixer.Sound("audio/shoot.mp3")
貓出現 = pygame.mixer.Sound("audio/cat_appear.mp3")
貓攻擊 = pygame.mixer.Sound("audio/cat_attack.mp3")
狗出現 = pygame.mixer.Sound("audio/dog_appear.mp3")
狗攻擊 = pygame.mixer.Sound("audio/dog_attack.mp3")
鳥出現 = pygame.mixer.Sound("audio/bird_appear.mp3")
鳥攻擊 = pygame.mixer.Sound("audio/bird_attack.mp3")
死亡 = pygame.mixer.Sound("audio/dead.mp3")


背景 = pygame.image.load("image/背景.jpg")
背景 = pygame.transform.scale(背景, (視窗寬度, 視窗高度))
暫停按鈕 = pygame.image.load("image/pause.png")
開始按鈕 = pygame.image.load("image/start.png")
退出按鈕 = pygame.image.load("image/button_exit.png")
敵人城堡 = pygame.image.load("image/敵堡.png")
城堡 = pygame.image.load("image/我堡.png")
倉鼠按鈕 = pygame.image.load("image/button_hamster.png")
金幣倉鼠按鈕 = pygame.image.load("image/button_coin.png")
盾牌倉鼠按鈕 = pygame.image.load("image/button_defense.png")
弓箭手按鈕 = pygame.image.load("image/button_archer.png")
邱比特按鈕 = pygame.image.load("image/button_cupid.png")

倉鼠按鈕_gray = cv2.imread("./image/button_hamster.png", cv2.IMREAD_UNCHANGED)
倉鼠按鈕_gray = cv2.cvtColor(倉鼠按鈕_gray, cv2.COLOR_BGR2GRAY)

金幣倉鼠按鈕_gray = cv2.imread("./image/button_coin.png", cv2.IMREAD_UNCHANGED)
金幣倉鼠按鈕_gray = cv2.cvtColor(金幣倉鼠按鈕_gray, cv2.COLOR_BGR2GRAY)

盾牌倉鼠按鈕_gray = cv2.imread("./image/button_defense.png", cv2.IMREAD_UNCHANGED)
盾牌倉鼠按鈕_gray = cv2.cvtColor(盾牌倉鼠按鈕_gray, cv2.COLOR_BGR2GRAY)

弓箭手按鈕_gray = cv2.imread("./image/button_archer.png", cv2.IMREAD_UNCHANGED)
弓箭手按鈕_gray = cv2.cvtColor(弓箭手按鈕_gray, cv2.COLOR_BGR2GRAY)

邱比特按鈕_gray = cv2.imread("./image/button_cupid.png", cv2.IMREAD_UNCHANGED)
邱比特按鈕_gray = cv2.cvtColor(邱比特按鈕_gray, cv2.COLOR_BGR2GRAY)

cv2.imwrite('./image/button_hamster_gray.png', 倉鼠按鈕_gray)
cv2.imwrite('./image/button_coin_gray.png', 金幣倉鼠按鈕_gray)
cv2.imwrite('./image/button_defense_gray.png', 盾牌倉鼠按鈕_gray)
cv2.imwrite('./image/button_archer_gray.png', 弓箭手按鈕_gray)
cv2.imwrite('./image/button_cupid_gray.png', 邱比特按鈕_gray)

倉鼠按鈕_灰階 = pygame.image.load("image/button_hamster_gray.png")
金幣倉鼠按鈕_灰階 = pygame.image.load("image/button_coin_gray.png")
盾牌倉鼠按鈕_灰階 = pygame.image.load("image/button_defense_gray.png")
弓箭手按鈕_灰階 = pygame.image.load("image/button_archer_gray.png")
邱比特按鈕_灰階 = pygame.image.load("image/button_cupid_gray.png")

金幣 = pygame.image.load("image/coin.png")
弓箭手弓箭 = pygame.image.load("image/archer_arrow.png")
邱比特弓箭 = pygame.image.load("image/cupid_arrow.png")


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
鳥走動1 = pygame.image.load("image/bird_walk1.png")
鳥走動2 = pygame.image.load("image/bird_walk2.png")
鳥超愛1 = pygame.image.load("image/bbb.png")
鳥超愛2 = pygame.image.load("image/bird_love2.png")
弓箭手 = pygame.image.load("image/archer.png")
邱比特 = pygame.image.load("image/cupid.png")

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
弓箭手攻擊1 = pygame.image.load("image/archer_attack1.png")
弓箭手攻擊2 = pygame.image.load("image/archer_attack2.png")
弓箭手攻擊3 = pygame.image.load("image/archer_attack3.png")
弓箭手攻擊4 = pygame.image.load("image/archer_attack4.png")
邱比特攻擊1 = pygame.image.load("image/cupid_attack1.png")
邱比特攻擊2 = pygame.image.load("image/cupid_attack2.png")
邱比特攻擊3 = pygame.image.load("image/cupid_attack3.png")
邱比特攻擊4 = pygame.image.load("image/cupid_attack4.png")

敵人城堡 = pygame.transform.scale(敵人城堡, (180, 320))
城堡 = pygame.transform.scale(城堡, (180, 320))

暫停按鈕 = pygame.transform.scale(暫停按鈕, (50, 50))
開始按鈕 = pygame.transform.scale(開始按鈕, (150, 150))
退出按鈕 = pygame.transform.scale(退出按鈕, (150, 60))
倉鼠按鈕 = pygame.transform.scale(倉鼠按鈕, (100, 80))
金幣倉鼠按鈕 = pygame.transform.scale(金幣倉鼠按鈕, (100, 80))
盾牌倉鼠按鈕 = pygame.transform.scale(盾牌倉鼠按鈕, (100, 80))
弓箭手按鈕 = pygame.transform.scale(弓箭手按鈕, (100, 80))
邱比特按鈕 = pygame.transform.scale(邱比特按鈕, (100, 80))

倉鼠按鈕_灰階 = pygame.transform.scale(倉鼠按鈕_灰階, (100, 80))
金幣倉鼠按鈕_灰階 = pygame.transform.scale(金幣倉鼠按鈕_灰階, (100, 80))
盾牌倉鼠按鈕_灰階 = pygame.transform.scale(盾牌倉鼠按鈕_灰階, (100, 80))
弓箭手按鈕_灰階 = pygame.transform.scale(弓箭手按鈕_灰階, (100, 80))
邱比特按鈕_灰階 = pygame.transform.scale(邱比特按鈕_灰階, (100, 80))

金幣 = pygame.transform.scale(金幣, (40, 40))
弓箭手弓箭 = pygame.transform.scale(弓箭手弓箭, (150, 150))
邱比特弓箭 = pygame.transform.scale(邱比特弓箭, (150, 150))

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

鳥走動1 = pygame.transform.scale(鳥走動1, (150, 150))
鳥走動2 = pygame.transform.scale(鳥走動2, (150, 150))

鳥超愛1 = pygame.transform.scale(鳥超愛1, (150, 150))
鳥超愛2 = pygame.transform.scale(鳥超愛2, (150, 150))

弓箭手 = pygame.transform.scale(弓箭手, (150, 150))
邱比特 = pygame.transform.scale(邱比特, (150, 150))


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

弓箭手攻擊1 = pygame.transform.scale(弓箭手攻擊1, (150, 150))
弓箭手攻擊2 = pygame.transform.scale(弓箭手攻擊2, (150, 150))
弓箭手攻擊3 = pygame.transform.scale(弓箭手攻擊3, (150, 150))
弓箭手攻擊4 = pygame.transform.scale(弓箭手攻擊4, (150, 150))
邱比特攻擊1 = pygame.transform.scale(邱比特攻擊1, (150, 150))
邱比特攻擊2 = pygame.transform.scale(邱比特攻擊2, (150, 150))
邱比特攻擊3 = pygame.transform.scale(邱比特攻擊3, (150, 150))
邱比特攻擊4 = pygame.transform.scale(邱比特攻擊4, (150, 150))

倉鼠走動列表 = [走動1, 走動2, 走動3, 走動4]
金幣倉鼠走動列表 = [金幣走動1, 金幣走動2, 金幣走動3, 金幣走動4]
盾牌倉鼠走動列表 = [盾牌走動1, 盾牌走動2, 盾牌走動3, 盾牌走動4]
貓走動列表 = [貓走動1, 貓走動2, 貓走動3, 貓走動4]
狗走動列表 = [狗走動1, 狗走動2, 狗走動3, 狗走動4]
鳥走動列表 = [鳥走動1, 鳥走動2]
弓箭手走動列表 = [弓箭手攻擊1, 弓箭手攻擊2]
邱比特走動列表 = [邱比特攻擊1, 邱比特攻擊2]


font = pygame.font.Font("k12x8.ttf", 20)
font_15 = pygame.font.Font("k12x8.ttf", 15)
敵方塔文字 = font.render("∞/∞", True, "black")
我方塔文字 = font.render("∞/∞", True, "black")


敵人列表 = []
倉鼠列表 = []
敵人特殊角色列表 = []
倉鼠特殊角色列表 = []

class 角色:
    def __init__(self, 類型, 座標, 血量, 攻擊力, 移動次數):
        self.類型 = 類型
        self.座標 = pygame.Rect(座標[0], 座標[1], 座標[2], 座標[3])
        self.血量 = 血量
        self.攻擊力 = 攻擊力
        self.移動次數 = 移動次數
        self.最遠座標 = None
        self.圖片索引 = 0

class 鳥角色:
    def __init__(self, 座標, 血量, 移動次數):
        self.座標 = pygame.Rect(座標[0], 座標[1], 座標[2], 座標[3])
        self.血量 = 血量
        self.移動次數 = 移動次數
        self.魅惑 = False
        self.停留開始時間 = None

class 倉鼠角色:
    def __init__(self, 類型, 座標, 血量, 移動次數):
        self.類型 = 類型
        self.座標 = pygame.Rect(座標[0], 座標[1], 座標[2], 座標[3])
        self.血量 = 血量
        self.移動次數 = 移動次數
       
       
def 倉鼠出擊():
    倉鼠列表.append(角色('倉鼠', (722, 280, 0, 0), 1000, 3, 0))
def 金幣出擊():
    倉鼠列表.append(角色('金幣倉鼠', (722, 280, 0, 0), 500, 1, 0))
def 盾牌出擊():
    倉鼠列表.append(角色('盾牌倉鼠', (722, 280, 0, 0), 1500, 2, 0))
def 貓出擊():
    敵人列表.append(角色('貓', (180, 280, 0, 0), 500, 3, 0))
def 狗出擊():
    敵人列表.append(角色('狗', (180, 280, 0, 0), 1000, 5, 0))
def 鳥出擊():
    敵人特殊角色列表.append(鳥角色((0, 10, 0, 0), 200, 0))
def 弓箭手出擊():
    global h_arrow
    h_arrow = 1
    倉鼠特殊角色列表.append(倉鼠角色('弓箭手', (730, 150, 0, 0), 200, 0))
def 邱比特出擊():
    global h_cupid
    h_cupid = 1
    倉鼠特殊角色列表.append(倉鼠角色('邱比特', (730, 150, 0, 0), 200, 0))


def 倉鼠行動():
    global 敵方塔文字, 敵方城堡_生命值, 結束, h1, h2
    for 倉鼠 in 倉鼠列表:
        if 倉鼠.血量 > 0:
            目標座標 = 150 if 倉鼠.最遠座標 is None else 倉鼠.最遠座標
            if 倉鼠.座標.x > 目標座標:
                倉鼠.座標.x -= 6
            elif 倉鼠.座標.x >= 目標座標:
                倉鼠.最遠座標 = None
            for 敵人 in 敵人列表:
                if abs(倉鼠.座標.x - 敵人.座標.x) <= 60:
                    倉鼠.最遠座標 = 倉鼠.座標.x
                    h1 = 倉鼠.最遠座標 - 30
                    h2 = 倉鼠.最遠座標
                    攻擊(倉鼠, 敵人)
            if 倉鼠.座標.x <= 150:
                倉鼠.最遠座標 = 倉鼠.座標.x
                h1 = 150
                h2 = 180
                攻擊x = random.randint(h1, h2)
                倉鼠.座標.x = 攻擊x
                塔被攻擊.play(0)
                倉鼠.最遠座標 = 倉鼠.座標.x
                敵方塔文字 = font.render("∞/∞", True, "black")
               

def 敵人行動():
    global 我方塔文字, 我方城堡_生命值, 結束, x1, x2
    for 敵人 in 敵人列表:
        if 敵人.血量 > 0:
            目標座標 = 722 if 敵人.最遠座標 is None else 敵人.最遠座標
            if 敵人.座標.x < 目標座標:
                敵人.座標.x += 6
            elif 敵人.座標.x <= 目標座標:
                敵人.最遠座標 = None
            for 倉鼠 in 倉鼠列表:
                if abs(敵人.座標.x - 倉鼠.座標.x) <= 60:
                    敵人.最遠座標 = 敵人.座標.x
                    x1 = 敵人.最遠座標 - 30
                    x2 = 敵人.最遠座標
                    攻擊(敵人, 倉鼠)
            if 敵人.座標.x >= 722:
                敵人.最遠座標 = 敵人.座標.x
                x1 = 632
                x2 = 662
                攻擊x = random.randint(x1, x2)
                敵人.座標.x = 攻擊x
                塔被攻擊.play(0)
                我方塔文字 = font.render("∞/∞", True, "black")

def 鳥行動():
    global h_arrow, h_cupid, 金幣倉鼠數量
    目標座標 = 360

    for 鳥 in 敵人特殊角色列表:
        if 鳥.血量 > 0:
            if 鳥.座標.x < 目標座標:
                鳥.座標.x += 6
                鳥.停留開始時間 = None
            elif 鳥.座標.x == 目標座標 and 鳥.停留開始時間 is None:
                    鳥.停留開始時間 = time.time()
            elif 鳥.座標.x == 目標座標 and time.time() - 鳥.停留開始時間 >= 5:
                if 鳥.魅惑 is False:
                    鳥攻擊.play(0)
                    金幣倉鼠數量 = 0
                    倉鼠列表.clear()
                    倉鼠特殊角色列表.clear()
                    敵人列表.clear()
                    h_arrow = 0
                    h_cupid = 0
                    鳥.座標.x += 6                        
                else:
                   
                    鳥.座標.x += 6
            elif 鳥.座標.x > 目標座標 and 鳥.座標.x <= 視窗寬度:
                鳥.座標.x += 6

def 更新遊戲():
    倉鼠行動()
    敵人行動()
    鳥行動()

def 攻擊(攻擊者, 被攻擊者):
    global 金幣倉鼠數量
    if 攻擊者.類型 == '倉鼠':
        倉鼠攻擊.play(0)
    elif 攻擊者.類型 == '金幣倉鼠':
        金幣攻擊.play(0)
    elif 攻擊者.類型 == '盾牌倉鼠':
        盾牌攻擊.play(0)
    elif 攻擊者.類型 == '狗':
        狗攻擊.play(0)
    elif 攻擊者.類型 == '貓':
        貓攻擊.play(0)
    被攻擊者.血量 -= 攻擊者.攻擊力
    if 被攻擊者.血量 <= 0:
        if 被攻擊者 in 敵人列表:
            死亡.play(0)
            敵人列表.remove(被攻擊者)
        else:
            if 被攻擊者.類型 == '金幣倉鼠':
                金幣倉鼠數量 -= 1
            死亡.play(0)
            倉鼠列表.remove(被攻擊者)
        攻擊者.最遠座標 = None


def 結束():
    while True:
        pygame.display.update()
        屏幕.blit(背景, (0, 0))
        屏幕.blit(敵人城堡, (40, 100))
        屏幕.blit(城堡, (722, 100))
            
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.quit()
        subprocess.run(["python", "hamster.py"])
        sys.exit()


while True:
    if current_time - start_time >= 0.5:
        更新金錢()
        更新遊戲()
        start_time = current_time
       
    暫停按鈕信息 = 屏幕.blit(暫停按鈕, (10, 10))
    退出按鈕信息 = 屏幕.blit(退出按鈕, (770, 400))
    倉鼠按鈕信息 = 屏幕.blit(倉鼠按鈕, (50, 400))
    金幣倉鼠按鈕信息 = 屏幕.blit(金幣倉鼠按鈕, (200, 400))
    盾牌倉鼠按鈕信息 = 屏幕.blit(盾牌倉鼠按鈕, (350, 400))
    弓箭手按鈕信息 = 屏幕.blit(弓箭手按鈕, (500, 400))
    邱比特按鈕信息 = 屏幕.blit(邱比特按鈕, (650, 400))
   

    while True:
        current_time = time.time()
        更新金錢()
        更新遊戲()
        if current_time - last_cat_attack_time >= 10:
            貓出現.play(0)
            貓出擊()
            last_cat_attack_time = current_time

        if current_time - last_dog_attack_time >= 20:
            狗出現.play(0)
            狗出擊()
            last_dog_attack_time = current_time
           
        if current_time - last_bird_attack_time >= 30:
            鳥出現.play(0)
            鳥出擊()
            last_bird_attack_time = current_time
           
        更新遊戲()
        更新金錢()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
       
        滑鼠點擊 = pygame.mouse.get_pressed()
        (mx, my) = pygame.mouse.get_pos()

        if 暫停狀態:
            開始按鈕信息 = 屏幕.blit(開始按鈕, (386, 174.5))
            退出按鈕信息 = 屏幕.blit(退出按鈕, (770, 400))
            屏幕.blit(font.render("EXIT", True, "white"), (820, 422))
            pygame.display.update()
        
            while 暫停狀態:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (mx, my) = pygame.mouse.get_pos()
                        if 退出按鈕信息.collidepoint((mx, my)):
                            選擇.play(0)
                            pygame.time.delay(300)
                            pygame.quit()
                            subprocess.run(["python", "hamster.py"])
                            sys.exit()
                        if 開始按鈕信息.collidepoint((mx, my)):
                            選擇.play(0)
                            暫停狀態 = False
        if 滑鼠點擊[0] and 暫停按鈕信息.collidepoint((mx, my)):
            選擇.play(0)
            暫停狀態 = True

        if 滑鼠點擊[0] and 倉鼠按鈕信息.collidepoint((mx, my)) and 按下標誌 == 0 and 錢 >= 50:
            倉鼠出現.play(0)
            倉鼠出擊()
            按下標誌 = 1
            錢 = 錢 - 50
            錢文字 = font.render(str(錢) + "/" + "1000", True, "black")
        elif 滑鼠點擊[0] and 金幣倉鼠按鈕信息.collidepoint((mx, my)) and 金幣按下標誌 == 0 and 錢 >= 100:
            倉鼠出現.play(0)
            金幣出擊()
            金幣按下標誌 = 1
            金幣倉鼠數量 += 1
            錢 = 錢 - 100
            錢文字 = font.render(str(錢) + "/" + "1000", True, "black")
        elif 滑鼠點擊[0] and 盾牌倉鼠按鈕信息.collidepoint((mx, my)) and 盾牌按下標誌 == 0 and 錢 >= 150:
            倉鼠出現.play(0)
            盾牌出擊()
            盾牌按下標誌 = 1
            錢 = 錢 - 150
            錢文字 = font.render(str(錢) + "/" + "1000", True, "black")
        elif 滑鼠點擊[0] and 弓箭手按鈕信息.collidepoint((mx, my)) and 弓箭手按下標誌 == 0 and 錢 >= 200 and h_arrow == 0 and h_cupid == 0:
            倉鼠出現.play(0)
            弓箭手出擊()
            弓箭手按下標誌 = 1
            錢 = 錢 - 200
            錢文字 = font.render(str(錢) + "/" + "1000", True, "black")
        elif 滑鼠點擊[0] and 邱比特按鈕信息.collidepoint((mx, my)) and 邱比特按下標誌 == 0 and 錢 >= 300 and h_arrow == 0 and h_cupid == 0:
            倉鼠出現.play(0)
            邱比特出擊()
            邱比特按下標誌 = 1
            錢 = 錢 - 300
            錢文字 = font.render(str(錢) + "/" + "1000", True, "black")
        else:
            按下標誌 = 0
            金幣按下標誌 = 0
            盾牌按下標誌 = 0
            弓箭手按下標誌 = 0
            邱比特按下標誌 = 0

        屏幕.blit(背景, (0, 0))
        屏幕.blit(敵人城堡, (40, 100))
        屏幕.blit(城堡, (722, 100))

        for 倉鼠 in 倉鼠列表:
            if 倉鼠.座標.x >= 150:
                if 倉鼠.類型 == '倉鼠':
                    if 倉鼠.最遠座標 == None:
                        if 倉鼠.移動次數 % 8 == 0 or 倉鼠.移動次數 % 8 == 1:
                            屏幕.blit(走動1, (倉鼠.座標[0], 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 8 == 2 or 倉鼠.移動次數 % 8 == 3:
                            屏幕.blit(走動2, (倉鼠.座標[0], 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 8 == 4 or 倉鼠.移動次數 % 8 == 5:
                            屏幕.blit(走動3, (倉鼠.座標[0], 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 8 == 6 or 倉鼠.移動次數 % 8 == 7:
                            屏幕.blit(走動4, (倉鼠.座標[0], 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                    else:
                        if 倉鼠.移動次數 % 3 == 0:
                            屏幕.blit(攻擊1, (random.randint(h1, h2), 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 3 == 1:
                            屏幕.blit(攻擊2, (random.randint(h1, h2), 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 3 == 2:
                            屏幕.blit(攻擊3, (random.randint(h1, h2), 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                elif 倉鼠.類型 == '金幣倉鼠':
                    if 倉鼠.最遠座標 == None:
                        if 倉鼠.移動次數 % 8 == 0 or 倉鼠.移動次數 % 8 == 1:
                            屏幕.blit(金幣走動1, (倉鼠.座標[0], 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 8 == 2 or 倉鼠.移動次數 % 8 == 3:
                            屏幕.blit(金幣走動2, (倉鼠.座標[0], 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 8 == 4 or 倉鼠.移動次數 % 8 == 5:
                            屏幕.blit(金幣走動3, (倉鼠.座標[0], 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 8 == 6 or 倉鼠.移動次數 % 8 == 7:
                            屏幕.blit(金幣走動4, (倉鼠.座標[0], 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                    else:
                        if 倉鼠.移動次數 % 3 == 0:
                            屏幕.blit(金幣攻擊1, (random.randint(h1, h2), 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 3 == 1:
                            屏幕.blit(金幣攻擊2, (random.randint(h1, h2), 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 3 == 2:
                            屏幕.blit(金幣攻擊3, (random.randint(h1, h2), 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                elif 倉鼠.類型 == '盾牌倉鼠':
                    if 倉鼠.最遠座標 == None:
                        if 倉鼠.移動次數 % 8 == 0 or 倉鼠.移動次數 % 8 == 1:
                            屏幕.blit(盾牌走動1, (倉鼠.座標[0], 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 8 == 2 or 倉鼠.移動次數 % 8 == 3:
                            屏幕.blit(盾牌走動2, (倉鼠.座標[0], 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 8 == 4 or 倉鼠.移動次數 % 8 == 5:
                            屏幕.blit(盾牌走動3, (倉鼠.座標[0], 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 8 == 6 or 倉鼠.移動次數 % 8 == 7:
                            屏幕.blit(盾牌走動4, (倉鼠.座標[0], 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                    else:
                        if 倉鼠.移動次數 % 3 == 0:
                            屏幕.blit(盾牌攻擊1, (random.randint(h1, h2), 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 3 == 1:
                            屏幕.blit(盾牌攻擊2, (random.randint(h1, h2), 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1
                        elif 倉鼠.移動次數 % 3 == 2:
                            屏幕.blit(盾牌攻擊3, (random.randint(h1, h2), 倉鼠.座標[1]))
                            倉鼠.移動次數 += 1

        for 敵人 in 敵人列表:
            if 敵人.座標.x <= 722:
                if 敵人.類型 == '貓':
                    if 敵人.最遠座標 == None:
                        if 敵人.移動次數 % 8 == 0 or 敵人.移動次數 % 8 == 1:
                            屏幕.blit(貓走動1, (敵人.座標[0], 敵人.座標[1]))
                            敵人.移動次數 += 1
                        elif 敵人.移動次數 % 8 == 2 or 敵人.移動次數 % 8 == 3:
                            屏幕.blit(貓走動2, (敵人.座標[0], 敵人.座標[1]))
                            敵人.移動次數 += 1
                        elif 敵人.移動次數 % 8 == 4 or 敵人.移動次數 % 8 == 5:
                            屏幕.blit(貓走動3, (敵人.座標[0], 敵人.座標[1]))
                            敵人.移動次數 += 1
                        elif 敵人.移動次數 % 8 == 6 or 敵人.移動次數 % 8 == 7:
                            屏幕.blit(貓走動4, (敵人.座標[0], 敵人.座標[1]))
                            敵人.移動次數 += 1
                    else:
                        if 敵人.移動次數 % 2 == 0:
                            屏幕.blit(貓攻擊1, (random.randint(x1, x2), 敵人.座標[1]))
                            敵人.移動次數 += 1
                        elif 敵人.移動次數 % 2 == 1:
                            屏幕.blit(貓攻擊2, (random.randint(x1, x2), 敵人.座標[1]))
                            敵人.移動次數 += 1
                       
                elif 敵人.類型 == '狗':
                    if 敵人.最遠座標 == None:
                        if 敵人.移動次數 % 8 == 0 or 敵人.移動次數 % 8 == 1:
                            屏幕.blit(狗走動1, (敵人.座標[0], 敵人.座標[1]))
                            敵人.移動次數 += 1
                        elif 敵人.移動次數 % 8 == 2 or 敵人.移動次數 % 8 == 3:
                            屏幕.blit(狗走動2, (敵人.座標[0], 敵人.座標[1]))
                            敵人.移動次數 += 1
                        elif 敵人.移動次數 % 8 == 4 or 敵人.移動次數 % 8 == 5:
                            屏幕.blit(狗走動3, (敵人.座標[0], 敵人.座標[1]))
                            敵人.移動次數 += 1
                        elif 敵人.移動次數 % 8 == 6 or 敵人.移動次數 % 8 == 7:
                            屏幕.blit(狗走動4, (敵人.座標[0], 敵人.座標[1]))
                            敵人.移動次數 += 1
                    else:
                        if 敵人.移動次數 % 2 == 0:
                            屏幕.blit(狗攻擊1, (random.randint(x1, x2), 敵人.座標[1]))
                            敵人.移動次數 += 1
                        elif 敵人.移動次數 % 2 == 1:
                            屏幕.blit(狗攻擊2, (random.randint(x1, x2), 敵人.座標[1]))
                            敵人.移動次數 += 1

        for 鳥 in 敵人特殊角色列表:
            if 鳥.魅惑 == False:
                if 鳥.座標.x <= 922:
                    if 鳥.移動次數 % 4 == 0 or 鳥.移動次數 % 4 == 1:
                        屏幕.blit(鳥走動1, (鳥.座標[0], 鳥.座標[1]))
                        鳥.移動次數 += 1
                    else:
                        屏幕.blit(鳥走動2, (鳥.座標[0], 鳥.座標[1]))
                        鳥.移動次數 += 1
            else:
                if 鳥.座標.x == 360:
                    if 鳥.移動次數 % 5 <= 1:
                        屏幕.blit(鳥超愛2, (鳥.座標[0], 鳥.座標[1]))
                        鳥.移動次數 += 1
                    elif 鳥.移動次數 % 5 <= 3:
                        屏幕.blit(鳥超愛1, (鳥.座標[0], 鳥.座標[1]))
                        鳥.移動次數 += 1
                    else:
                        屏幕.blit(鳥超愛2, (鳥.座標[0], 鳥.座標[1]))
                        敵人列表.clear()
                        鳥.移動次數 = 0
                        鳥.座標.x += 6
                else:
                    if 鳥.移動次數 % 4 == 0 or 鳥.移動次數 % 4 == 1:
                        屏幕.blit(鳥超愛1, (鳥.座標[0], 鳥.座標[1]))
                        鳥.移動次數 += 1
                    else:
                        屏幕.blit(鳥超愛2, (鳥.座標[0], 鳥.座標[1]))
                        鳥.移動次數 += 1
                    if (鳥.座標.x + 6) == 360:
                        鳥.移動次數 = 0
                   
        for 特殊倉鼠 in 倉鼠特殊角色列表:
            if 特殊倉鼠.類型 == '弓箭手':
                目標在範圍內 = False
                for 鳥 in 敵人特殊角色列表:
                    if 鳥.座標.x == 360:
                        目標在範圍內 = True
                        break
               
                if 目標在範圍內:
                    射擊.play(0)
                    if 特殊倉鼠.移動次數 % 16 == 0 or 特殊倉鼠.移動次數 % 16 == 1:
                        屏幕.blit(弓箭手攻擊1, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                    elif 特殊倉鼠.移動次數 % 16 == 2 or 特殊倉鼠.移動次數 % 16 == 3:
                        屏幕.blit(弓箭手攻擊2, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                    elif 特殊倉鼠.移動次數 % 16 == 4 or 特殊倉鼠.移動次數 % 16 == 5:
                        屏幕.blit(弓箭手攻擊3, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                    elif 特殊倉鼠.移動次數 % 16 == 6 or 特殊倉鼠.移動次數 % 16 == 7:
                        屏幕.blit(弓箭手攻擊3, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        屏幕.blit(弓箭手弓箭, (670, 130))
                    elif 特殊倉鼠.移動次數 % 16 == 8 or 特殊倉鼠.移動次數 % 16 == 9:
                        屏幕.blit(弓箭手攻擊3, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        屏幕.blit(弓箭手弓箭, (610, 110))
                    elif 特殊倉鼠.移動次數 % 16 == 10 or 特殊倉鼠.移動次數 % 16 == 11:
                        屏幕.blit(弓箭手攻擊4, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        屏幕.blit(弓箭手弓箭, (550, 90))
                    elif 特殊倉鼠.移動次數 % 16 == 12 or 特殊倉鼠.移動次數 % 16 == 13:
                        屏幕.blit(弓箭手攻擊4, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        屏幕.blit(弓箭手弓箭, (490, 70))
                    elif 特殊倉鼠.移動次數 % 16 == 14 or 特殊倉鼠.移動次數 % 16 == 15:
                        屏幕.blit(弓箭手攻擊4, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        屏幕.blit(弓箭手弓箭, (430, 50))
                        死亡.play(0)
                        倉鼠特殊角色列表.remove(特殊倉鼠)
                        敵人特殊角色列表.remove(鳥)
                        h_arrow = 0
                        h_cupid = 0
                else:
                    if 特殊倉鼠.移動次數 % 4 == 0 or 特殊倉鼠.移動次數 % 4 == 1:
                        屏幕.blit(弓箭手攻擊1, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        for 鳥 in 敵人特殊角色列表:
                            if (鳥.座標.x + 6) == 360:
                                特殊倉鼠.移動次數 = 0
                    elif 特殊倉鼠.移動次數 % 4 == 2 or 特殊倉鼠.移動次數 % 4 == 3:
                        屏幕.blit(弓箭手攻擊2, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        for 鳥 in 敵人特殊角色列表:
                            if (鳥.座標.x + 6) == 360:
                                特殊倉鼠.移動次數 = 0
                特殊倉鼠.移動次數 += 1
       
            elif 特殊倉鼠.類型 == '邱比特':
                目標在範圍內 = False
                for 鳥 in 敵人特殊角色列表:
                    if 鳥.座標.x == 360:
                        目標在範圍內 = True
                        break
               
                if 目標在範圍內:
                    射擊.play(0)
                    if 特殊倉鼠.移動次數 % 16 == 0 or 特殊倉鼠.移動次數 % 16 == 1:
                        屏幕.blit(邱比特攻擊1, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                    elif 特殊倉鼠.移動次數 % 16 == 2 or 特殊倉鼠.移動次數 % 16 == 3:
                        屏幕.blit(邱比特攻擊2, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                    elif 特殊倉鼠.移動次數 % 16 == 4 or 特殊倉鼠.移動次數 % 16 == 5:
                        屏幕.blit(邱比特攻擊3, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                    elif 特殊倉鼠.移動次數 % 16 == 6 or 特殊倉鼠.移動次數 % 16 == 7:
                        屏幕.blit(邱比特攻擊3, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        屏幕.blit(邱比特弓箭, (670, 130))
                    elif 特殊倉鼠.移動次數 % 16 == 8 or 特殊倉鼠.移動次數 % 16 == 9:
                        屏幕.blit(邱比特攻擊3, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        屏幕.blit(邱比特弓箭, (610, 110))
                    elif 特殊倉鼠.移動次數 % 16 == 10 or 特殊倉鼠.移動次數 % 16 == 11:
                        屏幕.blit(邱比特攻擊4, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        屏幕.blit(邱比特弓箭, (550, 90))
                    elif 特殊倉鼠.移動次數 % 16 == 12 or 特殊倉鼠.移動次數 % 16 == 13:
                        屏幕.blit(邱比特攻擊4, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        屏幕.blit(邱比特弓箭, (490, 70))
                    elif 特殊倉鼠.移動次數 % 16 == 14 or 特殊倉鼠.移動次數 % 16 == 15:
                        屏幕.blit(邱比特攻擊4, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        屏幕.blit(邱比特弓箭, (430, 50))
                        倉鼠特殊角色列表.remove(特殊倉鼠)
                        h_arrow = 0
                        h_cupid = 0
                        鳥.魅惑 = True
                       
                else:
                    if 特殊倉鼠.移動次數 % 4 == 0 or 特殊倉鼠.移動次數 % 4 == 1:
                        屏幕.blit(邱比特攻擊1, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        for 鳥 in 敵人特殊角色列表:
                            if (鳥.座標.x + 6) == 360:
                                特殊倉鼠.移動次數 = 0
                    elif 特殊倉鼠.移動次數 % 4 == 2 or 特殊倉鼠.移動次數 % 4 == 3:
                        屏幕.blit(邱比特攻擊2, (特殊倉鼠.座標[0], 特殊倉鼠.座標[1]))
                        for 鳥 in 敵人特殊角色列表:
                            if (鳥.座標.x + 6) == 360:
                                特殊倉鼠.移動次數 = 0
                特殊倉鼠.移動次數 += 1

        更新按鈕()
           
        屏幕.blit(敵方塔文字, (45, 90))
        屏幕.blit(我方塔文字, (722, 90))
        屏幕.blit(錢文字, (750,30))
        屏幕.blit(金幣, (700, 20))
        pygame.display.update()
        pygame.time.Clock().tick(15)
                           
        if 結束 == 1:
            break
        錢文字 = font.render(str(錢) + "/" + "1000", True, "black")
        更新區域 = pygame.Rect(722, 0, 200, 50)
        屏幕.blit(錢文字, (750, 30))
        屏幕.blit(金幣, (700, 20))
   
        pygame.display.update()
        pygame.time.Clock().tick(15)