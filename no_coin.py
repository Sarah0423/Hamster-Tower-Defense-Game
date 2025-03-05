import pygame
import sys
import random
import time
import subprocess

def update_button():
    game_window.blit(pause_button, (10, 10))
    game_window.blit(cupid_button, (650, 400))
    game_window.blit(archer_button, (500, 400))
    game_window.blit(defense_button, (350, 400))
    game_window.blit(coin_button, (200, 400))
    game_window.blit(hamster_button, (50, 400))

start_time = time.time()
current_time = time.time()
last_cat_attack_time = time.time()
last_dog_attack_time = time.time()
last_bird_attack_time = time.time()

hamster_button_down = 0
coin_button_down = 0
defense_button_down = 0
archer_button_down = 0
cupid_button_down = 0

h_arrow = 0
h_cupid = 0

num = 0
my_hp = 10000
enemy_hp = 10000
win = "You Win!!"
defeat = "You Lose..."
end = 0
pause = False

pygame.init()

width = 922
height = 499
game_window = pygame.display.set_mode((width, height))
game_window.fill("white")

BGM=pygame.mixer.Sound("audio/bgm.wav")
BGM.play(-1)
select = pygame.mixer.Sound("audio/choose.mp3")
explosion = pygame.mixer.Sound("audio/explosion.mp3")
tower_attacked = pygame.mixer.Sound("audio/tower_attack.mp3")
hamster_appear = pygame.mixer.Sound("audio/appear.mp3")
hamster_attack = pygame.mixer.Sound("audio/hamster_attack.mp3")
coin_attack = pygame.mixer.Sound("audio/coin_attack.mp3")
defense_attack = pygame.mixer.Sound("audio/defense_attack.mp3")
shoot = pygame.mixer.Sound("audio/shoot.mp3")
cat_appear = pygame.mixer.Sound("audio/cat_appear.mp3")
cat_attack = pygame.mixer.Sound("audio/cat_attack.mp3")
dog_appear = pygame.mixer.Sound("audio/dog_appear.mp3")
dog_attack = pygame.mixer.Sound("audio/dog_attack.mp3")
bird_appear = pygame.mixer.Sound("audio/bird_appear.mp3")
bird_attack = pygame.mixer.Sound("audio/bird_attack.mp3")
dead = pygame.mixer.Sound("audio/dead.mp3")

bg = pygame.image.load("image/背景.jpg")
bg = pygame.transform.scale(bg, (width, height))
pause_button = pygame.image.load("image/pause.png")
start_button = pygame.image.load("image/start.png")
exit_button = pygame.image.load("image/button_exit.png")
enemy_tower = pygame.image.load("image/敵堡.png")
my_tower = pygame.image.load("image/我堡.png")
hamster_button = pygame.image.load("image/button_hamster.png")
coin_button = pygame.image.load("image/button_coin.png")
defense_button = pygame.image.load("image/button_defense.png")
archer_button = pygame.image.load("image/button_archer.png")
cupid_button = pygame.image.load("image/button_cupid.png")

archer_arrow = pygame.image.load("image/archer_arrow.png")
cupid_arrow = pygame.image.load("image/cupid_arrow.png")


hamster_walk1 = pygame.image.load("image/normal_walk1.png")
hamster_walk2 = pygame.image.load("image/normal_walk2.png")
hamster_walk3 = pygame.image.load("image/normal_walk3.png")
hamster_walk4 = pygame.image.load("image/normal_walk4.png")
coin_walk1 = pygame.image.load("image/coin_walk1.png")
coin_walk2 = pygame.image.load("image/coin_walk2.png")
coin_walk3 = pygame.image.load("image/coin_walk3.png")
coin_walk4 = pygame.image.load("image/coin_walk4.png")
defense_walk1 = pygame.image.load("image/defense_walk1.png")
defense_walk2 = pygame.image.load("image/defense_walk2.png")
defense_walk3 = pygame.image.load("image/defense_walk3.png")
defense_walk4 = pygame.image.load("image/defense_walk4.png")
cat_walk1 = pygame.image.load("image/cat_walk1.png")
cat_walk2 = pygame.image.load("image/cat_walk2.png")
cat_walk3 = pygame.image.load("image/cat_walk3.png")
cat_walk4 = pygame.image.load("image/cat_walk2.png")
dog_walk1 = pygame.image.load("image/dog_walk1.png")
dog_walk2 = pygame.image.load("image/dog_walk2.png")
dog_walk3 = pygame.image.load("image/dog_walk3.png")
dog_walk4 = pygame.image.load("image/dog_walk2.png")
bird_walk1 = pygame.image.load("image/bird_walk1.png")
bird_walk2 = pygame.image.load("image/bird_walk2.png")
bird_loved1 = pygame.image.load("image/bbb.png")
bird_loved2 = pygame.image.load("image/bird_love2.png")
archer = pygame.image.load("image/archer.png")
cupid = pygame.image.load("image/cupid.png")

