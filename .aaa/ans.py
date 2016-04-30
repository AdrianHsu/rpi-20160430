import RPi.GPIO as GPIO
import pygame
import time

#prepare warning sound
pygame.init()
pygame.mixer.music.load("sound.wav")
#pygame.mixer.music.load("bobogey.wav")

# set 7_segment on/off
on = 1
off = 0

#set GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(35,GPIO.IN)
GPIO.output(10,GPIO.HIGH)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)


segments = [29, 31, 32, 33, 36, 38, 40]
tenths = [16, 18, 22, 15, 13, 11, 7]

for segment in segments:
	GPIO.setup(segment, GPIO.OUT)
	GPIO.output(segment, off)
for tenth in tenths:
	GPIO.setup(tenth, GPIO.OUT)
	GPIO.output(tenth,off)


segments = {'a': 22, 'b': 15, 'c': 7, 'd': 11, 'e': 13, 'f': 18, 'g': 16}
num = {	' ': [],
	'0': ['a', 'b', 'c', 'd', 'e', 'f'],
	'1': ['b', 'c'],
	'2': ['a', 'b', 'd', 'e', 'g'],
	'3': ['a', 'b', 'c', 'd', 'g'],
	'4': ['b', 'c', 'f', 'g'],
	'5': ['a', 'c', 'd', 'f', 'g'],
	'6': ['a', 'c', 'd', 'e', 'f', 'g'],
	'7': ['a', 'b', 'c'],
	'8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
	'9': ['a', 'b', 'c', 'd', 'f', 'g'],
	'e': ['a', 'd', 'e', 'f', 'g']}
tenths = {'a': 33, 'b': 40, 'c': 32, 'd': 38, 'e': 36, 'f': 31, 'g': 29}
ten = { ' ': [],
	'0': ['a', 'b', 'c', 'd', 'e', 'f'],
	'1': ['b', 'c'],
	'2': ['a', 'b', 'd', 'e', 'g'],
	'3': ['a', 'b', 'c', 'd', 'g'],
	'4': ['b', 'c', 'f', 'g'],
	'5': ['a', 'c', 'd', 'f', 'g'],
	'6': ['a', 'c', 'd', 'e', 'f', 'g'],
	'7': ['a', 'b', 'c'],
	'8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
	'9': ['a', 'b', 'c', 'd', 'f', 'g'],
	'e': ['a', 'd', 'e', 'f', 'g']}
try:
	while True:
		if GPIO.input(23):
			n = 2
			t = 2
			m = 0
			while True:
				s = str(n)
				u = str(t)	
				digittenths = ten[u]
				for tenth in digittenths:
				        GPIO.output(tenths[tenth], on)
				digitSegments = num[s]
				for segment in digitSegments:
					GPIO.output(segments[segment], on)
				
				time.sleep(0.1)
				if (m%10) == 0 and (not m == 0):
					for segment in digitSegments:
						GPIO.output(segments[segment], off)
	
					GPIO.output(10, GPIO.HIGH)
					n = (n-1)%10
	                		if n == 9:
						for tenth in digittenths:
							GPIO.output(tenths[tenth],off)
						t = (t - 1)%10 
				if GPIO.input(35) or (n==0 and t==0) or GPIO.input(24):
						break
				m += 1
			if not GPIO.input(24):
				GPIO.output(10,GPIO.LOW)
				GPIO.output(3,GPIO.LOW)
				GPIO.output(5,GPIO.LOW)
				for segment in num['8']:
					GPIO.output(segments[segment], off)
				for tenth in ten['8']:
					GPIO.output(tenths[tenth], off)
				for segment in num['0']:
					GPIO.output(segments[segment], on)
				for tenth in ten['0']:
					GPIO.output(tenths[tenth], on)
				pygame.mixer.music.play()
				time.sleep(2)
				# time.sleep(200) 						# for test only

			if GPIO.input(24):
				for segment in num['8']:
					GPIO.output(segments[segment], off)
				for tenth in ten['8']:
					GPIO.output(tenths[tenth], off)
				for segment in num['e']:
					GPIO.output(segments[segment], on)
				for tenth in ten['e']:
					GPIO.output(tenths[tenth], on)
		        	time.sleep(2)

#for reset
			GPIO.output(10,GPIO.HIGH)
			GPIO.output(3,GPIO.HIGH)
			GPIO.output(5,GPIO.HIGH)
			for segment in num['8']:
				GPIO.output(segments[segment], off)
			for tenth in ten['8']:
				GPIO.output(tenths[tenth], off)
except KeyboardInterrupt:
	GPIO.cleanup()


