import pygame
import MySQLdb as sql
import urllib.request
import json
import tkinter as tk
from tkinter import *
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from apiclient import discovery
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import json
import webbrowser as wb
class ui:
	def __init__(self,user,conn):
		pygame.init()
		self.artist=[]
		self.song=[]
		self.tag=0
		DEVELOPER_KEY = "AIzaSyDN5BMduRd5uM1HgycDdPieJokgAEGzExI"
		YOUTUBE_API_SERVICE_NAME = "youtube"
		YOUTUBE_API_VERSION = "v3"
		self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
		self.username=user
		self.displ=pygame.display.set_mode((1250,700))
		pygame.display.update()
		pygame.display.set_caption('WELCOME TO HOOLI MUSIC')
		self.clock=pygame.time.Clock()
		pygame.display.update()
		self.con=conn
		self.api_key='4862f153fba7cd366337ead11e3e2659 '
		self.con.query("select country from user where(username='"+self.username+"');")
		self.data=self.con.store_result()
		self.data=self.data.fetch_row()
		self.country=self.data[0][0]
		url="http://ws.audioscrobbler.com/2.0/?method=geo.gettoptracks&country="+self.country+"&api_key="+self.api_key+"&format=json"
		self.data=urllib.request.urlopen(url).read()
		self.data=self.data.decode("utf-8")
		self.data=json.loads(self.data)
		self.sym()
		crashed=False
		loadx=350
		loady=150
		while not crashed:
			self.con.close()
			self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
			fontobj=pygame.font.Font('freesansbold.ttf',60)
			textsurf=fontobj.render("HOOLI ",True,(255,140,0))
			textre=textsurf.get_rect()
			textre.center=(130,32)
			self.displ.blit(textsurf,textre)
			fontobj=pygame.font.Font('freesansbold.ttf',60)
			textsurf=fontobj.render("MUSIC",True,(255,255,255))
			textre=textsurf.get_rect()
			textre.center=(250,80)
			self.displ.blit(textsurf,textre)
			orange=(255,140,0)
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render(self.username,True,(255,255,0))
			textre=textsurf.get_rect()
			textre.center=(210,120)
			self.displ.blit(textsurf,textre)
			button1=pygame.Rect(20,159,200,50)
			pygame.draw.rect(self.displ,orange,button1)
			button2=pygame.Rect(20,219,200,50)
			pygame.draw.rect(self.displ,orange,button2)
			button3=pygame.Rect(20,279,200,50)
			pygame.draw.rect(self.displ,orange,button3)
			button4=pygame.Rect(20,339,200,50)
			pygame.draw.rect(self.displ,orange,button4)
			button5=pygame.Rect(20,399,200,50)
			pygame.draw.rect(self.displ,orange,button5)
			button6=pygame.Rect(20,459,200,50)
			pygame.draw.rect(self.displ,orange,button6)
			button7=pygame.Rect(20,519,200,50)
			pygame.draw.rect(self.displ,orange,button7)
			button8=pygame.Rect(20,579,200,50)
			pygame.draw.rect(self.displ,orange,button8)
			button9=pygame.Rect(378,20,200,50)
			pygame.draw.rect(self.displ,orange,button9)
			button10=pygame.Rect(595,20,200,50)
			pygame.draw.rect(self.displ,orange,button10)
			button11=pygame.Rect(812,20,200,50)
			pygame.draw.rect(self.displ,orange,button11)
			button12=pygame.Rect(1029,20,200,50)
			pygame.draw.rect(self.displ,orange,button12)
			
			
			for event in pygame.event.get():
				mouse=pygame.mouse.get_pos()
				if event.type== pygame.QUIT:
					crashed=True
				if(button1.collidepoint(mouse) and event.type==pygame.MOUSEBUTTONDOWN):
					self.popular_artist()
				if(button2.collidepoint(mouse) and event.type==pygame.MOUSEBUTTONDOWN):
					self.popular_song()
				if(button3.collidepoint(mouse) and event.type==pygame.MOUSEBUTTONDOWN):
					self.searched_song()
				if(button4.collidepoint(mouse) and event.type==pygame.MOUSEBUTTONDOWN):
					self.searched_album()
				if(button5.collidepoint(mouse) and event.type==pygame.MOUSEBUTTONDOWN):
					self.searched_artist()	
				if(button6.collidepoint(mouse) and event.type==pygame.MOUSEBUTTONDOWN):
					self.my_song()
				if(button7.collidepoint(mouse) and event.type==pygame.MOUSEBUTTONDOWN):
					self.my_artist()
				if(button8.collidepoint(mouse) and event.type==pygame.MOUSEBUTTONDOWN):
					crashed=True
				if(button9.collidepoint(mouse) and event.type==pygame.MOUSEBUTTONDOWN):
					self.temp1=tk.Tk()
					self.temp1.geometry("{}x{}".format(300,300))
					self.temp1.title("Song Search")
					t=tk.Label(self.temp1,text="Enter Song Name",font="Helvetical 10")
					t.place(x=10,y=5)
					self.wigdet=tk.Entry(self.temp1)
					self.wigdet.place(x=10,y=20)
					m=tk.Button(self.temp1,text="Submit",command=self.song_s)
					m.place(x=30,y=50)
				if(button10.collidepoint(mouse) and event.type==pygame.MOUSEBUTTONDOWN):
					self.temp1=tk.Tk()
					self.temp1.geometry("{}x{}".format(300,300))
					self.temp1.title("Artist Search")
					t=tk.Label(self.temp1,text="Enter Artist Name",font="Helvetical 10")
					t.place(x=10,y=5)
					self.wigdet=tk.Entry(self.temp1)
					self.wigdet.place(x=10,y=20)
					m=tk.Button(self.temp1,text="Submit",command=self.artist_s)
					m.place(x=30,y=50)
				if(button11.collidepoint(mouse) and event.type==pygame.MOUSEBUTTONDOWN):
					self.temp1=tk.Tk()
					self.temp1.geometry("{}x{}".format(300,300))
					self.temp1.title("Album Search")
					t=tk.Label(self.temp1,text="Enter Album Name",font="Helvetical 10")
					t.place(x=10,y=5)
					self.wigdet=tk.Entry(self.temp1)
					self.wigdet.place(x=10,y=20)
					m=tk.Button(self.temp1,text="Submit",command=self.album_s)
					m.place(x=30,y=50)
				if(button12.collidepoint(mouse) and event.type==pygame.MOUSEBUTTONDOWN):
					self.profile()
				if(mouse[0]>350 and mouse[0]<=523 and mouse[1]>150 and mouse[1]<=320 and event.type == pygame.MOUSEBUTTONDOWN):
					self.search_response = self.youtube.search().list(q=self.song[0],part="id,snippet",maxResults=10).execute()
					stamp=datetime.now()
					stamp=str(stamp)
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into logs(username,at,song,artist) values('"+self.username+"','"+stamp+"','"+self.song[0]+"','"+self.artist[0]+"');")
					self.con.commit()
					self.play()
				elif(mouse[0]>551 and mouse[0]<=720 and mouse[1]>150 and mouse[1]<=320 and event.type == pygame.MOUSEBUTTONDOWN):
					self.search_response = self.youtube.search().list(q=self.song[1]+" by "+self.artist[1],part="id,snippet",maxResults=10).execute()
					stamp=datetime.now()
					stamp=str(stamp)
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into logs(username,at,song,artist) values('"+self.username+"','"+stamp+"','"+self.song[1]+"','"+self.artist[1]+"');")
					self.con.commit()
					self.play()	
				elif(mouse[0]>753 and mouse[0]<=923 and mouse[1]>150 and mouse[1]<=320 and event.type == pygame.MOUSEBUTTONDOWN):
					self.search_response = self.youtube.search().list(q=self.song[2]+" by "+self.artist[2],part="id,snippet",maxResults=10).execute()
					stamp=datetime.now()
					stamp=str(stamp)
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into logs(username,at,song,artist) values('"+self.username+"','"+stamp+"','"+self.song[2]+"','"+self.artist[2]+"');")
					self.con.commit()
					self.play()	
				elif(mouse[0]>950 and mouse[0]<=1122 and mouse[1]>150 and mouse[1]<=320 and event.type == pygame.MOUSEBUTTONDOWN):
					self.search_response = self.youtube.search().list(q=self.song[3]+" by "+self.artist[3],part="id,snippet",maxResults=10).execute()
					stamp=datetime.now()
					stamp=str(stamp)
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into logs(username,at,song,artist) values('"+self.username+"','"+stamp+"','"+self.song[3]+"','"+self.artist[3]+"');")
					self.con.commit()
					self.play()	
				elif(mouse[0]>350 and mouse[0]<=523 and mouse[1]>399 and mouse[1]<=570 and event.type == pygame.MOUSEBUTTONDOWN):
					self.search_response = self.youtube.search().list(q=self.song[4]+" by "+self.artist[4],part="id,snippet",maxResults=10).execute()
					stamp=datetime.now()
					stamp=str(stamp)
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into logs(username,at,song,artist) values('"+self.username+"','"+stamp+"','"+self.song[4]+"','"+self.artist[4]+"');")
					self.con.commit()
					self.play()	
				elif(mouse[0]>551 and mouse[0]<=720 and mouse[1]>399 and mouse[1]<=570 and event.type == pygame.MOUSEBUTTONDOWN):
					self.search_response = self.youtube.search().list(q=self.song[5]+" by "+self.artist[5],part="id,snippet",maxResults=10).execute()
					stamp=datetime.now()
					stamp=str(stamp)
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into logs(username,at,song,artist) values('"+self.username+"','"+stamp+"','"+self.song[5]+"','"+self.artist[5]+"');")
					self.con.commit()
					self.play()
				elif(mouse[0]>753 and mouse[0]<=923 and mouse[1]>399 and mouse[1]<=570 and event.type == pygame.MOUSEBUTTONDOWN):
					self.search_response = self.youtube.search().list(q=self.song[6]+" by "+self.artist[6],part="id,snippet",maxResults=10).execute()
					stamp=datetime.now()
					stamp=str(stamp)
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into logs(username,at,song,artist) values('"+self.username+"','"+stamp+"','"+self.song[6]+"','"+self.artist[6]+"');")
					self.con.commit()
					self.play()
				elif(mouse[0]>950 and mouse[0]<=1122 and mouse[1]>399 and mouse[1]<=570 and event.type == pygame.MOUSEBUTTONDOWN):
					self.search_response = self.youtube.search().list(q=self.song[7]+" by "+self.artist[7],part="id,snippet",maxResults=10).execute()
					stamp=datetime.now()
					stamp=str(stamp)
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into logs(username,at,song,artist) values('"+self.username+"','"+stamp+"','"+self.song[7]+"','"+self.artist[7]+"');")
					self.con.commit()
					self.play()
				elif(mouse[0]>468 and mouse[0]<580 and mouse[1]>345 and mouse[1]<367 and event.type == pygame.MOUSEBUTTONDOWN):
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into music values('"+self.username+"','"+self.artist[0]+"','"+self.song[0]+"');")
					self.con.commit()
				elif(mouse[0]>668 and mouse[0]<706 and mouse[1]>345 and mouse[1]<367 and event.type == pygame.MOUSEBUTTONDOWN):
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into music values('"+self.username+"','"+self.artist[1]+"','"+self.song[1]+"');")
					self.con.commit()
				elif(mouse[0]>868 and mouse[0]<906 and mouse[1]>345 and mouse[1]<367 and event.type == pygame.MOUSEBUTTONDOWN):
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into music values('"+self.username+"','"+self.artist[2]+"','"+self.song[2]+"');")
					self.con.commit()
				elif(mouse[0]>1068 and mouse[0]<1108 and mouse[1]>345 and mouse[1]<367 and event.type == pygame.MOUSEBUTTONDOWN):
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into music values('"+self.username+"','"+self.artist[3]+"','"+self.song[3]+"');")
					self.con.commit()
				elif(mouse[0]>468 and mouse[0]<580 and mouse[1]>596 and mouse[1]<616 and event.type == pygame.MOUSEBUTTONDOWN):
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into music values('"+self.username+"','"+self.artist[4]+"','"+self.song[4]+"');")
					self.con.commit()
				elif(mouse[0]>668 and mouse[0]<706 and mouse[1]>596 and mouse[1]<616 and event.type == pygame.MOUSEBUTTONDOWN):
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into music values('"+self.username+"','"+self.artist[5]+"','"+self.song[5]+"');")
					self.con.commit()
				elif(mouse[0]>868 and mouse[0]<906 and mouse[1]>596 and mouse[1]<616 and event.type == pygame.MOUSEBUTTONDOWN):
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into music values('"+self.username+"','"+self.artist[6]+"','"+self.song[6]+"');")
					self.con.commit()
				elif(mouse[0]>1068 and mouse[0]<1108 and mouse[1]>596 and mouse[1]<616 and event.type == pygame.MOUSEBUTTONDOWN):
					self.con.close()
					self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
					self.con.query("insert into music values('"+self.username+"','"+self.artist[7]+"','"+self.song[7]+"');")
					self.con.commit()
				
			if(button2.collidepoint(mouse)):
				pygame.draw.rect(self.displ,(255,255,255),button2)
			if(button1.collidepoint(mouse)):
				pygame.draw.rect(self.displ,(255,255,255),button1)
			if(button3.collidepoint(mouse)):
				pygame.draw.rect(self.displ,(255,255,255),button3)
			if(button4.collidepoint(mouse)):
				pygame.draw.rect(self.displ,(255,255,255),button4)
			if(button5.collidepoint(mouse)):
				pygame.draw.rect(self.displ,(255,255,255),button5)
			if(button6.collidepoint(mouse)):
				pygame.draw.rect(self.displ,(255,255,255),button6)
			if(button7.collidepoint(mouse)):
				pygame.draw.rect(self.displ,(255,255,255),button7)
			if(button8.collidepoint(mouse)):
				pygame.draw.rect(self.displ,(255,255,255),button8)
			if(button9.collidepoint(mouse)):
				pygame.draw.rect(self.displ,(255,255,255),button9)
			if(button10.collidepoint(mouse)):
				pygame.draw.rect(self.displ,(255,255,255),button10)
			if(button11.collidepoint(mouse)):
				pygame.draw.rect(self.displ,(255,255,255),button11)
			if(button12.collidepoint(mouse)):
				pygame.draw.rect(self.displ,(255,255,255),button12)	
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render("Popular Artist",True,(0,0,0))
			textre=textsurf.get_rect()
			textre.center=(120,180)
			self.displ.blit(textsurf,textre)
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render("Popular Song",True,(0,0,0))
			textre=textsurf.get_rect()
			textre.center=(120,250)
			self.displ.blit(textsurf,textre)
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render("Most Searched Songs",True,(0,0,0))
			textre=textsurf.get_rect()
			textre.center=(120,310)
			self.displ.blit(textsurf,textre)
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render("Most Searched Album",True,(0,0,0))
			textre=textsurf.get_rect()
			textre.center=(120,370)
			self.displ.blit(textsurf,textre)
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render("Most Searched Artist",True,(0,0,0))
			textre=textsurf.get_rect()
			textre.center=(120,430)
			self.displ.blit(textsurf,textre)
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render("My Songs",True,(0,0,0))
			textre=textsurf.get_rect()
			textre.center=(120,490)
			self.displ.blit(textsurf,textre)
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render("My Artists",True,(0,0,0))
			textre=textsurf.get_rect()
			textre.center=(120,550)
			self.displ.blit(textsurf,textre)
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render("Logout",True,(0,0,0))
			textre=textsurf.get_rect()
			textre.center=(120,610)
			self.displ.blit(textsurf,textre)
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render("Search Song",True,(0,0,0))
			textre=textsurf.get_rect()
			textre.center=(470,45)
			self.displ.blit(textsurf,textre)
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render("Search Artist",True,(0,0,0))
			textre=textsurf.get_rect()
			textre.center=(710,45)
			self.displ.blit(textsurf,textre)
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render("Search Album",True,(0,0,0))
			textre=textsurf.get_rect()
			textre.center=(920,45)
			self.displ.blit(textsurf,textre)
			fontobj=pygame.font.Font('freesansbold.ttf',18)
			textsurf=fontobj.render("My Profile",True,(0,0,0))
			textre=textsurf.get_rect()
			textre.center=(1120,45)
			self.displ.blit(textsurf,textre)	
			self.clock.tick(100)
			pygame.display.update()
		
	def sym(self):
		a=455
		b=325
		self.artist=[]
		self.song=[]
		self.displ.fill((0,0,0))
		pygame.display.update()
		loadx=350
		loady=150
		self.temp=0
		if(self.tag==0):
			self.tag=1
			while(self.temp<8):
				for j in range(1,5):
					url=self.data['tracks']['track'][self.temp+1]['image'][2]['#text']
					filename="im"+str(self.temp+1)+".png"
					try:
						image=requests.get(url)
						with open(filename,'wb') as damm:
							for chunk in image.iter_content():
								damm.write(chunk)
						artist=self.data['tracks']['track'][self.temp+1]['artist']['name']
						self.artist.append(artist)
						song=self.data['tracks']['track'][self.temp+1]['name']
						self.song.append(song)
						out=artist
						var=pygame.image.load(filename)
						self.displ.blit(var,(loadx,loady))
						like=pygame.image.load("like.png")
						self.displ.blit(like,(a,b))
						fontobj=pygame.font.Font('freesansbold.ttf',12)
						textsurf=fontobj.render(out,True,(255,255,255))
						textre=textsurf.get_rect()
						textre.center=(loadx+66,loady+180)
						self.displ.blit(textsurf,textre)
						fontobj=pygame.font.Font('freesansbold.ttf',12)
						textsurf=fontobj.render(song,True,(255,140,0))
						textre=textsurf.get_rect()
						textre.center=(loadx+60,loady+195)
						self.displ.blit(textsurf,textre)
						loadx+=200
						a+=200
						self.temp+=1
						pygame.display.update()
						os.remove(filename)
					except:
						self.temp+=1
				loadx=350
				a=455
				b+=250
				loady+=250
		else:
			while(self.temp<8):
				for j in range(1,5):
					url=self.data['results']['trackmatches']['track'][self.temp+1]['image'][2]['#text']
					filename="im"+str(self.temp+1)+".png"
					try:
						image=requests.get(url)
						with open(filename,'wb') as damm:
							for chunk in image.iter_content():
								damm.write(chunk)
						artist=self.data['results']['trackmatches']['track'][self.temp+1]['artist']
						self.artist.append(artist)
						song=self.data['results']['trackmatches']['track'][self.temp+1]['name']
						self.song.append(song)
						out=artist
						var=pygame.image.load(filename)
						self.displ.blit(var,(loadx,loady))
						like=pygame.image.load("like.png")
						self.displ.blit(like,(a,b))
						fontobj=pygame.font.Font('freesansbold.ttf',12)
						textsurf=fontobj.render(out,True,(255,255,255))
						textre=textsurf.get_rect()
						textre.center=(loadx+66,loady+180)
						self.displ.blit(textsurf,textre)
						fontobj=pygame.font.Font('freesansbold.ttf',12)
						textsurf=fontobj.render(song,True,(255,140,0))
						textre=textsurf.get_rect()
						textre.center=(loadx+60,loady+195)
						self.displ.blit(textsurf,textre)
						loadx+=200
						a+=200
						self.temp+=1
						pygame.display.update()
						os.remove(filename)
					except:
						self.temp+=1
				loadx=350
				a=455
				b+=250
				loady+=250

	def profile(self):
		self.con.close()
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		self.con.query("select * from user where(username='"+self.username+"');")
		r=self.con.store_result()
		r=r.fetch_row()
		x=tk.Tk()
		x.title(self.username)
		x.geometry("{}x{}".format(800,300))
		a=Label(x,text="Name :",font="Helvetical 15")
		a.place(x=10,y=10)
		a=Label(x,text="Year Of Birth :",font="Helvetical 15")
		a.place(x=10,y=40)
		a=Label(x,text="Age :",font="Helvetical 15")
		a.place(x=10,y=70)
		a=Label(x,text="Phone :",font="Helvetical 15")
		a.place(x=10,y=100)
		a=Label(x,text="Country :",font="Helvetical 15")
		a.place(x=10,y=130)
		a=Label(x,text="Email :",font="Helvetical 15")
		a.place(x=10,y=160)
		a=Label(x,text="Username :",font="Helvetical 15")
		a.place(x=10,y=190)
		a=Label(x,text=r[0][0],font="Helvetical 15")
		a.place(x=200,y=10)
		a=Label(x,text=r[0][1],font="Helvetical 15")
		a.place(x=200,y=40)
		a=Label(x,text=r[0][2],font="Helvetical 15")
		a.place(x=200,y=70)
		a=Label(x,text=r[0][3],font="Helvetical 15")
		a.place(x=200,y=100)
		a=Label(x,text=r[0][4],font="Helvetical 15")
		a.place(x=200,y=130)
		a=Label(x,text=r[0][5],font="Helvetical 15")
		a.place(x=200,y=160)
		a=Label(x,text=r[0][6],font="Helvetical 15")
		a.place(x=200,y=190)
		x.mainloop()
	def play(self):
		for i in range(5):
			try:
				x=self.search_response['items'][i]['id']['videoId']
				url="https://www.youtube.com/embed/"+x
				wb.open_new(url)
				print(self.search_response)
				break
			except:
				i+=1
	def song_s(self):
		self.con.close()
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		a=self.wigdet.get()
		url="http://ws.audioscrobbler.com/2.0/?method=track.search&track="+a+"&api_key="+self.api_key+"&format=json"
		try:
			self.data=urllib.request.urlopen(url).read()
			self.data=self.data.decode("utf-8")
			self.data=json.loads(self.data)
			self.sym()
		except:
			print("Query Not Found")
		try:
			self.con.query("insert into search values('"+self.username+"','"+a+"','Song');")
			self.con.commit()
			self.temp1.destroy()
			return
		except:
			self.temp1.destroy()
			return
	def artist_s(self):
		self.con.close()
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		a=self.wigdet.get()
		url="http://ws.audioscrobbler.com/2.0/?method=track.search&track="+a+"&api_key="+self.api_key+"&format=json"
		try:
			self.data=urllib.request.urlopen(url).read()
			self.data=self.data.decode("utf-8")
			self.data=json.loads(self.data)
			self.sym()
		except:
			print("Query Not Found")
		try:
			self.con.query("insert into search values('"+self.username+"','"+a+"','Artist');")
			self.con.commit()
			self.temp1.destroy()
			return
		except:
			self.temp1.destroy()
			return
	def album_s(self):
		self.con.close()
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		a=self.wigdet.get()
		url="http://ws.audioscrobbler.com/2.0/?method=track.search&track="+a+"&api_key="+self.api_key+"&format=json"
		try:	
			self.data=urllib.request.urlopen(url).read()
			self.data=self.data.decode("utf-8")
			self.data=json.loads(self.data)
			self.sym()
		except:
			print("Query Not Found")
		try:
			self.con.query("insert into search values('"+self.username+"','"+a+"','Album');")
			self.con.commit()
			self.temp1.destroy()
			return
		except:
			self.temp1.destroy()
			return
	def my_song(self):
		self.con.close()
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		x=[]
		y=[]
		e=np.arange(5)
		z=None
		try:
			self.con.query("select song,count(song) from music where(username='"+self.username+"') group by (song) order by count(song) desc;")
			data=self.con.store_result()
			z=data.fetch_row()
		except:
			print("ERROR")
		i=z
		print(i)
		count=0
		while(count<5 and i):
			x.append(z[0][0])
			y.append(z[0][1])
			i=data.fetch_row()
			if(i):
				z=i
				count+=1
		try:
			plt.bar(e,y)
			plt.title("My Songs")
			plt.xticks(e,x)
			plt.show()
		except:
			print("No data")
	def my_artist(self):
		self.con.close()
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		x=[]
		y=[]
		e=np.arange(5)
		z=None
		try:
			self.con.query("select artist,count(artist) from music where(username='"+self.username+"') group by (artist) order by count(artist) desc;")
			data=self.con.store_result()
			z=data.fetch_row()
		except:
			print("ERROR")
		i=z
		print(i)
		count=0
		while(count<5 and i):
			x.append(z[0][0])
			y.append(z[0][1])
			i=data.fetch_row()
			if(i):
				z=i
				count+=1
		try:
			plt.bar(e,y)
			plt.title("My Artists")
			plt.xticks(e,x)
			plt.show()
		except:
			print("No data")
	def popular_song(self):
		self.con.close()
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		self.con.close()
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		x=[]
		y=[]
		e=np.arange(5)
		z=None
		try:
			self.con.query("call get_song();")
			data=self.con.store_result()
			z=data.fetch_row()
		except:
			print("ERROR")
		i=z
		print(i)
		count=0
		while(count<5 and i):
			x.append(z[0][0])
			y.append(z[0][1])
			i=data.fetch_row()
			if(i):
				z=i
				count+=1
		try:
			plt.bar(e,y)
			plt.title("Popular Songs")
			plt.xticks(e,x)
			plt.show()
		except:
			print("No Data")
	def popular_artist(self):
		self.con.close()
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		x=[]
		y=[]
		e=np.arange(5)
		z=None
		try:
			self.con.query("call get_artist();")
			data=self.con.store_result()
			z=data.fetch_row()
		except:
			print("ERROR")
		i=z
		print(i)
		count=0
		while(count<5 and i):
			x.append(z[0][0])
			y.append(z[0][1])
			i=data.fetch_row()
			if(i):
				z=i
				count+=1
		try:
			plt.bar(e,y)
			plt.title("Popular Artists")
			plt.xticks(e,x)
			plt.show()
		except:
			print("No Data")
	def searched_song(self):
		self.con.close()
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		x=[]
		y=[]
		e=np.arange(5)
		z=None
		try:
			self.con.query("select query,count(query) from search where(search_by='song') group by(query) order by count(query) desc;")
			data=self.con.store_result()
			z=data.fetch_row()
		except:
			print("ERROR")
		i=z
		print(i)
		count=0
		while(count<5 and i):
			x.append(z[0][0])
			y.append(z[0][1])
			i=data.fetch_row()
			if(i):
				z=i
				count+=1
		try:
			plt.bar(e,y)
			plt.title("Most Searched Songs")
			plt.xticks(e,x)
			plt.show()
		except:
			print("No Data")
	def searched_album(self):
		self.con.close()
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		x=[]
		y=[]
		e=np.arange(5)
		z=None
		try:
			self.con.query("select query,count(query) from search where(search_by='album') group by(query) order by count(query) desc;")
			data=self.con.store_result()
			z=data.fetch_row()
		except:
			print("ERROR")
		i=z
		print(i)
		count=0
		while(count<5 and i):
			x.append(z[0][0])
			y.append(z[0][1])
			i=data.fetch_row()
			if(i):
				z=i
				count+=1
		try:
			plt.bar(e,y)
			plt.title("Most Searched albums")
			plt.xticks(e,x)
			plt.show()
		except:
			print("No Data")
	def searched_artist(self):
		self.con.close()
		self.con=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		x=[]
		y=[]
		e=np.arange(5)
		z=None
		try:
			self.con.query("select query,count(query) from search where(search_by='artist') group by(query) order by count(query) desc;")
			data=self.con.store_result()
			z=data.fetch_row()
		except:
			print("ERROR")
		i=z
		count=0
		while(count<5 and i):
			x.append(z[0][0])
			y.append(z[0][1])
			i=data.fetch_row()
			if(i):
				z=i
				count+=1
		try:
			plt.bar(e,y)
			plt.title("Most Searched Artists")
			plt.xticks(e,x)
			plt.show()
		except:
			print("No Data")
		
		


	
		
