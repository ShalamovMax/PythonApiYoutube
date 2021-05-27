
from googleapiclient.discovery import build
from pymongo import MongoClient

DEVELOPER_KEY = 'Youtube_developer_API' #add your API Key
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

#starting a connection to MongoDB database server
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["DB_search"]

#Creating  collections
col_video = mydb["Video"]
col_channel = mydb["Channel"]
col_playlist = mydb["Playlist"]


def YoutubeAPI(query, max_results):
    
    
              youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)
            
              search_response = youtube.search().list(
                    q=query,
                    part='id,snippet',
                    maxResults=max_results
              ).execute()
              del youtube
                
              results = search_response.get('items', [])
              del search_response
                  
              videos = []
              channels = []
              playlists = []
                
              for search_result in results:
                          
                        if search_result['id']['kind'] == 'youtube#video':
                          videos.append('%s (%s)' % (search_result['snippet']['title'],
                                                     search_result['id']['videoId']))
                          
                        elif search_result['id']['kind'] == 'youtube#channel':
                          channels.append('%s (%s)' % (search_result['snippet']['title'],
                                                       search_result['id']['channelId']))
                        
                        elif search_result['id']['kind'] == 'youtube#playlist':
                          playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                                        search_result['id']['playlistId']))
                
              del results  
              print ('Videos:\n', '\n'.join(videos), '\n')
              print ('Channels:\n', '\n'.join(channels), '\n')
              print ('Playlists:\n', '\n'.join(playlists), '\n')
              
              # saving extracted data to MongoDB database
              list_ = []
              for s in videos:
                  
                     text = s.split('(')
                     link = text [-1][:-1]
                     text_find = s.find(link)-1
                     full_link =  "https://www.youtube.com/watch?v=" + link
                     print('Video Title:', s[:text_find] ,'\n')
                     print('Video Link:', full_link ,'\n')
                     mydict = { "Video Title": s[:text_find], "Video Link": full_link }
                     list_.append(mydict)
                     
              col_video.insert_many(list_)
              del videos
            
              liste_ = []  
              for s in channels:  
                  
                   text = s.split('(')
                   link = text [-1][:-1]
                   text_find = s.find(link)-1
                   full_link =  "https://www.youtube.com/channel/" + link
                   print('Channel Title:', s[:text_find] ,'\n')
                   print('Channel Link:', full_link ,'\n')
                     
                   mydict = { "Channel Title": s[:text_find], "Channel Link": full_link }
                   liste_.append(mydict)
                   
              col_channel.insert_many(liste_)  
              del channels   
              
              liste_ = []  
              for s in playlists:  
                  
                   text = s.split('(')
                   link = text [-1][:-1]
                   text_find = s.find(link)-1
                   full_link =  "https://www.youtube.com/watch?v=WW2DKBGCvEs&list=" + link
                   print('Playlist Title:', s[:text_find] ,'\n')
                   print('Playlist Link:', full_link ,'\n')
                     
                   mydict = { "Playlist Title": s[:text_find], "Playlist Link": full_link }
                   liste_.append(mydict)
                   
              col_playlist.insert_many(liste_)  
              del playlists
              
              print("MongoDB Data saved")



if __name__ == '__main__':

  max_results = 50
  query = "Youtube"
  
  YoutubeAPI(query, max_results)
  
