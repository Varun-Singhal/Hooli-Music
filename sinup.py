import tkinter as tk
from tkinter import *
import time 
import MySQLdb as sql
import random
import requests
from home import *
from datetime import datetime
class sinup:
	def __init__(self):
		self.master=tk.Tk()
		self.master.title("Sign-Up Page")
		self.master.geometry('{}x{}'.format(1000,600))
		self.conn=sql.connect(host="localhost",user="root",passwd="hwp@7299",db='hooli')
		self.watch1=0
		self.watch2=0
		self.createwidgets()
		self.master.mainloop()
	def validate(self,tp):
		if tp=='em':
			self.conn.query("select username from password where(email='"+self.temp+"');")
			loop=self.conn.store_result()
			loop=loop.fetch_row()
			for i in loop:
				if(i):
					return(True)
		else:
			self.conn.query("select username from password where(username='"+self.temp+"');")
			loop=self.conn.store_result()
			loop=loop.fetch_row()
			for i in loop:
				if(i):
					return(True)


	def createwidgets(self):
		self.pic1=PhotoImage(file="login4.png")
		self.picture=Label(self.master,image=self.pic1)
		self.picture.pack(side=RIGHT)
		self.title1=Label(self.master,text=" Hooli Sign-Up",font=' Helvetica 50' ,justify=LEFT )
		self.title1.pack(anchor=NW)
		self.name=Label(self.master,text="Name", font='10')
		self.name.place(x=20,y=100 )
		self.data1=Entry(self.master,width=20)
		self.data1.place(x=150 ,y=100)
		self.email=Label(self.master,font='10',text="Email-ID")
		self.email.place(x=20,y=150)
		self.button1=Button(self.master,text="Verify" , command=self.verifyemail)
		self.button1.place(x=350,y=150)
		self.data2=Entry(self.master,width=20)
		self.data2.place(x=150,y=150)
		self.year=Label(self.master,font='10',text="Birth Year")
		self.year.place(x=20,y=200)
		self.data3=Entry(self.master,width=20)
		self.data3.place(x=150,y=200)
		self.phone=Label(self.master,font='10',text="Phone")
		self.phone.place(x=20,y=250)
		self.data4=Entry(self.master,width=20)
		self.data4.place(x=150,y=250)
		self.country=Label(self.master, font='10',text="Country")
		self.country.place(x=20,y=300)
		self.data5=Entry(self.master,width=20)
		self.data5.place(x=150,y=300)
		self.username=Label(self.master,text="Username", font='10')
		self.username.place(x=20,y=350 )
		self.button2=Button(self.master,text="Verify" , command=self.verifyusername)
		self.button2.place(x=350,y=350)
		self.passw=Label(self.master,font='10',text="Password")
		self.passw.place(x=20,y=400)
		self.data6=Entry(self.master,width=20)
		self.data6.place(x=150,y=350)
		self.data7=Entry(self.master,width=20,show='*')
		self.data7.place(x=150,y=400)
		cancel=tk.Button(self.master, text="Cancel", command=self.master.destroy)
		cancel.place(x=70,y=450)
		submit=tk.Button(self.master, text='Submit', command=self.make)
		submit.place(x=180,y=450)	
	def verifyemail(self):
		self.temp=self.data2.get()
		if('@' not in self.temp):
			temp=tk.Tk()
			temp.geometry("{}x{}".format(200,50))
			temp.title("Invalid Email")
			x=Label(temp,text="Invalid Email ID", font=' Helvetical 10')
			x.place(x=2,y=2)
			temp.mainloop()
		elif(self.validate('em')):
			temp=tk.Tk()
			temp.geometry("{}x{}".format(200,50))
			temp.title("Invalid Email")
			x=Label(temp,text="Email already registered", font=' Helvetical 10')
			x.place(x=2,y=2)
			temp.mainloop()
		else:
			self.watch1=1
			self.email=self.data2.get()
			self.data2.destroy()
			self.data2=Label(self.master,text="ACCEPTED",font='Arial 10')
			self.data2.place(x=150,y=150)
			self.button1.destroy()
			
	def verifyusername(self):
		self.temp=self.data6.get()
		if(self.validate('us')):
			temp=tk.Tk()
			temp.geometry("{}x{}".format(200,50))
			temp.title("Invalid username")
			x=Label(temp,text="Username already taken", font=' Helvetical 10')
			x.place(x=2,y=2)
			temp.mainloop()
		else:
			self.watch2=1
			self.username=self.data6.get()
			self.data6.destroy()
			self.data6=Label(self.master,text="ACCEPTED",font='Arial 10')
			self.data6.place(x=150,y=350)
			self.button2.destroy()

	
	def make(self):
		if(self.watch2==1 and self.watch1==1):
			self.name=str(self.data1.get())
			self.year=str(self.data3.get())
			self.phone=str(self.data4.get())
			self.country=str(self.data5.get())
			self.passw=str(self.data7.get())
			if(self.name and self.email and self.year and self.phone and self.country and self.username and self.passw):
				self.age=str(datetime.now().year-int(self.year))
				self.conn.query("insert into password values ('"+self.username+"','"+self.passw+"','"+self.email+"');")
				self.conn.commit()
				self.conn.query("insert into user values ('"+self.name+"',"+self.year+","+self.age+","+self.phone+",'"+self.country+"','"+self.email+"','"+self.username+"');")
				self.conn.commit()
				wow=ui(self.username,self.conn)
				self.master.destroy()
			else:
				temp=tk.Tk()
				temp.geometry("{}x{}".format(200,50))
				temp.title("Missing Data")
				x=Label(temp,text="Provide all the data", font=' Helvetical 10')
				x.place(x=2,y=2)
				temp.mainloop()
		elif(self.watch1==0):
			temp=tk.Tk()
			temp.geometry("{}x{}".format(200,50))
			temp.title("Not Verified")
			x=Label(temp,text="Email not verified", font=' Helvetical 10')
			x.place(x=2,y=2)
			temp.mainloop()
		else:
			temp=tk.Tk()
			temp.geometry("{}x{}".format(200,50))
			temp.title("Not verified")
			x=Label(temp,text="Username not verified", font=' Helvetical 10')
			x.place(x=2,y=2)
			temp.mainloop()
		