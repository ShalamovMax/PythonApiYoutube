# PythonApiYoutube
Get All Youtube Playlist Videos
Retrieving details about youtube videos, channels, playlists then save all these details to the MongoDB database

# Getting started
##1- create a google account on gmail

##2- creat a project in the https://console.developers.google.com/apis/dashboard

##3 search for 'YouTube Data API' then click on 'Enable API' option, you should see 'ON' on the 'YouTube Data API v3'. 

##4 from this screen copy your 'Youtube API Key'

##5 open a command window or from your terminal you can install Google API client:
\>\> pip install --upgrade google-api-python-client

#  MongoDB server installation:
##1 go to MongoDB web site and download MongoDB server: https://www.mongodb.com/what-is-mongodb

##2 install MongoDB python driver from your commande window: 
\>\> pip install pymongo 

# Runing the code:
##1 go to Anaconda web site and download Anaconda Installer: https://www.anaconda.com/distribution/#download-section

##2 Then download and extract the source code files 'Youtube-API'

##3 Launch Spyder

##4 Launch MongoDB server

##5 Paste the source code and add your 'Youtube API Key'

##6 Write your query and run the code

# Extract all playlist\and 3 last
```
db.playlists.find().pretty()
```
```
db.playlists.find().limit(3)
```
