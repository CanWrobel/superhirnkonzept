class Stone:
    colors = {
        "B": "\x1b[44m\x1b[37m",  # Blue background, white text
        "R": "\x1b[41m\x1b[30m",  # Red background, black text
        "P": "\x1b[45m\x1b[30m",  # Purple background, black text
        "Y": "\x1b[43m\x1b[30m",  # Yellow background, black text
        "G": "\x1b[42m\x1b[30m",  # Green background, black text
        "O": "\x1b[48;2;255;165;0m\x1b[30m",  # Orange background (RGB), black text
        "W": "\x1b[47m\x1b[30m",  # White background, black text
        "D": "\x1b[40m\x1b[37m"  # Black background, white text
    }

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{Stone.colors[self.color]} {self.color} \x1b[0m"


# Main program
blue_stone = Stone("B")
red_stone = Stone("R")
purple_stone = Stone("P")
yellow_stone = Stone("Y")
green_stone = Stone("G")
orange_stone = Stone("O")
white_stone = Stone("W")
black_stone = Stone("D")

print("Mastermind")
print("Das ist nur ein Konzept. Der Coder hat folgenden Code eingelegt: R B P Y G")
print(f"|__| [{blue_stone}][{blue_stone}][{red_stone}][{orange_stone}][{yellow_stone}]")

print("-----------------------------------------")
print(f"|01| [{blue_stone}][{red_stone}][{purple_stone}][{yellow_stone}][{green_stone}] Coder response: {white_stone} {white_stone} {black_stone}{black_stone}")
print(f"|02| [{blue_stone}][{red_stone}][{purple_stone}][{yellow_stone}][{green_stone}] Coder response: {white_stone} {white_stone} {black_stone}{black_stone}")
print(f"|03| [{blue_stone}][{red_stone}][{purple_stone}][{yellow_stone}][{green_stone}] Coder response: {white_stone} {white_stone} {black_stone}{black_stone}")
print(f"|04| [{blue_stone}][{red_stone}][{purple_stone}][{yellow_stone}][{green_stone}] Coder response: {white_stone} {white_stone} {black_stone}{black_stone}")
print(f"|05| [{blue_stone}][{red_stone}][{purple_stone}][{yellow_stone}][{green_stone}] Coder response: {white_stone} {white_stone} {black_stone}{black_stone}")
print(f"|06| [{blue_stone}][{red_stone}][{purple_stone}][{yellow_stone}][{green_stone}] Coder response: {white_stone} {white_stone} {black_stone}{black_stone}")
print(f"|07| [{blue_stone}][{red_stone}][{purple_stone}][{yellow_stone}][{green_stone}] Coder response: {white_stone} {white_stone} {black_stone}{black_stone}")
print(f"|08| [{blue_stone}][{red_stone}][{purple_stone}][{yellow_stone}][{green_stone}] Coder response: {white_stone} {white_stone} {black_stone}{black_stone}")
print(f"|09| [{blue_stone}][{red_stone}][{purple_stone}][{yellow_stone}][{green_stone}] Coder response: {white_stone} {white_stone} {black_stone}{black_stone}")
print(f"|10| [{blue_stone}][{red_stone}][{purple_stone}][{yellow_stone}][{green_stone}] Coder response: {white_stone} {white_stone} {black_stone}{black_stone}")

