import tkinter as tk
from tkinter import *
import time 
import MySQLdb as sql
import home
class login:
	def __init__(self):
		self.master=tk.Tk()
		self.master.title("Login Page")
		self.master.geometry('{}x{}'.format(850,560))
		self.username=""
		self.password=""
		self.createwidgets()
		self.conn=sql.connect(host="localhost",user="root",passwd="hwp@7299",db="hooli")
		self.master.mainloop()

	def createwidgets(self):
		self.pic1=PhotoImage(file="login1.png")
		self.picture=Label(self.master,image=self.pic1)
		self.picture.pack(side=RIGHT)
		self.title1=Label(self.master,text=" Hooli Login",font=' Helvetica 50' ,justify=LEFT )
		self.title1.pack(anchor=NW)
		self.name=Label(self.master,text="Username", font='10')
		self.name.place(x=20,y=100 )
		self.data1=Entry(self.master,width=20)
		self.data1.place(x=150 ,y=100)
		self.passw=Label(self.master,font='10',text="Password")
		self.passw.place(x=20,y=200)
		forgot=tk.Button(self.master,text="Forgot Password", command=self.forgot)
		forgot.place(x=160,y=220)
		self.data2=Entry(self.master,width=20,show='*')
		self.data2.place(x=150,y=200)
		cancel=tk.Button(self.master, text="Cancel", command=self.master.destroy)
		cancel.place(x=70,y=300)
		submit=tk.Button(self.master, text='Submit', command=self.verify)
		submit.place(x=180,y=300)	
	def verify(self):
		self.name=self.data1.get()
		self.passw=self.data2.get()
		self.conn.query("select	username,pass from password where( username='"+self.name+"');")
		x=self.conn.store_result()
		x=x.fetch_row()
		if( not x):
				error=Label(self.master,text="Invalid Password or Username, Retry",font='Arial 15')
				error.place(x=45,y=350)
					
		else:
			if(x[0][0]== self.name and x[0][1]==self.passw):
				self.master.destroy()
				wow=home.ui(self.name,self.conn)
			else:
				error=Label(self.master,text="Invalid Password or Username, Retry",font='Arial 15')
				error.place(x=45,y=350)
				
					
		
				
	def forgot(self):
		self.temp=tk.Tk()
		self.temp.title("Reset Password")
		self.temp.geometry("{}x{}".format(450,100))
		lab=Label(self.temp,text="Enter your email",font="Helvetical 10")
		self.dat=Entry(self.temp,width=25)
		b=Button(self.temp,text="Submit",command=self.verifyemail)
		lab.place(x=2,y=10)
		self.dat.place(x=150,y=10)
		b.place(x=50,y=50)
	def verifyemail(self):
		tempdata=self.dat.get()
		self.conn.query("select username,pass from password where(email='"+tempdata+"');")
		self.back=self.conn.store_result()
		self.back=self.back.fetch_row()
		if(self.back):
				i=self.back[0]
				self.temp.destroy()
				self.temp=tk.Tk()
				self.temp.title("Reset Password")
				self.temp.geometry("{}x{}".format(450,100))
				self.lab=Label(self.temp,text="UserName and Password mailed to your Email-id")
				self.lab.place(x=2,y=10)
				import requests
				requests.post("https://api.mailgun.net/v3/sandbox850beddfa2f44c31a5f9cdcea273bb00.mailgun.org/messages",
					auth=("api", "key-1542acb80ace8ba1990b5438a5ed1c6d"),
					data={"from": "Mailgun Sandbox <postmaster@sandbox850beddfa2f44c31a5f9cdcea273bb00.mailgun.org>",
					"to": "singhal.varun72@gmail.com","subject": "Password Information",
					"text": "Dear Customer , Your Username:"+str(i[0])+"\nand Password:"+str(i[1])})
		else:
				self.temp.destroy()
				self.temp=tk.Tk()
				self.temp.title("Reset Password")
				self.temp.geometry("{}x{}".format(450,100))
				self.b=Button(self.temp,text="Close",command=self.temp.destroy)
				self.lab=Label(self.temp,text="Invalid Email, Please Sign-UP")
				self.lab.place(x=2,y=10)
				self.b.place(x=5,y=30)
				self.temp.mainloop()