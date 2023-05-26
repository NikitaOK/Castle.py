from pygame import *
from time import sleep
from random import *
#класс-родитель для других спрайтов
mixer.init()
class GameSprite(sprite.Sprite):
 # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
     # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
     # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
 
     # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def collidepoint(self,player_x,player_y):
        return self.rect.collidepoint(player_x,player_y)
 # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
 #метод, в котором реализовано управление спрайтом по кнопкам стрелочкам клавиатуры
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed,health, armor, power):
     # Вызываем конструктор класса (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)
 
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
        self.health = health
        self.armor = armor
        self.power = power
    #движение
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 450:
            self.rect.y -= self.y_speed
        if keys[K_d] and self.rect.x < win_width - 90:
            self.rect.x += self.x_speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.x_speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.y_speed
    def enemy_update(self,enemy):
        self.rect.y = enemy.rect.y
    #методы боя
    def strike(self, enemy):#метод удара
        enemy.health -= self.power
    #передввижение фаер бола
    def update_firebol(self,enemy):
        self.rect.x += 3
        self.rect.y = enemy.rect.y - 160


#цвета
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BlUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255) 
#Создаем окошко
win_width = 1370
win_height = 700
display.set_caption("The Castle")
window = display.set_mode((win_width, win_height))
back = (119, 210, 223)#задаем цвет согласно цветовой схеме RGB
clock = time.Clock()
#главные окна
win_main = GameSprite('main.png',0,0,1370,700)#main
win_spravka = GameSprite('spravka.png',150,150,1000,500)#справка 1
win_spravka2 = GameSprite('spravka2.png',150,150,1000,500)#справка 2
win_spravka3 = GameSprite('spravka3.png',150,150,1000,500)#справка 3
win_info_hero = GameSprite('infoh.png',150,150,1000,500)#информация огерое(окно)
main_boi = GameSprite('vraginfo.png',0,0,1370,700)#меню перед боем
win_magaz= GameSprite('magaz1.png',0,0,1370,700)#магазин
win_spravka_kod = GameSprite('spravka_kod.png',0,0,1370,700)#справка про коды

theend = GameSprite('theend.png',0,0,1370,700)#концовка
theend2 = GameSprite('theend2.png',0,0,1370,700)
vibor =  GameSprite('vibor.png',0,0,1370,700)
vibor1 =  GameSprite('vibor.png',200,40,400,600)
vibor2 =  GameSprite('vibor.png',740,40,400,600)
#вспомогательные значки
#универсальная иконка для закрытия окон
krest = GameSprite('krest.png',1050,150,100,100)
krest_kod = GameSprite('krest.png',1270,0,100,100)#для spravka_kod
#main иконки
icon_boi = GameSprite('png1.png',0,100,100,100)
icon2_info_hero = GameSprite('png2.png',0,230,100,100)
icon3_magaz = GameSprite('png3.png',0,390,100,100)
#иконка кодов
codes = GameSprite('kod_image.png',0,550,100,100)
#иконки для выбора боя
skeleton_icon_vspom = GameSprite('vrag2.png',200,220,250,250)
voin_icon_vspom = GameSprite('vrag2.png',550,230,250,250)
mag_icon_vspom = GameSprite('vrag3mag.png',880,230,220,225)
vuixod_iz_boi = GameSprite('krest.png',900,0,60,80)
#иконки магазина
stil1 = GameSprite('vrag2.png',200,220,250,250)
stil2 = GameSprite('vrag2.png',550,230,250,250)
stil3 = GameSprite('vrag3mag.png',880,230,220,225)
#арена для боя и перед заставка боем
arena_boi = GameSprite('arena.png',0,0,1370,700)
#создание экрана победы и поражеия
victory = GameSprite('WIN.png',0,0,1370,700)
loose = GameSprite('loose.png',0,0,1370,700)
#игровая валюта и прочее
level = 0
money = 0
stil = 'Нет'
opit = 0
name = 'Белл:'

