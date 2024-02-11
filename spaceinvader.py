import pygame
import time
import random
import os

pygame.font.init()

WIDTH=500
HEIGHT=400

PLAYER_WIDTH=20
PLAYER_HIEGHT=60

STAR_WIDTH=10
STAR_HIEGHT=10
STAR_VEL=3

PLAYER_VEL=4




BG_IMG=pygame.transform.scale(pygame.image.load(os.path.join("assets","bg.jpeg")),(WIDTH,HEIGHT))

WIN=pygame.display.set_mode((WIDTH,HEIGHT))

FONT=pygame.font.SysFont("comicsans",20)

pygame.display.set_caption("space invader")


def draw(player,elapsed_time,stars):

	WIN.blit(BG_IMG,(0,0))

	font_text=FONT.render(f"Time : {round(elapsed_time)} s",1,"white")
	WIN.blit(font_text,(15,15))

	for star in stars:
		pygame.draw.rect(WIN,"white",star)

	pygame.draw.rect(WIN,"light blue",player)
	pygame.display.update()


def main():

	run=True

	hit=False

	player=pygame.Rect(360,HEIGHT-PLAYER_HIEGHT-12,PLAYER_WIDTH,PLAYER_HIEGHT)

	clock=pygame.time.Clock()
	start_time=time.time()
	elapsed_time=0

	star_add_increment=2000
	star_count=0

	stars=[]

	while run:

		star_count+=clock.tick(60)
		print(star_count)
		elapsed_time=time.time()-start_time

		if star_count>star_add_increment:

			for i in range(8):
				star_x=random.randint(5,WIDTH-STAR_WIDTH)
				star_y=random.randint(5,150)
				star=pygame.Rect(star_x-10,-star_y,STAR_WIDTH,STAR_HIEGHT)
				stars.append(star)

			star_add_increment=max(200,star_add_increment-20)
			star_count=0
		

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run=False
				break

		keys=pygame.key.get_pressed()

		if keys[pygame.K_LEFT] and player.x>5:
			player.x-=PLAYER_VEL

		if keys[pygame.K_RIGHT] and player.x<WIDTH- PLAYER_WIDTH-5:
			player.x+=PLAYER_VEL

		for star in stars[:]:
			star.y+=STAR_VEL

			if star.y > HEIGHT:
				stars.remove(star)

			elif star.y+STAR_HIEGHT>=player.y and star.colliderect(player):
				stars.remove(star)
				hit=True
				break

		if hit:
			LOST_TEXT=FONT.render("You lost",1,"white")
			WIN.blit(LOST_TEXT,(WIDTH/2-LOST_TEXT.get_width()/2,HEIGHT/2-LOST_TEXT.get_height()))
			pygame.display.update()
			pygame.time.delay(5000)
			break

		


		draw(player,elapsed_time,stars)



if __name__ == '__main__':
	main()