hamster_attack1 = pygame.image.load("image/normal_attack1.png")
hamster_attack2 = pygame.image.load("image/normal_attack2.png")
hamster_attack3 = pygame.image.load("image/normal_attack3.png")
coin_attack1 = pygame.image.load("image/coin_attack1.png")
coin_attack2 = pygame.image.load("image/coin_attack2.png")
coin_attack3 = pygame.image.load("image/coin_attack3.png")
defense_attack1 = pygame.image.load("image/defense_attack1.png")
defense_attack2 = pygame.image.load("image/defense_attack2.png")
defense_attack3 = pygame.image.load("image/defense_attack3.png")
cat_attack1 = pygame.image.load("image/cat_attack1.png")
cat_attack2 = pygame.image.load("image/cat_attack2.png")
dog_attack1 = pygame.image.load("image/dog_attack1.png")
dog_attack2 = pygame.image.load("image/dog_attack2.png")
archer_attack1 = pygame.image.load("image/archer_attack1.png")
archer_attack2 = pygame.image.load("image/archer_attack2.png")
archer_attack3 = pygame.image.load("image/archer_attack3.png")
archer_attack4 = pygame.image.load("image/archer_attack4.png")
cupid_attack1 = pygame.image.load("image/cupid_attack1.png")
cupid_attack2 = pygame.image.load("image/cupid_attack2.png")
cupid_attack3 = pygame.image.load("image/cupid_attack3.png")
cupid_attack4 = pygame.image.load("image/cupid_attack4.png")

enemy_tower = pygame.transform.scale(enemy_tower, (180, 320))
my_tower = pygame.transform.scale(my_tower, (180, 320))

pause_button = pygame.transform.scale(pause_button, (50, 50))
start_button = pygame.transform.scale(start_button, (150, 150))
exit_button = pygame.transform.scale(exit_button, (150, 60))
hamster_button = pygame.transform.scale(hamster_button, (100, 80))
coin_button = pygame.transform.scale(coin_button, (100, 80))
defense_button = pygame.transform.scale(defense_button, (100, 80))
archer_button = pygame.transform.scale(archer_button, (100, 80))
cupid_button = pygame.transform.scale(cupid_button, (100, 80))
archer_arrow = pygame.transform.scale(archer_arrow, (150, 150))
cupid_arrow = pygame.transform.scale(cupid_arrow, (150, 150))

hamster_walk1 = pygame.transform.scale(hamster_walk1, (150, 150))
hamster_walk2 = pygame.transform.scale(hamster_walk2, (150, 150))
hamster_walk3 = pygame.transform.scale(hamster_walk3, (150, 150))
hamster_walk4 = pygame.transform.scale(hamster_walk4, (150, 150))

coin_walk1 = pygame.transform.scale(coin_walk1, (150, 150))
coin_walk2 = pygame.transform.scale(coin_walk2, (150, 150))
coin_walk3 = pygame.transform.scale(coin_walk3, (150, 150))
coin_walk4 = pygame.transform.scale(coin_walk4, (150, 150))

defense_walk1 = pygame.transform.scale(defense_walk1, (150, 150))
defense_walk2 = pygame.transform.scale(defense_walk2, (150, 150))
defense_walk3 = pygame.transform.scale(defense_walk3, (150, 150))
defense_walk4 = pygame.transform.scale(defense_walk4, (150, 150))

cat_walk1 = pygame.transform.scale(cat_walk1, (150, 150))
cat_walk2 = pygame.transform.scale(cat_walk2, (150, 150))
cat_walk3 = pygame.transform.scale(cat_walk3, (150, 150))
cat_walk4 = pygame.transform.scale(cat_walk4, (150, 150))

dog_walk1 = pygame.transform.scale(dog_walk1, (150, 150))
dog_walk2 = pygame.transform.scale(dog_walk2, (150, 150))
dog_walk3 = pygame.transform.scale(dog_walk3, (150, 150))
dog_walk4 = pygame.transform.scale(dog_walk4, (150, 150))

bird_walk1 = pygame.transform.scale(bird_walk1, (150, 150))
bird_walk2 = pygame.transform.scale(bird_walk2, (150, 150))

bird_loved1 = pygame.transform.scale(bird_loved1, (150, 150))
bird_loved2 = pygame.transform.scale(bird_loved2, (150, 150))

archer = pygame.transform.scale(archer, (150, 150))
cupid = pygame.transform.scale(cupid, (150, 150))


