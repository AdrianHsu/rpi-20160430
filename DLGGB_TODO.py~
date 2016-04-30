import RPi.GPIO as GPIO
import pygame
import time

#prepare warning sound
pygame.init()
#pygame.mixer.music.load("C4.wav")		# load bobogey_sound

# set 7_segment on/off
on = 1
off = 0

#set GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#\\TODO1\\
GPIO.setup(10,GPIO.OUT)													#GGB warning light
#\\To set GPIO pin 10 (LED) as an output, use function GPIO.setup(pin,GPIO.IN or GPIO.OUT) 
GPIO.setup(3,GPIO.OUT)			#relay
GPIO.setup(5,GPIO.OUT)			#relay
GPIO.setup(35,GPIO.IN)  			#GGB line
GPIO.setup(23,GPIO.IN)  			#GGB start
#\\TODO2\\
GPIO.setup(24,GPIO.IN)										#GGB finish
#\\Set GPIO pin 24 (finish) as an input, use function GPIO.setup(pin,GPIO.IN or GPIO.OUT) 
GPIO.output(10,GPIO.HIGH)

# set GPIO to 7-segment pin
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
	'2': ['a', 'b', 'd', 'e', 'g'],#\\TODO3\\	No. of LEDs  on 7-segment for showing number 2 
	'3': ['a', 'b', 'c', 'd', 'g'],
	'4': ['b', 'c', 'f', 'g'],
	'5': ['a', 'c', 'd', 'f', 'g'],
	'6': ['a', 'c', 'd', 'e', 'f', 'g'],
	'7': ['a', 'b', 'c'],
	'8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],#\\TODO4\\ No. of LEDs  on 7-segment for showing number 8
	'9': ['a', 'b', 'c', 'd', 'f', 'g'],
	'e': ['a', 'd', 'e', 'f', 'g']}
tenths = {'a': 33, 'b': 40, 'c': 32, 'd': 38, 'e': 36, 'f': 31, 'g': 29}
ten = { ' ': [],
	'0': ['a', 'b', 'c', 'd', 'e', 'f'],
	'1': ['b', 'c'],
	'2': ['a', 'b', 'd', 'e', 'g'],#\\TODO3\\ No. of LEDs  on 7-segment for showing number 2
	'3': ['a', 'b', 'c', 'd', 'g'],
	'4': ['b', 'c', 'f', 'g'],
	'5': ['a', 'c', 'd', 'f', 'g'],
	'6': ['a', 'c', 'd', 'e', 'f', 'g'],
	'7': ['a', 'b', 'c'],
	'8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],#\\TODO4\\ No. of LEDs  on 7-segment for showing number 8
	'9': ['a', 'b', 'c', 'd', 'f', 'g'],
	'e': ['a', 'd', 'e', 'f', 'g']}

try:
	while True:
		if GPIO.input(23):				#start when 3.3V leave pin23
			n = 2                       #n means digit in ones
			t = 2                      #t means digit in tens
			m = 0                       #m is just used for improving efficiency
			while True:
				s = str(n)
				u = str(t)	
				digittenths = ten[u]
				for tenth in digittenths:
				        GPIO.output(tenths[tenth], on)
				digitSegments = num[s]
				for segment in digitSegments:
						GPIO.output(segments[segment], on)#\\TODO8\\
					#\\Let 7-segment show the number
					#\\Use GPIO.input(pin) or GPIO.output(pin, GPIO.HIGH or GPIO.LOW) function
					#\\and set its pin as "segments[segment]"
				
				time.sleep(0.1)
				if (m%10) == 0 and (not m == 0):
					for segment in digitSegments:
						GPIO.output(tenths[tenth], off)#\\TODO9\\
						#\\Refresh the 7-segment, turn 7-segment off
						#\\Use GPIO.input(pin) or GPIO.output(pin, GPIO.HIGH or GPIO.LOW) function
						#\\and set its pin as "segments[segment]"
	
					GPIO.output(10, GPIO.HIGH)
					n=(n-1)%10#\\TODO1
					#\\Make "n" countdown from 9 to 0 repeatedl
					if n == 9:
						for tenth in digittenths:
							GPIO.output(tenths[tenth],off)
						t = (t - 1)%10 
					if GPIO.input(24) or GPIO.input(35) or (t==0 and n==0):
					#\\TODO7\\
				#\\Wait for GGB reach the end or GGB line is touched or time up
				#\\Use "if" taught just before to determine three condition:
				#\\1. GGB reach the end, so pin24 return true
				#\\2. GGB line is touched, so pin35 return true
				#\\3. Time up when counter reach 00
						break
				m += 1
			if not GPIO.input(24):
				GPIO.output(10,GPIO.LOW)#\\TODO6\\	
				#\\turn on LED(pin10) 
				#\\Use GPIO.input(pin) or GPIO.output(pin, GPIO.HIGH or GPIO.LOW) function
				GPIO.output(3,GPIO.LOW)
				GPIO.output(5,GPIO.LOW)
				for segment in num['8']:
					GPIO.output(segments[segment], off)
				for tenth in ten['8']:
					GPIO.output(tenths[tenth], off)
				for segment in num['0']:
					GPIO.output(segments[segment],on)
				for tenth in ten['0']:
					GPIO.output(tenths[tenth], on)
				# pygame.mixer.music.play()
				time.sleep(2)
				# time.sleep(200) 						# for test only

			if GPIO.input(24):
				for segment in num['8']:
					GPIO.output(segments[segment], off)
				for tenth in ten['8']:
					GPIO.output(tenths[tenth], off)
				for segment in num['e']:
					GPIO.output(segments[segment],on)
				for tenth in ten['e']:
					GPIO.output(tenths[tenth], on)
		        time.sleep(2)#\\TODO5\\	
					#\\wait for 2 sec 

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


