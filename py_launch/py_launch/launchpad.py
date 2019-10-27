import copy
import random
import time
import mido
from py_launch.pads import PadData


class PyLaunch():

    def __init__(self):
        
        local_pads = PadData()

        self.char_mapping = local_pads.char_mapping
        self.centered_chars = copy.deepcopy(self.char_mapping)
        self.symbol_mapping = local_pads.symbol_mapping        

        self.rows = [[pad + 16*x for pad in range(8)] for x in range(0, 8)]
        self.columns = [[x + 16*pad for pad in range(8)] for x in range(0, 8)]
        self.current_alignment = 4
        self.forbidden_range = [8+16*x + i for x in range(0, 8) for i in range(0, 8)]

        self.color_map = {'RED': 15,
        'ORANGE': 47,
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
                        if pad not in range(128) or pad in self.forbidden_range:
                            '''
                            try:
                                raise ValueError('Note must be between 0 and 127, current value is %d' % pad)
                            except:
                                pass
                                MY_LAUNCH.close_launchpad()
                            '''

                        else:
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

    def align_horizontal(self, column_alignment):
        """Aligns left edge of all characters to specified column, as long as full character can fit within the launchpad space"""
        for character in self.char_mapping.keys():
            shift_value = self.calculate_min_edge_distance(self.char_mapping[character], column_alignment)
            for index, pad in enumerate(self.char_mapping[character]):
                self.char_mapping[character][index] = pad + shift_value if column_alignment >= self.current_alignment else pad - shift_value
        self.current_alignment = column_alignment

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

    def close_launchpad(self):
        """Closes MIDI port"""
        self.clear_all_pads()
        self.midi_output.close()

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

    def push_horizontal(self, times=1, positive=True):
        """Moves pads along the x-axis"""
        for character in self.char_mapping.keys():
            for index, pad in enumerate(self.char_mapping[character]):
                self.char_mapping[character][index] = pad + times if positive else pad - times

    def push_vertical(self, times=1, positive=True):
        """Moves pads along the y-axis"""
        for character in self.char_mapping.keys():
            for index, pad in enumerate(self.char_mapping[character]):
                self.char_mapping[character][index] = pad - 16*times if positive else pad + 16*times

    def reset_pads(self):
        """Aligns all characters back to the default 'centered' position"""
        self.char_mapping = copy.deepcopy(self.centered_chars)
        self.current_alignment = 4

    def scroll(self, word, direction, positive=True):
        """Scrolls a word in the given axis direction across the launchpad"""
        #TODO: Clean up this method
        self.reset_pads()
        self.set_letter_delay(0.001)
        movement_range = []
        if direction == 'X':
            self.push_horizontal(times=5, positive=not positive)
            movement_range = range(0, 13)
            for char in word:
                for row in movement_range:
                    self.display_chars(char)
                    self.push_horizontal(positive=positive)
                self.reset_pads()
                self.push_horizontal(times=5, positive=not positive)
        else:
            self.push_vertical(times=8, positive=not positive)
            movement_range = range(0, 16)
            for char in word:
                for row in movement_range:
                    self.display_chars(char)
                    self.push_vertical(positive=positive)
                self.reset_pads()
                self.push_vertical(times=8, positive=not positive)
        self.reset_pads()

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

if __name__ == "__main__":
    MY_LAUNCH = PyLaunch()
    MY_LAUNCH.scroll("hello", direction='X', positive=False)
    MY_LAUNCH.scroll("world", direction='Y')
    MY_LAUNCH.close_launchpad()
    exit()