hamster_attack1 = pygame.transform.scale(hamster_attack1, (150, 150))
hamster_attack2 = pygame.transform.scale(hamster_attack2, (150, 150))
hamster_attack3 = pygame.transform.scale(hamster_attack3, (150, 150))

coin_attack1 = pygame.transform.scale(coin_attack1, (150, 150))
coin_attack2 = pygame.transform.scale(coin_attack2, (150, 150))
coin_attack3 = pygame.transform.scale(coin_attack3, (150, 150))

defense_attack1 = pygame.transform.scale(defense_attack1, (150, 150))
defense_attack2 = pygame.transform.scale(defense_attack2, (150, 150))
defense_attack3 = pygame.transform.scale(defense_attack3, (150, 150))

cat_attack1 = pygame.transform.scale(cat_attack1, (150, 150))
cat_attack2 = pygame.transform.scale(cat_attack2, (150, 150))

dog_attack1 = pygame.transform.scale(dog_attack1, (150, 150))
dog_attack2 = pygame.transform.scale(dog_attack2, (150, 150))


archer_attack1 = pygame.transform.scale(archer_attack1, (150, 150))
archer_attack2 = pygame.transform.scale(archer_attack2, (150, 150))
archer_attack3 = pygame.transform.scale(archer_attack3, (150, 150))
archer_attack4 = pygame.transform.scale(archer_attack4, (150, 150))
cupid_attack1 = pygame.transform.scale(cupid_attack1, (150, 150))
cupid_attack2 = pygame.transform.scale(cupid_attack2, (150, 150))
cupid_attack3 = pygame.transform.scale(cupid_attack3, (150, 150))
cupid_attack4 = pygame.transform.scale(cupid_attack4, (150, 150))

hamster_walk_list = [hamster_walk1, hamster_walk2, hamster_walk3, hamster_walk4]
coin_walk_list = [coin_walk1, coin_walk2, coin_walk3, coin_walk4]
defense_walk_list = [defense_walk1, defense_walk2, defense_walk3, defense_walk4]
cat_walk_list = [cat_walk1, cat_walk2, cat_walk3, cat_walk4]
dog_walk_list = [dog_walk1, dog_walk2, dog_walk3, dog_walk4]
bird_walk_list = [bird_walk1, bird_walk2]
archer_walk_list = [archer_attack1, archer_attack2]
cupid_walk_list = [cupid_attack1, cupid_attack2]

font = pygame.font.Font("k12x8.ttf", 20)
font_15 = pygame.font.Font("k12x8.ttf", 15)
enemy_word = font.render(str(enemy_hp) + "/" + "10000", True, "black")
my_word = font.render(str(my_hp) + "/" + "10000", True, "black")

enemy_list = []
hamster_list = []
enemy_sp_list = []
hamster_sp_list = []

class character:
    def __init__(self, typ, pla, hp, power, move):
        self.typ = typ
        self.pla = pygame.Rect(pla[0], pla[1], pla[2], pla[3])
        self.hp = hp
        self.power = power
        self.move = move
        self.far = None

class bird_character:
    def __init__(self, pla, hp, move):
        self.pla = pygame.Rect(pla[0], pla[1], pla[2], pla[3])
        self.hp = hp
        self.move = move
        self.charm = False
        self.stop_time = None

class hamster_character:
    def __init__(self, typ, pla, hp, move):
        self.typ = typ
        self.pla = pygame.Rect(pla[0], pla[1], pla[2], pla[3])
        self.hp = hp
        self.move = move
       
       
def generate_hamster():
    hamster_list.append(character('hamster', (722, 280, 0, 0), 1000, 3, 0))
def generate_coin():
    hamster_list.append(character('coin', (722, 280, 0, 0), 500, 1, 0))
def generate_defense():
    hamster_list.append(character('defense', (722, 280, 0, 0), 1500, 2, 0))
def generate_cat():
    enemy_list.append(character('cat', (180, 280, 0, 0), 500, 3, 0))
def generate_dog():
    enemy_list.append(character('dog', (180, 280, 0, 0), 1000, 5, 0))
def generate_bird():
    enemy_sp_list.append(bird_character((0, 10, 0, 0), 200, 0))
def generate_archer():
    global h_arrow
    h_arrow = 1
    hamster_sp_list.append(hamster_character('archer', (730, 150, 0, 0), 200, 0))
def generate_cupid():
    global h_cupid
    h_cupid = 1
    hamster_sp_list.append(hamster_character('cupid', (730, 150, 0, 0), 200, 0))


