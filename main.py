import pygame
import random
import time, datetime

from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, RLEACCEL)
#Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED= (255,0,0)

BUGpng = pygame.image.load("bug.png")
BUGpng_scaled = pygame.transform.scale(BUGpng,(64,64))

JorgePNG = pygame.image.load("JorgeVJ.png")
JorgePNG_scaled = pygame.transform.scale(JorgePNG,(80,80))
a=3
b=5
class Enemy(pygame.sprite.Sprite):

    def __init__(self,a,b):
        super(Enemy, self).__init__()
        self.surf= BUGpng_scaled
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect= self.surf.get_rect(center=(SCREEN_WIDTH+100, random.randint(0, SCREEN_HEIGHT)))
        self.speed= random.randint(a,b)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()        


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf= JorgePNG_scaled
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect= self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-4)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,4)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-4,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(4,0)
        
        if self.rect.left < 0:
            self.rect.left=0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top=0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


''' iniciamos los modulos de pygame'''

pygame.init()

''' Creamos y editamos la ventana de pygame (escena) '''
''' 1.-definir el tamaño de la ventana'''
SCREEN_WIDTH = 1000   # revisar ancho de la imagen de fondo
SCREEN_HEIGHT = 700  # revisar alto de la imagen de fondo

''' 2.- crear el objeto pantalla'''
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
background_image = pygame.image.load("DCC.png")
background_image_scaled= pygame.transform.scale(background_image,(1000,700))

gamerover_image=pygame.image.load("Gameover.png")
inicio_image=pygame.image.load("inicio.jpg")
inicio_image_scaled= pygame.transform.scale(inicio_image,(1000,700))
#Creamos pantalla de inicio
pygame.display.set_caption("Pantalla de inicio")

#Creamos botones
font= pygame.font.Font(None, 64)

start_button = pygame.Rect(350, 250, 300, 100)
start_text = font.render("START", True, WHITE)
start_text_rect = start_text.get_rect(center=start_button.center)

difficulty_button = pygame.Rect(350, 400, 300, 100)
difficulty_text = font.render("DIFFICULTY", True, WHITE)
difficulty_text_rect = difficulty_text.get_rect(center=difficulty_button.center)

quit_button = pygame.Rect(350, 550, 300, 100)
quit_text = font.render("QUIT", True, WHITE)
quit_text_rect = quit_text.get_rect(center=quit_button.center)

easy_button= pygame.Rect(350,250,300,100)
easy_text= font.render("EASY",True,WHITE)
easy_text_rect= easy_text.get_rect(center=easy_button.center)

normal_button= pygame.Rect(350,400,300,100)
normal_text= font.render("NORMAL",True,WHITE)
normal_text_rect= normal_text.get_rect(center=normal_button.center)

hard_button= pygame.Rect(350,550,300,100)
hard_text= font.render("HARD",True,WHITE)
hard_text_rect= hard_text.get_rect(center=hard_button.center)

''' Preparamos el gameloop '''
''' 1.- creamos el reloj del juego'''

clock = pygame.time.Clock()
''' 2.- generador de enemigos'''

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 350)

''' 3.- creamos la instancia de jugador'''
player = Player()

''' 4.- contenedores de enemigos y jugador'''
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

''' hora de hacer el gameloop '''
def gameloop():
    running= True
    gameover= False
    gameover_tiempo=True
    difficulty= False
    inicio= True
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 350)
    player = Player() 
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    a=3
    b=5
    while running:
        while gameover==True:
            screen.blit(gamerover_image,[0,0])
            fuente_gameover= pygame.font.Font(None,50)
            text= fuente_gameover.render("Perdiste, si quieres continuar presione C",True,WHITE)
            text1= fuente_gameover.render("y si quieres salir presione Q",True,WHITE)
            screen.blit(text,(150,300))
            screen.blit(text1,(300,350))
            pygame.display.flip()

            if gameover_tiempo==True:    
                tiempo_final= datetime.datetime.now() - start_time
                minuto= tiempo_final.seconds//60
                segundos= tiempo_final.seconds % 60
                tiempo= "{:02d}:{:02d}".format(minuto, segundos)
                print("   -------------------------   ")
                print("  ---------------------------  ")
                print(" ----------------------------- ")
                print("-------------------------------")
                print("PERDISTE!! TU TIEMPO FUE: "+str(tiempo))
                print("-------------------------------")
                print(" ----------------------------- ")
                print("  ---------------------------  ")
                print("   -------------------------   ")
                gameover_tiempo=False
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and event.key==pygame.K_q:
                    running=False
                    gameover=False 
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_c:
                    gameloop()
                elif event.type==QUIT:
                    running=False
                    gameover=False
        while inicio==True:
            screen.blit(inicio_image_scaled,[0,0])
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running= False
                    inicio=False
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        inicio=False
                        start_time= datetime.datetime.now()
                    elif difficulty_button.collidepoint(event.pos):
                        difficulty= True
                        inicio=False
                    elif quit_button.collidepoint(event.pos):
                        running=False
                        inicio=False
            pygame.draw.rect(screen, GREEN, start_button)
            screen.blit(start_text, start_text_rect)
            pygame.draw.rect(screen, GRAY, difficulty_button)
            screen.blit(difficulty_text, difficulty_text_rect)
            pygame.draw.rect(screen, GRAY, quit_button)
            screen.blit(quit_text, quit_text_rect)
            pygame.display.flip()
        while difficulty==True:
            screen.blit(inicio_image_scaled,[0,0])
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running= False
                    inicio= False
                    difficulty= False
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if easy_button.collidepoint(event.pos):
                        a=0
                        b=3
                        pygame.time.set_timer(ADDENEMY, 500)
                        difficulty=False
                        start_time= datetime.datetime.now()
                    elif normal_button.collidepoint(event.pos):
                        a=3
                        b=5
                        pygame.time.set_timer(ADDENEMY, 350)
                        difficulty=False
                        start_time= datetime.datetime.now()
                    elif hard_button.collidepoint(event.pos):
                        a=5
                        b=10
                        pygame.time.set_timer(ADDENEMY, 200)
                        difficulty=False
                        start_time= datetime.datetime.now()
                    
            pygame.draw.rect(screen, GREEN, normal_button)
            screen.blit(normal_text, normal_text_rect)
            pygame.draw.rect(screen, GRAY, easy_button)
            screen.blit(easy_text, easy_text_rect)
            pygame.draw.rect(screen, RED, hard_button)
            screen.blit(hard_text, hard_text_rect)
            pygame.display.flip()
        

        screen.blit(background_image_scaled,[0,0])
        for event in pygame.event.get():
            if event.type==KEYDOWN and event.key==K_ESCAPE:
                running=False
            elif event.type == ADDENEMY:
                new_enemy= Enemy(a,b)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type==QUIT:
                running=False
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            gameover= True
        pressed_keys= pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        clock.tick(60)
        pygame.display.flip()

    pygame.QUIT()

gameloop()