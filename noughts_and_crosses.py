import tkinter as tk
from itertools import cycle
root = tk.Tk()


class Tile(tk.Button):
    def __init__(self, parent, row, column):
        super().__init__(parent, width=TILE_SIZE,
                         height=TILE_SIZE, image=BLANK_IMAGE)
        self.row = row
        self.column = column
        self.set = False
        self.piece = id(self)
        self.bind('<Button-1>', self.click)

    def __repr__(self):
        return f'Tile {self.row=} {self.column=}'

    def click(self, *_):
        if self.set or game_over:
            return
        image = next(turn)
        self.config(image=image)
        self.piece = image_to_string[image]
        self.set = True
        check_game()

    def green(self):
        if self.piece == 'cross':
            self.config(image=GREEN_CROSS_IMAGE)
        else:
            self.config(image=GREEN_NOUGHT_IMAGE)


def check_game():
    global game_over
    checks = [[(row, column) for column in range(3)] for row in range(3)]
    checks.extend([[(row, column) for row in range(3)] for column in range(3)])
    checks.extend([[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]])
    for check in checks:
        if tiles[check[0]].piece == tiles[check[1]].piece == tiles[check[2]].piece:
            for coord in check:
                tiles[coord].green()
            game_over = True
            return True
    return False


game_over = False
BLANK_IMAGE = tk.PhotoImage(file='images/blank_tile.png')
NOUGHT_IMAGE = tk.PhotoImage(file='images/nought.png')
CROSS_IMAGE = tk.PhotoImage(file='images/cross.png')
GREEN_NOUGHT_IMAGE = tk.PhotoImage(file='images/green_nought.png')
GREEN_CROSS_IMAGE = tk.PhotoImage(file='images/green_cross.png')
TILE_SIZE = 100
image_to_string = {NOUGHT_IMAGE: 'nought', CROSS_IMAGE: 'cross'}
root.title('Noughts and Crosses')
root.resizable(False, False)
turn = cycle([NOUGHT_IMAGE, CROSS_IMAGE])

tiles = {(row, column): Tile(root, row, column)
         for column in range(3) for row in range(3)}
for tile in tiles.values():
    tile.grid(row=tile.row, column=tile.column)
tk.mainloop()