def hamster_act():
    global enemy_word, enemy_hp, end, h1, h2
    for hamster in hamster_list:
        if hamster.hp > 0:
            target = 150 if hamster.far is None else hamster.far
            if hamster.pla.x > target:
                hamster.pla.x -= 6
            elif hamster.pla.x >= target:
                hamster.far = None
            for enemy in enemy_list:
                if abs(hamster.pla.x - enemy.pla.x) <= 60:
                    hamster.far = hamster.pla.x
                    h1 = hamster.far - 30
                    h2 = hamster.far
                    hamster_attack(hamster, enemy)
            if hamster.pla.x <= 150:
                hamster.far = hamster.pla.x
                h1 = 150
                h2 = 180
                attack_x = random.randint(h1, h2)
                hamster.pla.x = attack_x
                tower_attacked.play(0)
                enemy_hp -= hamster.power
                hamster.far = hamster.pla.x
                enemy_word = font.render(str(enemy_hp) + "/" + "10000", True, "black")
                if enemy_hp <= 0:
                    enemy_hp = 0
                    end()
                    end = 1
               

def enemy_act():
    global my_word, my_hp, end, x1, x2
    for enemy in enemy_list:
        if enemy.hp > 0:
            target = 722 if enemy.far is None else enemy.far
            if enemy.pla.x < target:
                enemy.pla.x += 6
            elif enemy.pla.x <= target:
                enemy.far = None
            for hamster in hamster_list:
                if abs(enemy.pla.x - hamster.pla.x) <= 60:
                    enemy.far = enemy.pla.x
                    x1 = enemy.far - 30
                    x2 = enemy.far
                    hamster_attack(enemy, hamster)
            if enemy.pla.x >= 722:
                enemy.far = enemy.pla.x
                x1 = 632
                x2 = 662
                attack_x = random.randint(x1, x2)
                enemy.pla.x = attack_x
                tower_attacked.play(0)
                my_hp -= enemy.power
                my_word = font.render(str(my_hp) + "/" + "10000", True, "black")
                if my_hp <= 0:
                    my_hp = 0
                    end()
                    end = 1

def bird_act():
    global h_arrow, h_cupid
    target = 360

    for bird in enemy_sp_list:
        if bird.hp > 0:
            if bird.pla.x < target:
                bird.pla.x += 6
                bird.stop_time = None
            elif bird.pla.x == target and bird.stop_time is None:
                    bird.stop_time = time.time()
            elif bird.pla.x == target and time.time() - bird.stop_time >= 5:
                if bird.charm is False:
                    bird_attack.play(0)
                    hamster_list.clear()
                    hamster_sp_list.clear()
                    enemy_list.clear()
                    h_arrow = 0
                    h_cupid = 0
                    bird.pla.x += 6
                else:
                    bird.pla.x += 6
            elif bird.pla.x > target and bird.pla.x <= width:
                bird.pla.x += 6
               
def update_game():
    hamster_act()
    enemy_act
    bird_act()

def hamster_attack(attacker, attacked):
    if attacker.typ == 'hamster':
        hamster_attack.play(0)
    elif attacker.typ == 'coin':
        coin_attack.play(0)
    elif attacker.typ == 'defense':
        defense_attack.play(0)
    elif attacker.typ == 'dog':
        dog_attack.play(0)
    elif attacker.typ == 'cat':
        cat_attack.play(0)
    attacked.hp -= attacker.power
    if attacked.hp <= 0:
        if attacked in enemy_list:
            dead.play(0)
            enemy_list.remove(attacked)
        else:
            dead.play(0)
            hamster_list.remove(attacked)
        attacker.far = None

