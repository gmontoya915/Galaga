import pygame
from Spaceship import *
from Alien import *
import constants
from bullet import *
from star import *
from Boss import*
from Highscore import*
##largestNumber = 0
##file = open('test.txt', 'r')
##
##for line in file:
##    if line > largestNumber:
##        largestNumber = line
#print largestNumber
boss_spawner = 0
pygame.init()
screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]) 
ss = Spaceship()
a = Alien(800,100)
direction_counter = 50
bullet_counter = 0
bullets = []
aliens = [a]
stars = []
bosses = []
mode = "playing"
lose = pygame.image.load('you-lose-i-win.jpg')
lose = pygame.transform.scale(lose,(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT ))
score = 0 
score_font = pygame.font.SysFont("Times New Roman", 100) 
alien_spawner = 0
def hit_Spaceship(bullet):
	 if bullet.x > ss.x and bullet.x < ss.x + ss.width and bullet.y > ss.y and bullet.y < ss.y + ss.height:
			if bullet.bullet_type == constants.ALIEN_BULLET:
				return True
def hit_alien(bullet):
    global score
    for a in aliens:
        if bullet.x > a.x and bullet.x < a.x + a.width and bullet.y > a.y and bullet.y < a.y + a.height:
            if bullet.bullet_type == constants.SPACESHIP_BULLET:
                aliens.remove(a)
                score = score + 1
                return True

def update_bullets():
    global mode
    for b in bullets:
        b.move()
        if hit_alien(b) or b.is_offscreen():
            bullets.remove(b)
        if hit_Spaceship(b):
            mode = "lose"
            #f = open("test.txt","a") #opens file with name of "test.txt"
            #f.write(str (score) +"\n")
            #f.close
            Highscore.write_score(score)            



def update_stars():
	for s in stars:
		s.move()
		if s.y > constants.SCREEN_HEIGHT: 
			stars.remove(s)

def update_bosses():
	for b in bosses:
		b.update()
def update_aliens():
	for a in aliens:
		bullet = a.update()
		if bullet != None:
			bullets.append(bullet)
def spawn_aliens():
	for x in range(0,5):
		aliens.append(Alien(x*100,100))
def spawn_Boss(): 
	for x in range (0,1):
		bosses.append(Boss(x*200,0))

def update_counters():
	global direction_counter
	if direction_counter == 900:
		direction_counter = 0
		for a in aliens:
			a.reverse_direction()
			
	else:
		direction_counter = direction_counter + 1
	global bullet_counter
	if bullet_counter == 11:
		bullet_counter = 0
	else:
		bullet_counter = bullet_counter + 1

def generate_starRow():
	stars = []
	for x in range(constants.SCREEN_WIDTH):
		if random.randint(0,1000) == 1:
			stars.append(star(x,0))
	return stars

def holding_keys():
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		ss.move_up()
	if keys[pygame.K_DOWN]:
		ss.move_down()
	if keys[pygame.K_LEFT]:
		ss.move_left()
	if keys[pygame.K_RIGHT]:
		ss.move_right()
	if keys[pygame.K_SPACE] and bullet_counter == 0:
		bullets.append(ss.shoot()) 	
spawn_aliens()

while True:
    if mode == "playing":
    
        alien_spawner = alien_spawner + 1
        boss_spawner = boss_spawner + 1
        if alien_spawner == 110:
            spawn_aliens()
            alien_spawner = 0
        if boss_spawner == 500:
            spawn_Boss() 
            boss_spawner = 0


        holding_keys() 
        stars = stars + generate_starRow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(ss.shoot())
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bullet_counter = 0



        update_counters()
        update_bullets()
        update_aliens()
        update_stars()
        update_bosses()
        screen.fill([0,0,0])
        for s in stars:
            pygame.draw.rect(screen, [255,255,255], [s.x,s.y,s.width,s.height])
        for b in bullets:
            screen.blit(b.image,b.rect)
        for a in aliens: 
            screen.blit(a.image, a.rect)
        screen.blit (ss.image, ss.rect)
        for b in bosses:
            screen.blit(b.image, b.rect)

        label = score_font.render(str(score), 1, pygame.color.THECOLORS['white'])   
        screen.blit(label, (1000, 0))
        pygame.display.update()
        pygame.time.delay(20)
    
   
    if mode == "lose":
        screen.blit(lose, [0, 0])
        highscore_list = Highscore.get_top_scores(10)              
        Highscore.show_high_scores(pygame, screen, highscore_list, 0, 0)            
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        
