import random
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
        'J': [4, 5, 6,
        21,
        37,
        53,
        69,
        85,
        98, 101,
        115, 116],
        'K': [2, 6,
        18, 21,
        34, 36,
        50, 51,
        66, 67,
        82, 84,
        98, 101,
        114, 118],
        'L': [2,
        18,
        34,
        50,
        66,
        82,
        98,
        114, 115, 116, 117, 118],
        'M': [2, 6,
        18, 19, 21, 22,
        34, 36, 38,
        50, 52, 54,
        66, 70,
        82, 86,
        98, 102, 
        114, 118],
        'N': [2, 6,
        18, 22,
        34, 35, 38,
        50, 52, 54,
        66, 69, 70,
        82, 86,
        98, 102,
        114, 118],
        'O': [3, 4, 5,
        18, 22,
        34, 38,
        50, 54,
        66, 70,
        82, 86,
        98, 102,
        115, 116, 117],
        'P': [2, 3, 4, 5,
        18, 22,
        34, 38,
        50, 51, 52, 53,
        66,
        82,
        98,
        114],
        'Q': [3, 4, 5,
        18, 22,
        34, 38,
        50, 54,
        66, 70,
        82, 84, 86,
        98, 101,
        115, 116, 118],
        'R': [2, 3, 4, 5,
        18, 22,
        34, 38,
        50, 51, 52, 53,
        66, 67,
        82, 84,
        98, 101,
        114, 118],
        'S': [3, 4, 5, 6,
        18,
        34,
        51, 52, 53,
        70,
        86,
        102,
        114, 115, 116, 117],
        'T': [2, 3, 4, 5, 6,
        20,
        36,
        52,
        68,
        84,
        100,
        116],
        'U': [2, 6,
        18, 22,
        34, 38,
        50, 54,
        66, 70,
        82, 86,
        98, 102,
        115, 116, 117],
        'V': [2, 6,
        18, 22,
        34, 38,
        50, 54,
        67, 69,
        83, 85,
        99, 101,
        116],
        'W': [2, 6,
        18, 22,
        34, 38,
        50, 54,
        66, 68, 70,
        82, 84, 86,
        98, 100, 102,
        115, 117],
        'X': [2, 6,
        18, 22,
        35, 37,
        52,
        67, 69,
        82, 86,
        98, 102,
        114, 118],
        'Y': [2, 6,
        18, 22,
        35, 37,
        52,
        68, 
        84,
        100,
        116],
        'Z': [2, 3, 4, 5, 6,
        22,
        37,
        52,
        67,
        82,
        98,
        114, 115, 116, 117, 118]    
        }

        self.alignment = {'LEFT': -2,
        'CENTER': 0,
        'RIGHT': 1}

        self.color_map = {'RED': 15,
        'GREEN': 60,
        'AMBER': 63}

        self.current_color = self.color_map['GREEN']

        self.lit_pads = []

        self.letter_delay = 0.5
        self.word_delay = self.letter_delay / 2

        self.midi_output = mido.open_output('Launchpad S 1')

    def display(self, word, color=None):
        if color != 'RANDOM':
            self.set_pad_color(color)
        for letter in word.upper():
            if color == 'RANDOM':
                self.set_pad_color(color)
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

    def set_letter_delay(self, new_delay):
        self.letter_delay = new_delay
        self.word_delay = new_delay / 2

    def set_pad_color(self, color):
        if color is not None:
            if color.upper() == 'RANDOM':
                self.current_color = self.color_map[random.choice(list(self.color_map.keys()))]
            else:
                self.current_color = self.color_map[color]

    def show_all_chars(self):
        for char in self.char_mapping.keys():
            self.display(char)

    def close_launchpad(self):
        self.midi_output.close()


if __name__ == "__main__":
    MY_LAUNCH = PyLaunch()
    MY_LAUNCH.display('GO HOOS', color='RANDOM')    
    MY_LAUNCH.set_letter_delay(0.1)
    MY_LAUNCH.show_all_chars()
    MY_LAUNCH.close_launchpad()
    exit()