#переменная цикла
run = True
#main
main = True
#задание параметров боя
boi = False
boi_in = False
boi_skelet = False
boi_mag = False
Boi_voin = False
#магазин
magaz = False
#музыка
song_end = True
#выбор сложности
vibor_vspom = True
vibor_vspom_1 = False
vibor_vspom_2 = False
#иформация героя
info_hero = False
#обучающие справки
spravka2 = True
spravka= False
spravka3 = False
spravka_kod = True
z = 0 #счётчмк справок
b = 0 #счётчик окна перед боем
m = 0 #счётчик справки в магазине
a = 0 #счётчик стиля сэмпо
b = 0#счётчик стиля синоби
c = 0#счётчик стиля муссин
codess = False#ввод кода в консоль
health_chet = 0#счётчик восстановления жизни после боя
#имя героя
font.init()
font = font.SysFont('Arial', 30)
win_name = font.render(name,True,DARK_BLUE)
spawn1 = 0#переменнаыя для остоновки создания врагов и героя
#победа или поражение
hero_win = False
win_vrag = False
#интерфейсв бою
health_win_vrag = GameSprite('hp.png',0,100,100,50)
health_win_hero = GameSprite('hp.png',1270,100,100,50)
armor_win_vrag = GameSprite('armor.png',0,150,100,50)
armor_win_hero = GameSprite('armor.png',1270,150,100,50)



