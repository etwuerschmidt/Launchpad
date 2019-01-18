import mido
import time

output = mido.open_output('Launchpad S 1')

#F
notes = [0,1,2,3,4,5,16,32,48,49,50,51,64,80,96,112]

#Pads on
for i in notes:
	output.send(mido.Message('note_on', note=i, velocity=15))

time.sleep(2)

#Pads off
for i in notes:
	output.send(mido.Message('note_off', note=i))

pad = 0
pad2 = 5
incr = 1
velocity = 15

#Movement
while (pad > -1 and pad2 > -1):
	output.send(mido.Message('note_on', note=pad, velocity=velocity))
	output.send(mido.Message('note_on', note=pad2, velocity=velocity))
	time.sleep(0.05)
	output.send(mido.Message('note_off', note=pad, velocity=velocity))
	output.send(mido.Message('note_off', note=pad2, velocity=velocity))
	if (pad == 7 or pad2 == 7):
		incr = 16
		velocity = 60
	elif pad == 119 or pad2 == 119:
		incr = -1
		velocity = 62
	elif pad == 112 or pad2 == 112:
		incr = -16
		velocity = 47
	pad += incr
	pad2 += incr

output.close()
exit()