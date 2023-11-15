# stein.py

class Stein:
    colors = {
        'R': '\033[41m\033[32m',  # Red background, Green text
        'B': '\033[44m\033[33m',  # Blue background, Orange text
        'Y': '\033[43m\033[35m',  # Yellow background, Purple text
        'L': '\033[45m\033[33m',  # Purple background, Yellow text
        'O': '\033[42m\033[34m',  # Orange background, Blue text
        'G': '\033[42m\033[31m',  # Green background, Red text
        'S': '\033[40m\033[37m',  # Black background, White text
        'W': '\033[47m\033[30m',  # White background, Black text
    }

    def __init__(self, color):
        self.color = color
        self.complement = self.find_complement(color)

    @staticmethod
    def find_complement(color):
        complements = {
            'R': 'G',
            'B': 'O',
            'Y': 'L',
            'L': 'Y',
            'O': 'B',
            'G': 'R',
            'S': 'W',  # S for Schwarz (Black)
            'W': 'S',  # W for Weiß (White)
        }
        return complements.get(color, '')

    def __str__(self):
        return self.color

# Beispiel für die Benutzung:

