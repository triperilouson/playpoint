import sys
import time
import pygame
from pygame.locals import *

from pygame import font


pygame.init()

#list_k =[pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP,pygame.K_RIGHT]e
pygame.display.set_caption("События от клавиатуры")
def text_get(text_quetion):
    while True:
        try:
            bag_deleted = text_quetion
            screen = pygame.display.set_mode((900, 600))
            screen.fill(0)
            f2 = pygame.font.SysFont('serif', 20)
            input_box = pygame.Rect(250, 400, 400, 100)
            color_inactive = pygame.Color((0, 128, 255))
            color = color_inactive
            text_quetion = f2.render(f'{text_quetion}', True, (0, 128, 255))
            text = ''
            place = text_quetion.get_rect(center=(450, 100))
            done = False
            #гдето здесь ошибка надо протыкать энтер
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_RETURN:
                            done = True
                            break

                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                if not done:
                    screen.fill((0, 0, 0))
                    pygame.draw.rect(screen, color, input_box, 2)
                    txt_surface = f2.render(text, True, color)
                    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
                    screen.blit(text_quetion, place)
                    pygame.display.flip()

                else:

                    break
            #if text =='':

            return int(text)
        except Exception:

            screen = pygame.display.set_mode((900, 600))
            screen.fill(0)
            f2 = pygame.font.SysFont('serif', 50)
            text_error = f2.render('enter true (int)', True, (0, 128, 255))
            place_error = text_error.get_rect(center=(450, 300))
            screen.blit(text_error, place_error)
            pygame.display.flip()
            time.sleep(5)
            text_quetion = bag_deleted
text =text_get(text_quetion='enter speed')
speed = text
text =text_get(text_quetion='enter size')
size= text
text =text_get(text_quetion='enter amount of turn')
amount = text
text =text_get(text_quetion='enter plays x belong to first player')
x= text
text =text_get(text_quetion='enter plays y belong to first player')
y = text
text =text_get(text_quetion='enter speed belong to player 2')
speed2 = text
text =text_get(text_quetion='enter size belong to player 2')
size2= text
text =text_get(text_quetion='enter place x belong to second player')
x1 = text
text =text_get(text_quetion='enter place y belong to second player')
y1 = text
text =text_get(text_quetion='what play you whant? 1, 2')
play = text
time_start= time.time()
def player_squre_race(x=x,y=y,x1=x1,y1=y1,speed=speed,size=size,time_start=time_start,size2=size2,speed2=speed2):
    yes = False
    f2 = pygame.font.SysFont('serif', 48)
    text1 = f2.render(f'1', True, (0, 128, 255))
    screen = pygame.display.set_mode((900, 600))
    place = text1.get_rect(center=(450, 300))
    done = False
    is_blue = True
    clock = pygame.time.Clock()
    count = 0
    pygame.display.set_caption("События от клавиатуры")
    pressed = pygame.key.get_pressed()
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    y -= speed
                elif event.key == pygame.K_DOWN:
                    y += speed
                elif event.key == pygame.K_RIGHT:
                    x += speed
                elif event.key == pygame.K_LEFT:
                    x -= speed

                elif event.key == pygame.K_KP_8:
                    y1 -= speed2
                elif event.key == pygame.K_KP_2:
                    y1 += speed2
                elif event.key == pygame.K_KP_6:
                    x1 += speed2
                elif event.key == pygame.K_KP_4:
                    x1 -= speed2
                #пауза что криво работает толко один раз
                elif pressed[K_SPACE]:
                   time.sleep(5)



        screen.fill(0)

        #time_on_screen_end = pygame.time.get_ticks() - time_on_screen
        #time_on_screen = (time_on_screen_end // 1000)
        time_on_screen = time.time() - time_start
        time_on_screen =time.gmtime(time_on_screen)
        time_yes = f2.render(f'{time_on_screen.tm_sec}', True, (0, 128, 255))
        place_time = time_yes.get_rect(center=(800, 15))
        if time_on_screen.tm_sec == 30:
            text_get(text_quetion='win blue player congratulations')
            done = True
        if pygame.Rect(x, y, size, size) in pygame.Rect(x1, y1, size2, size2):
            text_get(text_quetion='win white player congratulations')
            done = True
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, size, size))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x1, y1, size2, size2))
        screen.blit(text1, place)
        screen.blit(time_yes, place_time)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
if play == 1:
    player_squre_race(x=x,y=y,x1=x1,y1=y1,speed=speed,size=size,time_start=time_start,size2=size2,speed2=speed2)
elif play == 2:
    def play_without_sight(x=x,y=y,x1=x1,y1=y1,speed=speed,size=size,time_start=time_start,size2=size2,speed2=speed2,amount=amount):
        true = False
        f2 = pygame.font.SysFont('serif', 48)
        text1 = f2.render(f'1', True, (0, 128, 255))
        screen = pygame.display.set_mode((900, 600))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, size, size))
        place = text1.get_rect(center=(450, 300))
        screen.blit(text1, place)
        pygame.display.update()
        done = False
        is_blue = True
        clock = pygame.time.Clock()
        count = 0
        flag =1
        pygame.display.set_caption("События от клавиатуры")
        pressed = pygame.key.get_pressed()
        i = 0
        while not done:
            if (i//amount)%2==0:
                player_constant = 1
            elif (i//amount)%2==1:
                player_constant = 2

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN and player_constant == 1:

                    if event.key == pygame.K_UP:
                        i += 1
                        y -= speed
                    elif event.key == pygame.K_DOWN:
                        i += 1
                        y += speed
                    elif event.key == pygame.K_RIGHT:
                        x += speed
                        i+=1
                    elif event.key == pygame.K_LEFT:
                        i += 1
                        x -= speed
                elif event.type == pygame.KEYDOWN and player_constant == 2:

                    if event.key == pygame.K_KP_8:
                        i += 1
                        y1 -= speed2
                    elif event.key == pygame.K_KP_2:
                        i += 1
                        y1 += speed2
                    elif event.key == pygame.K_KP_6:
                        i += 1
                        x1 += speed2
                    elif event.key == pygame.K_KP_4:
                        i += 1
                        x1 -= speed2
            screen.fill(0)
            text_player_number = f2.render(f'{player_constant}', True, (0, 128, 255))
            place_player_number = text_player_number.get_rect(center=(450, 300))
            screen.blit(text_player_number, place_player_number)
            time_on_screen = time.time() - time_start
            time_on_screen = time.gmtime(time_on_screen)
            time_yes = f2.render(f'{time_on_screen.tm_sec}', True, (0, 128, 255))
            place_time = time_yes.get_rect(center=(800, 15))
            if pygame.Rect(x, y, size, size) in pygame.Rect(x1, y1, size2, size2):
                text_get(text_quetion=f'win {player_constant} player congratulations')
                time.sleep(5)
                break

            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, size, size))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x1, y1, size2, size2))

            screen.blit(time_yes, place_time)
            pygame.display.flip()
            clock.tick(60)


    play_without_sight(x=x, y=y, x1=x1, y1=y1, speed=speed, size=size, time_start=time_start, size2=size2,speed2=speed2,amount=amount)
else:
    text_get(text_quetion='you do not want play....')
