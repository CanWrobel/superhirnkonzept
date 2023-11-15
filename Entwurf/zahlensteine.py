class Stone:
    colors = {
        "1": "\x1b[44m\x1b[37m",  # Blue background, white text
        "2": "\x1b[41m\x1b[30m",  # Red background, black text
        "3": "\x1b[45m\x1b[30m",  # Purple background, black text
        "4": "\x1b[43m\x1b[30m",  # Yellow background, black text
        "5": "\x1b[42m\x1b[30m",  # Green background, black text
        "6": "\x1b[48;2;255;165;0m\x1b[30m",  # Orange background (RGB), black text
        "7": "\x1b[47m\x1b[30m",  # White background, black text
        "8": "\x1b[40m\x1b[37m"  # Black background, white text
    }

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{Stone.colors[self.color]} {self.color} \x1b[0m"


# Main program
blue_stone = Stone("1")
red_stone = Stone("2")
purple_stone = Stone("3")
yellow_stone = Stone("4")
green_stone = Stone("5")
orange_stone = Stone("6")
white_stone = Stone("7")
black_stone = Stone("8")

print("Mastermind")
print("Das ist nur ein Konzept. Der Coder hat folgenden Code eingelegt: B B R O Y")
print(f"|__| [{blue_stone}][{blue_stone}][{red_stone}][{orange_stone}][{yellow_stone}]")
print("Der Rater sieht diesen code aber nicht")
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

