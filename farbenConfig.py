def f_farbe(text, farbe):
        farben = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'cyan': '\033[96m'
        }
        reset = '\033[0m'
        return farben.get(farbe,'') + text + reset