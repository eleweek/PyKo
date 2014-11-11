from bs4 import BeautifulSoup
import requests
import pafy
from prettytable import PrettyTable
from pytube import YouTube
from pprint import pprint
import os, sys


# Written by Daniel Koifman(A.K.A HeliosHype) and Alex Putilin
# You are allowed to freely use, edit, modify and distribute this script, just make sure to give proper credit :)



# TODO: how to handle playlists?





def downloadSong(url):
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    yt = YouTube()
    yt.url = url
    os.system('cls') # os.system('clear') for linux.
    print "Download URL fetched successfully!\n"
    print "1. Get the list of available streams"
    print "2. Get the highest resolution available"
    print "3. Start download the video\n"

    while True:
        print "Select an action: "
        action = raw_input("> ")

        if action == str(1):
            print "Availabile streams for the URL: \n"
            pprint(yt.videos)
            print "\n"

        elif action == str(2):
            print "Highest resolution is:"
            pprint(yt.filter('mp4')[-1])
            print "\n"

        elif action == str(3):
            print "Starting download: \n"
            best.download(quiet=False)
            print "Download finished!, the file has been downloaded to the same folder where the script is located."
            sys.exit(0)

        else:
            print "Not a valid option!\n"




songName = raw_input("Enter the name of the song: ")
artistName = raw_input("Enter the name of the artist: ")

# Making the song name and the artist name appear in a queryable format
replacedSongName = songName.replace(" ", "+")
replacedArtistName = artistName.replace(" ", "+")
song_titles = []
i = 1
z = 1


url = "https://www.youtube.com/results?search_query=%s+%s" % (replacedSongName, replacedArtistName)
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text)
for SongTitle in soup.findAll('a', {'class': 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink     spf-link '}):
    song_titles.append(SongTitle.string)
    i += 1


x = PrettyTable(["Video name"])
x.align["Video name"] = "l"
x.padding_width = 10
for title in song_titles:
    x.add_row([str(z) + "." + title])
    z += 1
print x


video_number = raw_input("Enter the number of the video to download: ")


for title in soup.findAll('a', {'title': song_titles[int(video_number)-1]}):
    link_to_download = "http://www.youtube.com" + title.get("href")


downloadSong(link_to_download)
