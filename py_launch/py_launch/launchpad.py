import copy
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
        114, 115, 116, 117, 118],
        '1': [4,
        19, 20,
        34, 36,
        52,
        68,
        84,
        100,
        114, 115, 116, 117, 118],
        '2': [3, 4, 5,
        18, 22,
        38,
        53,
        68,
        83,
        98,
        114, 115, 116, 117, 118],
        '3': [2, 3, 4, 5, 6, 
        21,
        36,
        53,
        70,
        86,
        98, 102,
        115, 116, 117],
        '4': [5,
        20, 21,
        35, 37,
        50, 53,
        66, 67, 68, 69, 70,
        85, 
        101,
        117],
        '5': [2, 3, 4, 5, 6,
        18,
        34, 
        50, 51, 52, 53,
        70,
        86,
        98, 102,
        115, 116, 117],
        '6': [4, 5, 
        19,
        34,
        50, 51, 52, 53,
        66, 70,
        82, 86, 
        98, 102, 
        115, 116, 117],
        '7': [2, 3, 4, 5, 6,
        22, 
        37, 
        52, 
        67,
        83,
        99,
        115],
        '8': [3, 4, 5, 
        18, 22,
        34, 38, 
        51, 52, 53,
        66, 70,
        82, 86,
        98, 102,
        115, 116, 117],
        '9': [3, 4, 5,
        18, 22,
        34, 38, 
        50, 54,
        67, 68, 69, 70,
        86,
        101,
        115, 116],
        '0': [3, 4, 5,
        18, 22,
        34, 37, 38,
        50, 52, 54,
        66, 68, 70,
        82, 83, 86,
        98, 102,
        115, 116, 117],
        '$': [4,
        19, 20, 21,
        34, 36, 38,
        51, 52,
        68, 69,
        82, 84, 86,
        99, 100, 101,
        116],
        '!': [4,
        20,
        36,
        52,
        68,
        84,
        116],
        '?': [3, 4, 5,
        18, 22,
        38,
        53, 
        68,
        84,
        116]
        }

        self.centered_chars = copy.deepcopy(self.char_mapping)

        self.symbol_mapping = {'SMILE': [2, 5,
        18, 21,
        34, 37,
        64, 71,
        81, 86,
        98, 99, 100, 101],
        'FROWN': [2, 5,
        18, 21,
        34, 37,
        66, 67, 68, 69,
        81, 86,
        96, 103],
        'HEART': [2, 3, 5, 6,
        17, 18, 19, 20, 21, 22, 23,
        33, 34, 35, 36, 37, 38, 39,
        49, 50, 51, 52, 53, 54, 55,
        66, 67, 68, 69, 70,
        83, 84, 85,
        100],
        'OK': [0, 1, 2, 4, 7,
        16, 18, 20, 22,
        32, 34, 36, 37,
        48, 50, 52,
        64, 66, 68,
        80, 82, 84, 85,
        96, 98, 100, 102,
        112, 113, 114, 116, 119],
        'UP': [4,
        19, 20, 21,
        34, 35, 36, 37, 38,
        49, 50, 51, 52, 53, 54, 55,
        67, 68, 69, 
        83, 84, 85, 
        99, 100, 101,
        115, 116, 117],
        'DOWN': [3, 4, 5,
        19, 20, 21,
        35, 36, 37,
        51, 52, 53,
        65, 66, 67, 68, 69, 70, 71,
        82, 83, 84, 85, 86,
        99, 100, 101,
        116],
        'CHECK': [23,
        38,
        53,
        64, 68,
        81, 83,
        98],
        'NO': [3, 4, 5,
        18, 22,
        33, 35, 39,
        49, 52, 55,
        65, 69, 71,
        82, 86,
        99, 100, 101],
        'PEACE': [3, 4, 5,
        18, 20, 22,
        33, 36, 39,
        49, 52, 55,
        65, 67, 68, 69, 71,
        82, 84, 86,
        99, 100, 101]
        }

        self.rows = [[pad + 16*x for pad in range(8)] for x in range(0, 8)]
        self.columns = [[x + 16*pad for pad in range(8)] for x in range(0, 8)]
        self.current_alignment = 4

        self.color_map = {'RED': 15,
        'GREEN': 60,
        'AMBER': 63}

        self.current_color = self.color_map['GREEN']

        self.lit_pads = []

        self.symbol_delay = 1
        self.letter_delay = 0.5
        self.word_delay = self.letter_delay / 2

        self.midi_output = mido.open_output('Launchpad S 1')
        self.midi_output.send(mido.Message('note_on', note=120, velocity=28))

    def display_chars(self, words, color=None, repeat=0):
        """Displays letters in a word that is passed in. Valid characters are can be represented by 1 key on a keyboard"""
        if color != 'RANDOM':
            self.set_pad_color(color)
        while repeat > -1:
            for character in words.upper():
                if color == 'RANDOM':
                    self.set_pad_color(color)
                if character == ' ':
                    time.sleep(self.word_delay)
                else:
                    for pad in self.char_mapping[character]:
                        if pad not in range(128):
                            try:
                                raise ValueError('Note must be between 0 and 127, current value is %d' % pad)
                            except:
                                MY_LAUNCH.close_launchpad()
                                raise
                        self.midi_output.send(mido.Message('note_on', note=pad, velocity=self.current_color))
                        self.lit_pads.append(pad)
                    time.sleep(self.letter_delay)
                    self.clear_lit_pads()
                    time.sleep(self.letter_delay)
            repeat = repeat - 1

    def display_symbols(self, symbols, color=None, repeat=0):
        """Displays special symbols that cannoted by represented by 1 key on a keyboard"""
        if color != 'RANDOM':
            self.set_pad_color(color)
        while repeat > -1:
            for symbol in symbols.upper().split():
                if color == 'RANDOM':
                    self.set_pad_color(color)
                for pad in self.symbol_mapping[symbol]:
                    self.midi_output.send(mido.Message('note_on', note=pad, velocity=self.current_color))
                    self.lit_pads.append(pad)
                time.sleep(self.symbol_delay)
                self.clear_lit_pads()
                time.sleep(self.symbol_delay)
            repeat = repeat - 1

    def align(self, column_alignment):
        """Aligns left edge of all characters to specified column, as long as full character can fit within the launchpad space"""
        for character in self.char_mapping.keys():
            shift_value = self.calculate_min_edge_distance(self.char_mapping[character], column_alignment)
            print("Char %s, shift %d" % (character, shift_value))
            for index, pad in enumerate(self.char_mapping[character]):
                self.char_mapping[character][index] = pad + shift_value if column_alignment >= self.current_alignment else pad - shift_value
        self.current_alignment = column_alignment

    def align_to_center(self):
        """Aligns all characters back to the default 'centered' position"""
        self.char_mapping = self.centered_chars
        self.current_alignment = 4

    def calculate_min_edge_distance(self, pads, column):
        """Returns the minimum distance from a character to a specified column"""
        h_edges = self.get_horizontal_edges(pads)
        print(h_edges)
        print("%s, %s" % (column, self.current_alignment))
        if column > self.current_alignment and h_edges[1] + abs(h_edges[0] - column) > 7:
            return 7 - h_edges[1]
        return abs(h_edges[0] - column)
        #return abs(h_edges[0] - column) if abs(h_edges[0] - column) <= abs(h_edges[1] - column) else abs(h_edges[1] - column)

    def clear_all_pads(self):
        """Turns off all pads"""
        for i in range(0, 121):
            self.midi_output.send(mido.Message('note_off', note=i))

    def clear_lit_pads(self):
        """Turns off all pads that are currently lit"""
        for i in self.lit_pads:
            self.midi_output.send(mido.Message('note_off', note=i))
            self.lit_pads = []

    def get_horizontal_edges(self, pads):
        """Returns the left and right edges of a character"""
        right_edge = 0
        left_edge = 7
        for pad in pads:
            for index, column in enumerate(self.columns):
                if pad in column:
                    right_edge = index if index > right_edge else right_edge
                    left_edge = index if index < left_edge else left_edge
        return [left_edge, right_edge]

    def set_letter_delay(self, new_delay):
        """Sets the delay between letters, as well as the delay between words"""
        self.letter_delay = new_delay
        self.word_delay = new_delay / 2

    def set_pad_color(self, color):
        """Sets the current pad color"""
        if color is not None:
            if color.upper() == 'RANDOM':
                self.current_color = self.color_map[random.choice(list(self.color_map.keys()))]
            else:
                self.current_color = self.color_map[color]

    def show_all_chars(self, color=None, repeat=0):
        """Cycles through all characters in the character map"""
        for char in self.char_mapping.keys():
            self.display_chars(char, color=color, repeat=repeat)

    def close_launchpad(self):
        """Closes MIDI port"""
        self.clear_all_pads()
        self.midi_output.close()


if __name__ == "__main__":
    MY_LAUNCH = PyLaunch()
    #MY_LAUNCH.align(0)
    #print(MY_LAUNCH.get_horizontal_edges(MY_LAUNCH.char_mapping['A']))
    
    '''
    MY_LAUNCH.set_letter_delay(0.001)
    for char in 'SMASH THAT F':
        for col in [4, 3, 2, 1, 0]:
            MY_LAUNCH.align(col)
            MY_LAUNCH.display_chars(char)
    
    
    for col in [4, 3, 2, 1, 0]:
        MY_LAUNCH.align(col)
        MY_LAUNCH.display_chars('A')
    
    '''
    MY_LAUNCH.set_letter_delay(0.2)
    MY_LAUNCH.display_chars('NAIDORF DID 911', color='RANDOM')  
    '''
    MY_LAUNCH.display_symbols('no smile', color='RANDOM')  
    
    MY_LAUNCH.align(0)
    MY_LAUNCH.display_chars('A')
    MY_LAUNCH.align(3)
    MY_LAUNCH.display_chars('A')
    #MY_LAUNCH.show_all_chars()
    '''
    MY_LAUNCH.close_launchpad()
    exit()
