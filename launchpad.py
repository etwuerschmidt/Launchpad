import mido
import time

output = mido.open_output('Launchpad S 1')

#F
notes = [0,1,2,3,4,5,16,32,48,49,50,51,64,80,96,112]

for i in notes:
	output.send(mido.Message('note_on', note=i, velocity=15))


time.sleep(5)

for i in notes:
	output.send(mido.Message('note_off', note=i))

output.close()
exit()