#МУЗЫКА В БОЮ
music_boi2 = mixer.Sound('strike.wav')
music_boi = mixer.Sound('v_boi.wav')
music_boi1 =  mixer.Sound('vzmax2.wav')
music_boi3 =mixer.Sound('vzmax1.wav')
music_boi4 =mixer.Sound('axe-hit-shield.wav')
music_boi5 = mixer.Sound('firebol.wav')
#МУЗЫКА КОНЦОВКИ
music_end =  mixer.Sound('screen_end.wav')
#МУЗЫКА В МЕНЮ
music_main = mixer.Sound('main_m.wav')
sound_m = 0 #Счётчик музыки в меню
sound = 0#кол-во проигрований музыки
blok= False#перменная определяющая блок
fireboll = 0#переменная определяющая количество фаерболов
konec = False#определение конца игры
#меню паузы
win_pause = GameSprite('fon.png',300,150,700,400)
while run:
    #создание врагов и героя в бою
    if vibor_vspom_1 and spawn1 == 0:
        firebol = Player('bullet.png',0,0,600,600,5,2,2,2,100)
        hero_1 = Player('hero.png',1300,600,130,170,10,10,10,2,5)#герой
        skeleton = Player('vrag2.png',100,600,130,170,10,10,10,2,2)#скелет
        voin = Player('vrag.png',100,600,130,170,7,7,15,7,6)#рыцарь
        mag =  Player('vrag3mag.png',100,600,130,170,7,7,10,10,0)#маг
        spawn1 +=1
    if vibor_vspom_2 and spawn1 == 0:
        firebol = Player('bullet.png',0,0,600,600,5,2,2,2,100)
        hero_1 = Player('hero.png',1300,600,130,170,10,10,7,2,5)#герой
        skeleton = Player('vrag2.png',100,600,130,170,10,10,10,3,3)#скелет
        voin = Player('vrag.png',100,600,130,170,7,7,20,20,4)#рыцарь
        mag = Player('vrag3mag.png',100,600,130,170,7,7,15,10,0)#маг
        spawn1 +=1   

    #надписи интерфейса и информации героя
    #стиль
    win = font.render(stil,True,DARK_BLUE)
    win_1 = font.render('Стиль:',True,DARK_BLUE)
    win_2 = font.render('Текущий стиль:',True,DARK_BLUE)
    # деньги
    win2 = font.render(str(money),True,DARK_BLUE)
    win2_vspom = font.render('Сэн',True,DARK_BLUE)
    win2_vspom2 = font.render('Текущее количество денег:',True,DARK_BLUE)
    #уровень
    win3 = font.render(str(level),True,DARK_BLUE)
    win3_1 = font.render('Уровень:',True,DARK_BLUE)
    win3_2 = font.render('Текущий уровень:',True,DARK_BLUE)
    #опыт
    win4 = font.render(str(opit),True,DARK_BLUE)
    win4_0 = font.render('Опыт:',True,DARK_BLUE)
    win4_1 = font.render('/ 1000',True,DARK_BLUE)
    win4_2 = font.render('/ 2000',True,DARK_BLUE)
    win4_3 = font.render('/ 3000',True,DARK_BLUE)
    win4_4 = font.render('/ max',True,DARK_BLUE)
    win4_5 = font.render('Текущее количество опыта:',True,DARK_BLUE)

    window.fill((LIGHT_BLUE))

    #выход
    ataka= False#перменная определяющая атаку
    pause= False#пауза в игре
    for e in event.get():
        keys = key.get_pressed()
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                pause = True
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x,y = e.pos

            #выбор сложности
            if vibor1.collidepoint(x,y) and vibor_vspom:
                vibor_vspom_1 = True
            if vibor2.collidepoint(x,y) and vibor_vspom:
                vibor_vspom_2 = True
            #выход через крестик из окон
            if spravka_kod and krest_kod.collidepoint(x,y):
                spravka_kod = False
            if spravka3 and krest.collidepoint(x,y):
                spravka3 = False
            if spravka and krest.collidepoint(x,y):
                spravka = False
            if spravka2 and krest.collidepoint(x,y):
                spravka2 = False
            if info_hero and krest.collidepoint(x,y):
                info_hero = False
            #проверка нажатия на codes
            if codes.collidepoint(x,y):
                codess = True
            #проверка нажатий на вспомогательные значки

            if icon_boi.collidepoint(x,y):
                boi = True
                main = False
                magaz = False
                info_hero = False
                spravka2 = False
                if z == 0:
                    spravka = True
                    z+=1
            #проверка уровня перед боем и выбор противника
            if skeleton_icon_vspom.collidepoint(x,y) and level >= 0 and boi:
                boi_skelet = True
                boi_in = True
                boi = False
            if voin_icon_vspom.collidepoint(x,y) and level >= 2 and boi:
                Boi_voin = True
                boi_in = True
                boi = False
            if mag_icon_vspom.collidepoint(x,y) and level >= 3 and boi:
                boi_mag = True
                boi_in = True
                boi = False
            #кнопка выхода из боя
            if vuixod_iz_boi.collidepoint(x,y) and boi_in:
                boi_in= False
                boi = True
                boi_mag = False
                boi_skelet = False
                Boi_voin = False


            #магазин
            if icon3_magaz.collidepoint(x,y):
                info_hero = False
                main = False
                boi = False
                spravka = False
                spravka2 = False
                magaz = True
                if m == 0:
                    spravka3 = True
                    m+=1
            #стиль 1
            if stil1.collidepoint(x,y) and level >= 1 and money >= 1000 and magaz:
                if stil != 'Стиль синоби' and stil != 'Стиль Муссин' and a!= 1:
                    stil = 'Стиль храма Сэмпо'
                    money = money - 1000
                    a +=1

            # стиль 2
            if stil2.collidepoint(x,y) and level >= 2 and money >= 2000 and magaz:
                if stil != 'Стиль Муссин' and b != 1:
                    stil = 'Стиль синоби'
                    money = money-2000
                    b+=1
            # стиль 3
            if stil3.collidepoint(x,y) and level >= 3 and money >= 3000 and magaz:
                if c!=1:
                    stil = 'Стиль Муссин'
                    money = money-3000
                    c+=1
            if pause:
                pause = False
            if hero_win and krest_kod.collidepoint(x,y) and boi:
                hero_win = False
            if win_vrag and krest_kod.collidepoint(x,y) and boi:
                win_vrag = False
            if boi_in:
                ataka = True
                blok = False
            #информация о герое
            if icon2_info_hero.collidepoint(x,y):
                info_hero = True
            #закрытие концовки
            if konec:
                run = False
        if e.type == MOUSEBUTTONDOWN and e.button == 3 and boi_in:
            if boi_in:
                blok = True
                ataka = False
                
    if boi_in == False and sound_m == 0:
        music_boi.stop()
        music_main.play(-1)
        sound_m += 1
        sound = 0
    #main
    if main:
        win_main.reset()
    #рисовка магазина    
    if magaz:
        stil1.reset()
        stil2.reset()
        stil3.reset()
        win_magaz.reset()
    # рисовка в бою
    if boi_in:

        if sound == 0:
            music_main.stop()
            music_boi.play(-1)
            sound +=1
            sound_m = 0
        vuixod_iz_boi.reset()
        arena_boi.reset()
        #основные условия проверки в бою
        if boi_skelet:
            #рисовка
            hero_1.reset()
            skeleton.reset()
            #атака
            if ataka:
                music_boi1.play()
                #удар и выпад если  координаты героя больше или равны координатам врага
                if hero_1.rect.x >= skeleton.rect.x + 50:
                    hero_1.rect.x -= 30
                #проверка блока у врага
                if hero_1.rect.x <= skeleton.rect.x + 50:
                    music_boi2.play()
                    hero_1.strike(skeleton)
                    ataka = False
            #провепка атаки врага
            if randint(1,4) == 1:
                music_boi3.play()
                # если координаты врага меньше координатов героя то он может сделать выпад
                if skeleton.rect.x <= hero_1.rect.x:
                    skeleton.rect.x += 10
                else:
                    skeleton.rect.x -= 30
                if skeleton.rect.x >= hero_1.rect.x -50 and skeleton.power > hero_1.armor and blok:
                    music_boi2.play()
                    skeleton.strike(hero_1)
                elif skeleton.power <= hero_1.armor and skeleton.rect.x >= hero_1.rect.x -100 and blok:
                    music_boi4.play()
                elif blok == False and skeleton.rect.x >= hero_1.rect.x -50:
                    music_boi2.play()
                    skeleton.strike(hero_1)

            #проверка хп
            if skeleton.health <= 0:
                hero_win = True
                boi_in = False
                boi = True
                spawn1 -= 1
                boi_skelet = False
                money += 500
                opit += 1000
            if hero_1.health <=0:
                win_vrag = True
                boi_in = False
                boi = True
                boi_skelet =False
                spawn1 -= 1            
            #отображение победы и поражения
            skeleton.enemy_update(hero_1)
            hero_1.update()

        #бой с рыцарем
        if Boi_voin:
            #рисовка
            hero_1.reset()
            voin.reset()
            #атака
            if ataka:
                music_boi1.play()
                #удар и выпад если  координаты героя больше или равны координатам врага
                if hero_1.rect.x >= voin.rect.x + 50:
                    hero_1.rect.x -= 30
                #проверка блока у врага
                if hero_1.rect.x <= voin.rect.x + 50:
                    hero_1.strike(voin)
                    ataka = False
                    music_boi2.play()
            #провепка атаки врага
            if randint(1,4) == 1:
                music_boi3.play()
                # если координаты врага меньше координатов героя то он может сделать выпад
                if voin.rect.x <= hero_1.rect.x:
                    voin.rect.x += 10
                else:
                    voin.rect.x -= 30
                if voin.rect.x >= hero_1.rect.x -50 and voin.power > hero_1.armor and blok:
                    music_boi2.play()
                    voin.strike(hero_1)
                elif voin.power <= hero_1.armor and voin.rect.x >= hero_1.rect.x -50 and blok:
                    music_boi4.play()
                elif blok == False and skeleton.rect.x >= hero_1.rect.x -50:
                    music_boi2.play()
                    voin.strike(hero_1)
            #проверка хп
            if voin.health <= 0:
                hero_win = True
                boi_in = False
                boi = True
                Boi_voin = False
                spawn1 -= 1
                money += 2000
                opit += 2000
            if hero_1.health <=0:
                win_vrag = True
                boi_in = False
                boi = True
                Boi_voin = False
                spawn1 -= 1
            voin.enemy_update(hero_1)
            hero_1.update()
        #бой с магом
        if boi_mag:
            #рисовка
            hero_1.reset()
            mag.reset()
            #атака мага(в любом случае ваншот т.к. такой конец требуется для продолжения игры)
            if fireboll == 0:
                music_boi5.play()
                fireboll +=1
            firebol.reset()
            firebol.update_firebol(mag)
            if firebol.rect.x >= hero_1.rect.x -300:
                firebol.strike(hero_1)
            #проверка хп
            if hero_1.health <=0:
                win_vrag = True
                konec = True              
                spawn1 -=1
            elif voin.rect.x >= hero_1.rect.x -50 and blok:
                firebol.reset()
                firebol.update_firebol(mag)
            mag.enemy_update(hero_1)
            hero_1.update()
        if level == 1 and health_chet == 0:
            if opit >= 2000:
                level = 2
                hero_1.health = 12
                opit = 0
                health_chet +=1
        if level == 2 and health_chet == 0: 
            if opit >= 3000:
                level = 3
                hero_1.health = 14
                opit = 0
                health_chet +=1
        if level ==0 and health_chet == 0:
            if opit >= 1000:
                level = 1
                hero_1.health = 10
                opit = 0
                health_chet +=1
        if level >= 3 and health_chet == 0:
            hero_1.health = 17
            health_chet +=1
    #рисовка меню выбора боя
    if boi:
        skeleton_icon_vspom.reset()
        voin_icon_vspom.reset()
        mag_icon_vspom.reset()
    if boi:
        main_boi.reset()
        if hero_win:
            krest_kod.reset()
            victory.reset()
        if win_vrag:
            krest_kod.reset()
            loose.reset()
    #рисовка креста для закрытия окон
    if spravka or spravka3:
        krest.reset()
    # информация о герое
    if info_hero:
        #ПРОВЕРКА УРОВНЯ
        if level == 0:
            hero_1.health = 10
        if level == 1:
            hero_1.health = 12
        if level == 2:
            hero_1.health = 14
        if level == 3:
            hero_1.health = 17
        #информация о характерисиках игрока
        win_health_hero = font.render('Жизнь - ',True,DARK_BLUE)
        win_health_hero1 = font.render(str(hero_1.health),True,DARK_BLUE)
        win_armor_hero = font.render('Блок -',True,DARK_BLUE)
        win_armor_hero1 = font.render(str(hero_1.armor),True,DARK_BLUE)
        win_power_hero = font.render('Атака -',True,DARK_BLUE)
        win_power_hero1 = font.render(str(hero_1.power),True,DARK_BLUE)


        win_info_hero.reset()
        #имя
        window.blit(win_name, (520, 180))
        #характеристики
        window.blit(win_health_hero,(590,180))
        window.blit(win_health_hero1,(680,180))
        window.blit(win_armor_hero,(730,180))
        window.blit(win_armor_hero1,(800,180))
        window.blit(win_power_hero,(850,180))
        window.blit(win_power_hero1,(940,180))
        #уровень
        window.blit(win3_2, (500, 245))
        window.blit(win3, (750, 245))
        #деньги
        window.blit(win2_vspom2,(500,415))
        window.blit(win2,(850,415))
        window.blit(win2_vspom,(950,415))
        #стиль
        window.blit(win_2,(500,360))
        window.blit(win,(700,360))
        #опыт
        window.blit(win4_5,(500,300))
        window.blit(win4,(850,300))

        if level ==0:
            window.blit(win4_1, (905, 300))
        if level == 1:
            window.blit(win4_2, (905, 300))        
        if level == 2:
            window.blit(win4_3, (905, 300))
        if level == 3:
            window.blit(win4_4, (905, 300))        
    #рисовка  справок
    if spravka2:
        win_spravka2.reset()
    if spravka:
        win_spravka.reset()
    if spravka3:
        win_spravka3.reset()
    #общие свединья в интерфейсе игры(верхняя панелька)
    if boi_in == False:
        health_chet = 0
        codes.reset()
        #Уровень
        window.blit(win3_1, (150, 10))
        window.blit(win3, (290, 10))
        #деньги
        window.blit(win2, (450, 10))
        window.blit(win2_vspom, (550, 10))
        #Опыт
        if level ==0:

            window.blit(win4_0, (700, 10))
            window.blit(win4, (780, 10))
            window.blit(win4_1, (880, 10))
        if level == 1:
            window.blit(win4_0, (700, 10))
            window.blit(win4, (780, 10))
            window.blit(win4_2, (880, 10))        
        if level == 2:
            window.blit(win4_0, (700, 10))
            window.blit(win4, (780, 10))
            window.blit(win4_3, (880, 10))
        if level == 3:
            window.blit(win4_0, (700, 10))
            window.blit(win4, (780, 10))
            window.blit(win4_4, (880, 10))
        #стиль
        window.blit(win, (1100, 10))
        window.blit(win_1, (1000, 10))
    #рисовка  иконки codes
    if spravka_kod:
        krest_kod.reset()
        win_spravka_kod.reset()
    # изменение ресуров если codess = True
    if codess:
        level = 3
        money = 100000
        opit = 3000
    #выбор сложности
    if vibor_vspom and spravka_kod == False:
        vibor1.reset()
        vibor2.reset()
        vibor.reset()
        if vibor_vspom_1 or vibor_vspom_2:
            vibor_vspom = False
    #конец
    if konec:
        music_boi.stop()
        music_main.stop()
        music_end.set_volume(0.1)
        music_end.play(-1)
        theend.reset()
        win_konec = font.render('Нажмите лкм',True,DARK_BLUE)
        window.blit(win_konec,(0,0))
    while pause:
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                pause = False
        win_pause.reset()
        display.update()
        clock.tick(80)
    #интерфейс в бою

    if boi_in:
        #интерфейс в бою
        win_armor_vs =font.render('armor:',True,DARK_BLUE)
        win_health_vs =font.render('hp:',True,DARK_BLUE)
        win_hero = font.render(str(hero_1.health),True,DARK_BLUE)
        win_hero1 = font.render(str(hero_1.armor),True,DARK_BLUE)
        win_skelet = font.render(str(skeleton.health),True,DARK_BLUE)
        win_skelet1 = font.render(str(skeleton.armor),True,DARK_BLUE)
        win_voin = font.render(str(voin.health),True,DARK_BLUE)
        win_voin1 = font.render(str(voin.armor),True,DARK_BLUE)
        win_mag = font.render('???',True,DARK_BLUE)
        win_mag1 = font.render('???',True,DARK_BLUE)
        #его рисование
        health_win_hero.reset()
        health_win_vrag.reset()
        armor_win_hero.reset()
        armor_win_vrag.reset()
        window.blit(win_armor_vs,(1270,150))
        window.blit(win_armor_vs,(0,150))
        window.blit(win_health_vs,(1270,100))
        window.blit(win_health_vs,(0,100))
        window.blit(win_hero, (1330, 100))
        window.blit(win_hero1, (1340, 150))

        if Boi_voin:
            window.blit(win_voin, (50, 100))
            window.blit(win_voin1, (70, 150))
        if boi_skelet:
            window.blit(win_skelet, (50, 100))
            window.blit(win_skelet1, (70, 150))
        if boi_mag:
            window.blit(win_mag, (50, 100))
            window.blit(win_mag1, (70, 150))    


    #изменение параметров из за стилей
    if stil == 'Стиль храма Сэмпо':
        if vibor_vspom_1:
            hero_1.armor = 6
            hero_1.power = 6
        if vibor_vspom_2:
            hero_1.armor = 5
            hero_1.power = 5
    if stil =='Стиль Муссин':
        if vibor_vspom_1:
            hero_1.armor = 10
            hero_1.power = 10
        if vibor_vspom_2:
            hero_1.armor = 9
            hero_1.power = 15
    if stil == 'Стиль синоби':
        if vibor_vspom_1:
            hero_1.armor = 8
            hero_1.power = 8
        if vibor_vspom_2:
            hero_1.armor = 7
            hero_1.power = 10
 #влючаем движение
    display.update()
    clock.tick(80)
while konec:
    for e in event.get():
        if e.type == QUIT:
            run = False
            konec = False
    theend2.reset()
    display.update()
    clock.tick(80)