def end():
    explosion.play(0)
    global num, enemy_hp, my_hp
    if enemy_hp == 0:
        for num in range(12):
            num = num + 1
            explode_area = [
                (170, 250, 180, 280),
                (250, 330, 180, 280),
                (330, 410, 180, 280),
                (410, 490, 180, 280),
                (490, 570, 180, 280)
            ]

            explode_hamster_x = random.randint(explode_area[0][0], explode_area[0][1])
            explode_hamster_y = random.randint(explode_area[0][2], explode_area[0][3])
            explode_coin_x = random.randint(explode_area[1][0], explode_area[1][1])
            explode_coin_y = random.randint(explode_area[1][2], explode_area[1][3])
            explode_defense_x = random.randint(explode_area[2][0], explode_area[2][1])
            explode_defense_y = random.randint(explode_area[2][2], explode_area[2][3])
            explode_archer_x = random.randint(explode_area[3][0], explode_area[3][1])
            explode_archer_y = random.randint(explode_area[3][2], explode_area[3][3])
            explode_cupid_x = random.randint(explode_area[4][0], explode_area[4][1])
            explode_cupid_y = random.randint(explode_area[4][2], explode_area[4][3])

            game_window.blit(bg, (0, 0))
            game_window.blit(enemy_tower, (40, 100))  
            game_window.blit(my_tower, (722, 100))
            game_window.blit(hamster_walk_list[num % 4], (explode_hamster_x, explode_hamster_y))
            game_window.blit(coin_walk_list[num % 4], (explode_coin_x, explode_coin_y))
            game_window.blit(defense_walk_list[num % 4], (explode_defense_x, explode_defense_y))
            game_window.blit(archer_walk_list[num % 2], (explode_archer_x, explode_archer_y))
            game_window.blit(cupid_walk_list[num % 2], (explode_cupid_x, explode_cupid_y))
            game_window.blit(enemy_word, (45, 90))
            game_window.blit(my_word, (722, 90))
            game_window.blit(font.render(win, True, "yellow"), (381, 250))
       
            pygame.display.update()
            pygame.time.Clock().tick(5)      
        time.sleep(1)
        
    if my_hp == 0:
        for num in range(26):
            num = num + 1
            explode_area = [
                (250, 330, 180, 280),
                (330, 410, 100, 200),
                (410, 490, 180, 280),
            ]

            explode_cat_x = random.randint(explode_area[0][0], explode_area[0][1])
            explode_cat_y = random.randint(explode_area[0][2], explode_area[0][3])
            explode_bird_x = random.randint(explode_area[1][0], explode_area[1][1])
            explode_bird_y = random.randint(explode_area[1][2], explode_area[1][3])
            explode_dog_x = random.randint(explode_area[2][0], explode_area[2][1])
            explode_dog_y = random.randint(explode_area[2][2], explode_area[2][3])

            game_window.blit(bg, (0, 0))
            game_window.blit(enemy_tower, (40, 100))  
            game_window.blit(my_tower, (722, 100))
            game_window.blit(cat_walk_list[num % 4], (explode_cat_x, explode_cat_y))
            game_window.blit(bird_walk_list[num % 2], (explode_bird_x, explode_bird_y))
            game_window.blit(dog_walk_list[num % 4], (explode_dog_x, explode_dog_y))
            game_window.blit(enemy_word, (45, 90))
            game_window.blit(my_word, (722, 90))
            game_window.blit(font.render(defeat, True, "black"), (381, 250))
       
            pygame.display.update()
            pygame.time.Clock().tick(5)      
        time.sleep(1)
   
    while True:
        pygame.display.update()
        game_window.blit(bg, (0, 0))
        game_window.blit(enemy_tower, (40, 100))
        game_window.blit(my_tower, (722, 100))
            
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.quit()
        subprocess.run(["python", "hamster.py"])
        sys.exit()

