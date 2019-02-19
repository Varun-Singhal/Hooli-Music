## Hooli Music Application

The app is linux based software which uses various APIs to make user's music listening experience pleasant. The user gets to search categories like songs, artists, genre.
The app also provides analytics like most likes and listened music based on global user logs. 

### APIs Configurations

Following is the list of third-party APIs for functioning of the software:

	* LastFM : Music & Artist Search
	* Youtube : Music Videos
	* Mailgun : Email API for sending confirmation & password recovery support

### Technology Stack

The application is built using the following tech stack :
	
	* Tkinter (Python UI Framework)
	* Pygame (Python framework for making basic games - used for better graphics and music integration on start-up)
	* MySQLdb / MongoDB (The application was initially built MongoDB)

	The database is changed to MySQLdb from MongoDB to explore the possiblities with using various database management systems.

### Running the application

If you wish to run the application, you need to configure the database as per written in code base.
The API keys used were enabled for trail version. You need to re-issue the API keys for smooth running.

```
$python hooli.py 
```

### Screenshots

![Start](https://github.com/Varun-Singhal/Hooli-Music/blob/master/screenshots/1.png)

![Home](https://github.com/Varun-Singhal/Hooli-Music/blob/master/screenshots/2.png)

![Sign-Up](https://github.com/Varun-Singhal/Hooli-Music/blob/master/screenshots/3.png)


##### The application is built to understand third party API integration into python code base.