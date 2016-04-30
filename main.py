import pafy
#!/usr/bin/python3
import subprocess
# import avconv
import alsaaudio

print("hello")

url = "ctlnamzyfLo"
video = pafy.new(url)
# print(video.title)

stream = video.getbestaudio()
print(stream.url)

par1 = ["curl", stream.url]
tmp = subprocess.Popen(par1, 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE)

pcms = alsaaudio.pcms();
mydevice = pcms[1];

print(mydevice)

play = alsaaudio.PCM(device=mydevice)
play.setformat(alsaaudio.PCM_FORMAT_S16_LE)
play.setrate(44100)
play.setchannels(2)
play.setperiodsize(44100 * 2 * 2 // 10)

par = ["avconv", "-i", "pipe:", "-f","s16le" ,"-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", "-"]
data = subprocess.Popen(par, 
        stdin=tmp.stdout, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE)

interval = data.stdout.read(44100 * 2 * 2 // 10)

while(interval != b''):
    play.write(interval)
    interval = data.stdout.read(44100 * 2 * 2 // 10)
print("end")
