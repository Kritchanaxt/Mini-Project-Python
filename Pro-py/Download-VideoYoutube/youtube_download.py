
import yt_dlp

link = "https://youtu.be/O3AFM-MSASM?si=bdPGfbJh-xL3F9Jh"
ydl_opts = {
    'format': 'best',  
    'outtmpl': 'downloaded_video3.%(ext)s', 
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("Success Download !")


