import time
import mido


class PyLaunch():

	def __init__(self):
		self.char_mapping = {'A': [3, 4, 5, 
									18, 22, 
									34, 38, 
									50, 54,
									66, 67, 68, 69, 70,
									82, 86,
									98, 102,
									114, 118],
		'B': [2, 3, 4, 5,
				18, 22,
				34, 38,
				50, 51, 52, 53,
				66, 70,
				82, 86,
				98, 102,
				114, 115, 116, 117],
		'C': [3, 4, 5,
				18, 22,
				34,
				50,
				66,
				82,
				98, 102,
				115, 116, 117],
		'D': [2, 3, 4, 5,
				18, 22,
				34, 38,
				50, 54,
				66, 70,
				82, 86,
				98, 102,
				114, 115, 116, 117],
		'E': [2, 3, 4, 5, 6,
				18,
				34,
				50, 51, 52, 53,
				66,
				82,
				98,
				114, 115, 116, 117, 118],
		'F': [2, 3, 4, 5, 6,
				18,
				34,
				50, 51, 52, 53,
				66, 
				82,
				98,
				114],
		'G': [3, 4, 5,
				18, 22,
				34, 
				50, 
				66,
				82, 85, 86,
				98, 102,
				115, 116, 117],
		'H': [2, 6,
				18, 22,
				34, 38,
				50, 51, 52, 53, 54,
				66, 70,
				82, 86,
				98, 102,
				114, 118],
		'I': [2, 3, 4, 5, 6,
				20,
				36,
				52,
				68,
				84,
				100,
				114, 115, 116, 117, 118],
		'J': [],
		'K': [],
		'L': [],
		'M': [],
		'N': [2, 6,
				18, 22,
				34, 35, 38,
				50, 52, 54,
				66, 69, 70,
				82, 86,
				98, 102,
				114, 118],
		'O': [],
		'P': [],
		'Q': [],
		'R': [],
		'S': [3, 4, 5, 6,
				18,
				34,
				51, 52, 53,
				70,
				86,
				102,
				114, 115, 116, 117],
		'T': [],
		'U': [2, 6,
				18, 22,
				34, 38,
				50, 54,
				66, 70,
				82, 86,
				98, 102,
				115, 116, 117],
		'V': [],
		'W': [],
		'X': [],
		'Y': [],
		'Z': []	
		}

		self.alignment = {'LEFT': -2,
		'CENTER': 0,
		'RIGHT': 1}

		self.color_map = {'RED': 15,
		'GREEN': 60,
		'AMBER': 63}

		self.current_color = self.color_map['GREEN']

		self.lit_pads = []

		self.letter_delay = 0.3
		self.word_delay = self.letter_delay / 2

		self.midi_output = mido.open_output('Launchpad S 1')

	def display(self, word):
		for letter in word.upper():
			if letter == ' ':
				time.sleep(self.word_delay)
			else:
				for pad in self.char_mapping[letter]:
					self.midi_output.send(mido.Message('note_on', note=pad, velocity=self.current_color))
					self.lit_pads.append(pad)
				time.sleep(self.letter_delay)
				self.clear_lit_pads()
				time.sleep(self.letter_delay)

	def clear_all_pads(self):
		for i in range(0, 120):
			self.midi_output.send(mido.Message('note_off', note=i))

	def clear_lit_pads(self):
		for i in self.lit_pads:
			self.midi_output.send(mido.Message('note_off', note=i))
		self.lit_pads = []

	def close_launchpad(self):
		self.midi_output.close()


if __name__ == "__main__":
	myLaunch = PyLaunch()
	myLaunch.display("BIG CHUNGUS")
	myLaunch.close_launchpad()