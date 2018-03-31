import pygame
import sys
from login import *
from sinup import *
pygame.init()

pygame.mixer.music.load('start.mp3')
pygame.mixer.music.play(0)

display_width=900
display_hieght=500
b=(display_width/2)
a=(display_hieght/2)
disp=pygame.display.set_mode((display_width,display_hieght))
pygame.display.set_caption('Holli Music')
pic=pygame.image.load('img.jpg')
clock=pygame.time.Clock()
x=0
y=0
button1=pygame.Rect(350,179,200,50)
button2=pygame.Rect(350,259,200,50)
black=(212,175,55)
white=(255,255,255) 
grey=(25,50,92)
l_grey=(236,236,236)
def text_objects(text,font,colour):
	textSurface= font.render(text,True, colour)
	return textSurface, textSurface.get_rect()
	
def message_display(text,y,x,size,colour):
	largeText=pygame.font.Font('freesansbold.ttf',size)
	TextSurf, TextRect = text_objects(text,largeText,colour)
	TextRect.center= (y,x)
	disp.blit(TextSurf,TextRect)
	
def heading():
	global a
	while(a>=100):
		message_display("Hooli Music",b,a,115,white)
		a-=1

		pygame.display.update()
		back(x,y)
	message_display("Hooli Music",b,a,115,white)
def back(x,y):
	disp.blit(pic,(x,y))
crashed=False

while not crashed:
	mouse=pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			crashed=True
		if event.type == pygame.MOUSEBUTTONDOWN and button1.collidepoint(mouse):
			pygame.quit()
			login()
		if event.type == pygame.MOUSEBUTTONDOWN and button2.collidepoint(mouse):
			pygame.quit()
			sinup()
		
	back(x,y)
	heading()
	pygame.draw.rect(disp,grey,button1)
	pygame.draw.rect(disp,grey,button2)
	if(button1.collidepoint(mouse)):
		pygame.draw.rect(disp,l_grey,button1)
	if(button2.collidepoint(mouse)):
		pygame.draw.rect(disp,l_grey,button2)
	message_display("Login",448,200,30,black)
	message_display("Sign-Up",449,280,30,black)
	pygame.display.update()
	#clock.tick(100)
pygame.quit()
quit()
