class PadData():

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