#!/usr/bin/python3
import pafy
import subprocess
# import avconv
# import pyalsaaudio

print("hello")
url = "https://www.youtube.com/watch?v=PaEnaoydUUo"
video = pafy.new(url)
print(video.title)
stream = video.getbestaudio("m4a", "true")
print(stream.url)
par1 = ["curl", stream.url]
tmp = subprocess.Popen(par1, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
par = ["avconv", "-i", "pipe:", "-f","s16le" ,"-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", "-"]
subprocess.Popen(par, stdin=tmp.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

