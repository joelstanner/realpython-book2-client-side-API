# basic web service example


# import the client libraries
import gdata.youtube
import gdata.youtube.service

# YouTubeService() used to generate the object so that we can communicate with
# the YouTube API
youtube_service = gdata.youtube.service.YouTubeService()

# prompt the user to enter the youtube ID
playlist = raw_input("Please enter the user id: ")

# setup the actual API call
url = "http://gdata.youtube.com/feeds/api/users/"
playlist_url = url + playlist + "/playlists"

# retrieve Youtube playlist
video_feed = youtube_service.GetYouTubePlaylistVideoFeed(playlist_url)

print video_feed.entry

#print"\nPlaylists for " + str.format(playlist) + ":\n"
#
## display each playlist to the screen
#for p in video_feed.entry:
#    print p.title.text