while True:
    if current_time - start_time >= 0.5:
        update_game()
        start_time = current_time

    pause_button_message = game_window.blit(pause_button, (10, 10))
    exit_button_message = game_window.blit(exit_button, (770, 400))
    hamster_button_message = game_window.blit(hamster_button, (50, 400))
    coin_button_message = game_window.blit(coin_button, (200, 400))
    defense_button_message = game_window.blit(defense_button, (350, 400))
    archer_button_message = game_window.blit(archer_button, (500, 400))
    cupid_button_message = game_window.blit(cupid_button, (650, 400))
   

    while True:
        current_time = time.time()
        update_game()
        if current_time - last_cat_attack_time >= 10:
            cat_appear.play(0)
            generate_cat()
            last_cat_attack_time = current_time

        if current_time - last_dog_attack_time >= 20:
            dog_appear.play(0)
            generate_dog()
            last_dog_attack_time = current_time

        if current_time - last_bird_attack_time >= 30:
            bird_appear.play(0)
            generate_bird()
            last_bird_attack_time = current_time
           
        update_game()
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
       
        mouse_click = pygame.mouse.get_pressed()
        (mx, my) = pygame.mouse.get_pos()

        if pause:
            start_button_message = game_window.blit(start_button, (386, 174.5))
            exit_button_message = game_window.blit(exit_button, (770, 400))
            game_window.blit(font.render("EXIT", True, "white"), (820, 422))
            pygame.display.update()
        
            while pause:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (mx, my) = pygame.mouse.get_pos()
                        if exit_button_message.collidepoint((mx, my)):
                            select.play(0)
                            pygame.time.delay(300)
                            pygame.quit()
                            subprocess.run(["python", "hamster.py"])
                            sys.exit()
                        if start_button_message.collidepoint((mx, my)):
                            select.play(0)
                            pause = False
        if mouse_click[0] and pause_button_message.collidepoint((mx, my)):
            select.play(0)
            pause = True

        if mouse_click[0] and hamster_button_message.collidepoint((mx, my)) and hamster_button_down == 0:
            hamster_appear.play(0)
            generate_hamster()
            hamster_button_down = 1
        elif mouse_click[0] and coin_button_message.collidepoint((mx, my)) and coin_button_down == 0:
            hamster_appear.play(0)
            generate_coin()
            coin_button_down = 1
        elif mouse_click[0] and defense_button_message.collidepoint((mx, my)) and defense_button_down == 0:
            hamster_appear.play(0)
            generate_defense()
            defense_button_down = 1
        elif mouse_click[0] and archer_button_message.collidepoint((mx, my)) and archer_button_down == 0 and h_arrow == 0 and h_cupid == 0:
            hamster_appear.play(0)
            generate_archer()
            archer_button_down = 1
        elif mouse_click[0] and cupid_button_message.collidepoint((mx, my)) and cupid_button_down == 0 and h_arrow == 0 and h_cupid == 0:
            hamster_appear.play(0)
            generate_cupid()
            cupid_button_down = 1
        else:
            hamster_button_down = 0
            coin_button_down = 0
            defense_button_down = 0
            archer_button_down = 0
            cupid_button_down = 0

        game_window.blit(bg, (0, 0))
        game_window.blit(enemy_tower, (40, 100))
        game_window.blit(my_tower, (722, 100))

        for hamster in hamster_list:
            if hamster.pla.x >= 150:
                if hamster.typ == 'hamster':
                    if hamster.far == None:
                        if hamster.move % 8 == 0 or hamster.move % 8 == 1:
                            game_window.blit(hamster_walk1, (hamster.pla[0], hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 8 == 2 or hamster.move % 8 == 3:
                            game_window.blit(hamster_walk2, (hamster.pla[0], hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 8 == 4 or hamster.move % 8 == 5:
                            game_window.blit(hamster_walk3, (hamster.pla[0], hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 8 == 6 or hamster.move % 8 == 7:
                            game_window.blit(hamster_walk4, (hamster.pla[0], hamster.pla[1]))
                            hamster.move += 1
                    else:
                        if hamster.move % 3 == 0:
                            game_window.blit(hamster_attack1, (random.randint(h1, h2), hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 3 == 1:
                            game_window.blit(hamster_attack2, (random.randint(h1, h2), hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 3 == 2:
                            game_window.blit(hamster_attack3, (random.randint(h1, h2), hamster.pla[1]))
                            hamster.move += 1
                elif hamster.typ == 'coin':
                    if hamster.far == None:
                        if hamster.move % 8 == 0 or hamster.move % 8 == 1:
                            game_window.blit(coin_walk1, (hamster.pla[0], hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 8 == 2 or hamster.move % 8 == 3:
                            game_window.blit(coin_walk2, (hamster.pla[0], hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 8 == 4 or hamster.move % 8 == 5:
                            game_window.blit(coin_walk3, (hamster.pla[0], hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 8 == 6 or hamster.move % 8 == 7:
                            game_window.blit(coin_walk4, (hamster.pla[0], hamster.pla[1]))
                            hamster.move += 1
                    else:
                        if hamster.move % 3 == 0:
                            game_window.blit(coin_attack1, (random.randint(h1, h2), hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 3 == 1:
                            game_window.blit(coin_attack2, (random.randint(h1, h2), hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 3 == 2:
                            game_window.blit(coin_attack3, (random.randint(h1, h2), hamster.pla[1]))
                            hamster.move += 1
                elif hamster.typ == 'defense':
                    if hamster.far == None:
                        if hamster.move % 8 == 0 or hamster.move % 8 == 1:
                            game_window.blit(defense_walk1, (hamster.pla[0], hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 8 == 2 or hamster.move % 8 == 3:
                            game_window.blit(defense_walk2, (hamster.pla[0], hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 8 == 4 or hamster.move % 8 == 5:
                            game_window.blit(defense_walk3, (hamster.pla[0], hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 8 == 6 or hamster.move % 8 == 7:
                            game_window.blit(defense_walk4, (hamster.pla[0], hamster.pla[1]))
                            hamster.move += 1
                    else:
                        if hamster.move % 3 == 0:
                            game_window.blit(defense_attack1, (random.randint(h1, h2), hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 3 == 1:
                            game_window.blit(defense_attack2, (random.randint(h1, h2), hamster.pla[1]))
                            hamster.move += 1
                        elif hamster.move % 3 == 2:
                            game_window.blit(defense_attack3, (random.randint(h1, h2), hamster.pla[1]))
                            hamster.move += 1

        for enemy in enemy_list:
            if enemy.pla.x <= 722:
                if enemy.typ == 'cat':
                    if enemy.far == None:
                        if enemy.move % 8 == 0 or enemy.move % 8 == 1:
                            game_window.blit(cat_walk1, (enemy.pla[0], enemy.pla[1]))
                            enemy.move += 1
                        elif enemy.move % 8 == 2 or enemy.move % 8 == 3:
                            game_window.blit(cat_walk2, (enemy.pla[0], enemy.pla[1]))
                            enemy.move += 1
                        elif enemy.move % 8 == 4 or enemy.move % 8 == 5:
                            game_window.blit(cat_walk3, (enemy.pla[0], enemy.pla[1]))
                            enemy.move += 1
                        elif enemy.move % 8 == 6 or enemy.move % 8 == 7:
                            game_window.blit(cat_walk4, (enemy.pla[0], enemy.pla[1]))
                            enemy.move += 1
                    else:
                        if enemy.move % 2 == 0:
                            game_window.blit(cat_attack1, (random.randint(x1, x2), enemy.pla[1]))
                            enemy.move += 1
                        elif enemy.move % 2 == 1:
                            game_window.blit(cat_attack2, (random.randint(x1, x2), enemy.pla[1]))
                            enemy.move += 1
                       
                elif enemy.typ == 'dog':
                    if enemy.far == None:
                        if enemy.move % 8 == 0 or enemy.move % 8 == 1:
                            game_window.blit(dog_walk1, (enemy.pla[0], enemy.pla[1]))
                            enemy.move += 1
                        elif enemy.move % 8 == 2 or enemy.move % 8 == 3:
                            game_window.blit(dog_walk2, (enemy.pla[0], enemy.pla[1]))
                            enemy.move += 1
                        elif enemy.move % 8 == 4 or enemy.move % 8 == 5:
                            game_window.blit(dog_walk3, (enemy.pla[0], enemy.pla[1]))
                            enemy.move += 1
                        elif enemy.move % 8 == 6 or enemy.move % 8 == 7:
                            game_window.blit(dog_walk4, (enemy.pla[0], enemy.pla[1]))
                            enemy.move += 1
                    else:
                        if enemy.move % 2 == 0:
                            game_window.blit(dog_attack1, (random.randint(x1, x2), enemy.pla[1]))
                            enemy.move += 1
                        elif enemy.move % 2 == 1:
                            game_window.blit(dog_attack2, (random.randint(x1, x2), enemy.pla[1]))
                            enemy.move += 1

        for bird in enemy_sp_list:
            if bird.charm == False:
                if bird.pla.x <= 922:
                    if bird.move % 4 == 0 or bird.move % 4 == 1:
                        game_window.blit(bird_walk1, (bird.pla[0], bird.pla[1]))
                        bird.move += 1
                    else:
                        game_window.blit(bird_walk2, (bird.pla[0], bird.pla[1]))
                        bird.move += 1
            else:
                if bird.pla.x == 360:
                    if bird.move % 5 <= 1:
                        game_window.blit(bird_loved2, (bird.pla[0], bird.pla[1]))
                        bird.move += 1
                    elif bird.move % 5 <= 3:
                        game_window.blit(bird_loved1, (bird.pla[0], bird.pla[1]))
                        bird.move += 1
                    else:
                        game_window.blit(bird_loved2, (bird.pla[0], bird.pla[1]))
                        enemy_list.clear()
                        bird.move = 0
                        bird.pla.x += 6
                else:
                    if bird.move % 4 == 0 or bird.move % 4 == 1:
                        game_window.blit(bird_loved1, (bird.pla[0], bird.pla[1]))
                        bird.move += 1
                    else:
                        game_window.blit(bird_loved2, (bird.pla[0], bird.pla[1]))
                        bird.move += 1
                    if (bird.pla.x + 6) == 360:
                        bird.move = 0
                   
        for sp_hamster in hamster_sp_list:
            if sp_hamster.typ == 'archer':
                in_range = False
                for bird in enemy_sp_list:
                    if bird.pla.x == 360:
                        in_range = True
                        break
               
                if in_range:
                    shoot.play(0)
                    if sp_hamster.move % 16 == 0 or sp_hamster.move % 16 == 1:
                        game_window.blit(archer_attack1, (sp_hamster.pla[0], sp_hamster.pla[1]))
                    elif sp_hamster.move % 16 == 2 or sp_hamster.move % 16 == 3:
                        game_window.blit(archer_attack2, (sp_hamster.pla[0], sp_hamster.pla[1]))
                    elif sp_hamster.move % 16 == 4 or sp_hamster.move % 16 == 5:
                        game_window.blit(archer_attack3, (sp_hamster.pla[0], sp_hamster.pla[1]))
                    elif sp_hamster.move % 16 == 6 or sp_hamster.move % 16 == 7:
                        game_window.blit(archer_attack3, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        game_window.blit(archer_arrow, (670, 130))
                    elif sp_hamster.move % 16 == 8 or sp_hamster.move % 16 == 9:
                        game_window.blit(archer_attack3, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        game_window.blit(archer_arrow, (610, 110))
                    elif sp_hamster.move % 16 == 10 or sp_hamster.move % 16 == 11:
                        game_window.blit(archer_attack4, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        game_window.blit(archer_arrow, (550, 90))
                    elif sp_hamster.move % 16 == 12 or sp_hamster.move % 16 == 13:
                        game_window.blit(archer_attack4, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        game_window.blit(archer_arrow, (490, 70))
                    elif sp_hamster.move % 16 == 14 or sp_hamster.move % 16 == 15:
                        game_window.blit(archer_attack4, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        game_window.blit(archer_arrow, (430, 50))
                        dead.play(0)
                        hamster_sp_list.remove(sp_hamster)
                        enemy_sp_list.remove(bird)
                        h_arrow = 0
                        h_cupid = 0
                else:
                    if sp_hamster.move % 4 == 0 or sp_hamster.move % 4 == 1:
                        game_window.blit(archer_attack1, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        for bird in enemy_sp_list:
                            if (bird.pla.x + 6) == 360:
                                sp_hamster.move = 0
                    elif sp_hamster.move % 4 == 2 or sp_hamster.move % 4 == 3:
                        game_window.blit(archer_attack2, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        for bird in enemy_sp_list:
                            if (bird.pla.x + 6) == 360:
                                sp_hamster.move = 0
                sp_hamster.move += 1
       
            elif sp_hamster.typ == 'cupid':
                in_range = False
                for bird in enemy_sp_list:
                    if bird.pla.x == 360:
                        in_range = True
                        break
               
                if in_range:
                    shoot.play(0)
                    if sp_hamster.move % 16 == 0 or sp_hamster.move % 16 == 1:
                        game_window.blit(cupid_attack1, (sp_hamster.pla[0], sp_hamster.pla[1]))
                    elif sp_hamster.move % 16 == 2 or sp_hamster.move % 16 == 3:
                        game_window.blit(cupid_attack2, (sp_hamster.pla[0], sp_hamster.pla[1]))
                    elif sp_hamster.move % 16 == 4 or sp_hamster.move % 16 == 5:
                        game_window.blit(cupid_attack3, (sp_hamster.pla[0], sp_hamster.pla[1]))
                    elif sp_hamster.move % 16 == 6 or sp_hamster.move % 16 == 7:
                        game_window.blit(cupid_attack3, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        game_window.blit(cupid_arrow, (670, 130))
                    elif sp_hamster.move % 16 == 8 or sp_hamster.move % 16 == 9:
                        game_window.blit(cupid_attack3, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        game_window.blit(cupid_arrow, (610, 110))
                    elif sp_hamster.move % 16 == 10 or sp_hamster.move % 16 == 11:
                        game_window.blit(cupid_attack4, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        game_window.blit(cupid_arrow, (550, 90))
                    elif sp_hamster.move % 16 == 12 or sp_hamster.move % 16 == 13:
                        game_window.blit(cupid_attack4, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        game_window.blit(cupid_arrow, (490, 70))
                    elif sp_hamster.move % 16 == 14 or sp_hamster.move % 16 == 15:
                        game_window.blit(cupid_attack4, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        game_window.blit(cupid_arrow, (430, 50))
                        hamster_sp_list.remove(sp_hamster)
                        h_arrow = 0
                        h_cupid = 0
                        bird.charm = True
                       
                else:
                    if sp_hamster.move % 4 == 0 or sp_hamster.move % 4 == 1:
                        game_window.blit(cupid_attack1, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        for bird in enemy_sp_list:
                            if (bird.pla.x + 6) == 360:
                                sp_hamster.move = 0
                    elif sp_hamster.move % 4 == 2 or sp_hamster.move % 4 == 3:
                        game_window.blit(cupid_attack2, (sp_hamster.pla[0], sp_hamster.pla[1]))
                        for bird in enemy_sp_list:
                            if (bird.pla.x + 6) == 360:
                                sp_hamster.move = 0
                sp_hamster.move += 1

        update_button()
           
        game_window.blit(enemy_word, (45, 90))
        game_window.blit(my_word, (722, 90))
        pygame.display.update()
        pygame.time.Clock().tick(15)
                           
        if end == 1:
            break

        pygame.display.update()
        pygame.time.Clock().tick(15)