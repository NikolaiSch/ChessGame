from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


blnk = "  "


class ChessBoard:
    def __init__(self):
        self.turn = "w"
        self.state = [
            ["br", "bb", "bk", "bq", "b", "bk", "bb", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            [blnk, blnk, blnk, blnk, blnk, blnk, blnk, blnk],
            [blnk, blnk, blnk, blnk, blnk, blnk, blnk, blnk],
            [blnk, blnk, blnk, blnk, blnk, blnk, blnk, blnk],
            [blnk, blnk, blnk, blnk, blnk, blnk, blnk, blnk],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wb", "wk", "wq", "w", "wk", "wb", "wr"],
        ]

    def move_piece(self, f_p, t_p):
        if self.state[f_p[0]][f_p[1]] != blnk:
            if self.check_move(f_p, t_p):
                board = self.state
                board[t_p[0]][t_p[1]] = board[f_p[0]][f_p[1]]
                board[f_p[0]][f_p[1]] = blnk
                self.state = board
                if self.turn == "w":
                    self.turn = "b"
                elif self.turn == "b":
                    self.turn = "w"

    def white_pawn(self, f_p, t_p):
        if f_p[0] == 6:
            if t_p[0] == 4:  # this is the initial 2 moves it can do
                if t_p[1] == f_p[1]:  # checks x coords remain same
                    return True
        if t_p[0] == f_p[0] - 1:  # New y = 1 above previous y
            if t_p[1] == f_p[1]:  # checks both x coords remain same
                if (
                    blnk == self.state[t_p[0]][t_p[1]]
                ):  # checks the square it wants to go to is empty
                    return True
            if t_p[1] == f_p[1] + 1:  # checks both x coords remain don't same
                if (
                    self.state[t_p[0]][t_p[1]][0] == "b"
                ):  # checks the square it wants to go to is not empty
                    return True
            if t_p[1] == f_p[1] - 1:  # checks both x coords dont remain same
                if (
                    self.state[t_p[0]][t_p[1]][0] == "b"
                ):  # checks the square it wants to go to is not empty
                    return True
        return False

    def black_pawn(self, f_p, t_p):
        if f_p[0] == 1:
            if t_p[0] == 3:  # this is the initial 2 moves it can do
                if t_p[1] == f_p[1]:  # checks x coords remain same
                    return True
        if t_p[0] == f_p[0] + 1:  # New y = 1 above previous y
            if t_p[1] == f_p[1]:  # checks both x coords remain same
                if (
                    blnk == self.state[t_p[0]][t_p[1]]
                ):  # checks the square it wants to go to is empty
                    return True
            if t_p[1] == f_p[1] + 1:  # checks both x coords remain don't same
                if (
                    self.state[t_p[0]][t_p[1]][0] == "w"
                ):  # checks the square it wants to go to is not empty
                    return True
            if t_p[1] == f_p[1] - 1:  # checks both x coords dont remain same
                if (
                    self.state[t_p[0]][t_p[1]][0] == "w"
                ):  # checks the square it wants to go to is not empty
                    return True
        return False

    def white_rook(self, f_p, t_p):

        if f_p[1] == t_p[1]:
            print(t_p[0], f_p[0])
            if t_p[0] - f_p[0] > 0:
                for i in range(f_p[0] + 1, t_p[0]):
                    if blnk != self.state[i][f_p[1]]:
                        return False
                if self.state[t_p[0]][t_p[1]][0] != "w":
                    return True

            if t_p[0] - f_p[0] < 0:
                for i in range(t_p[0] + 1, f_p[0]):
                    if blnk != self.state[i][f_p[1]]:
                        return False
                if self.state[t_p[0]][t_p[1]][0] != "w":
                    return True

        if f_p[0] == t_p[0]:
            print(t_p[1], f_p[1])
            if t_p[1] - f_p[1] > 0:
                for i in range(f_p[1] + 1, t_p[1]):
                    if blnk != self.state[f_p[0]][i]:
                        return False
                if self.state[t_p[0]][t_p[1]][0] != "w":
                    return True

            if t_p[1] - f_p[1] < 0:
                for i in range(t_p[1] + 1, f_p[1]):
                    if blnk != self.state[f_p[0]][i]:
                        return False
                if self.state[t_p[0]][t_p[1]][0] != "w":
                    return True
        return False

    def black_rook(self, f_p, t_p):
        if f_p[1] == t_p[1]:
            print(t_p[0], f_p[0])
            if t_p[0] - f_p[0] > 0:
                for i in range(f_p[0] + 1, t_p[0]):
                    if blnk != self.state[i][f_p[1]]:
                        return False
                if self.state[t_p[0]][t_p[1]][0] != "b":
                    return True

            if t_p[0] - f_p[0] < 0:
                for i in range(t_p[0] + 1, f_p[0]):
                    if blnk != self.state[i][f_p[1]]:
                        return False
                if self.state[t_p[0]][t_p[1]][0] != "b":
                    return True

        if f_p[0] == t_p[0]:
            print(t_p[1], f_p[1])
            if t_p[1] - f_p[1] > 0:
                for i in range(f_p[1] + 1, t_p[1]):
                    if blnk != self.state[f_p[0]][i]:
                        return False
                if self.state[t_p[0]][t_p[1]][0] != "b":
                    return True

            if t_p[1] - f_p[1] < 0:
                for i in range(t_p[1] + 1, f_p[1]):
                    if blnk != self.state[f_p[0]][i]:
                        return False
                if self.state[t_p[0]][t_p[1]][0] != "b":
                    return True
        return False

    def white_knight(self, f_p, t_p):
        if abs(f_p[0] - t_p[0]) == 2:
            if abs(f_p[1] - t_p[1]) == 1:
                if self.state[t_p[0]][t_p[1]][0] != "w":
                    return True
        elif abs(f_p[1] - t_p[1]) == 2:
            if abs(f_p[0] - t_p[0]) == 1:
                if self.state[t_p[0]][t_p[1]][0] != "w":
                    return True
        return False

    def black_knight(self, f_p, t_p):
        if abs(f_p[0] - t_p[0]) == 2:
            if abs(f_p[1] - t_p[1]) == 1:
                if self.state[t_p[0]][t_p[1]][0] != "w":
                    return True
        elif abs(f_p[1] - t_p[1]) == 2:
            if abs(f_p[0] - t_p[0]) == 1:
                if self.state[t_p[0]][t_p[1]][0] != "w":
                    return True
        return False

    def check_move(self, f_p, t_p):
        if self.state[f_p[0]][f_p[1]][0] != self.turn:
            return False
        match self.state[f_p[0]][f_p[1]]:
            case "wp":
                return self.white_pawn(f_p, t_p)
            case "bp":
                return self.black_pawn(f_p, t_p)
            case "wr":
                return self.white_rook(f_p, t_p)
            case "br":
                return self.black_rook(f_p, t_p)
            case "wk":
                return self.white_knight(f_p, t_p)
            case "bk":
                return self.white_knight(f_p, t_p)


cb = ChessBoard()

root = Tk()
stats = Tk()

bp = ImageTk.PhotoImage(Image.open("imgs/bp.webp").resize((30, 30)))
wp = ImageTk.PhotoImage(Image.open("imgs/wp.webp").resize((30, 30)))
br = ImageTk.PhotoImage(Image.open("imgs/br.webp").resize((30, 30)))
wr = ImageTk.PhotoImage(Image.open("imgs/wr.webp").resize((30, 30)))
bk = ImageTk.PhotoImage(Image.open("imgs/bk.webp").resize((30, 30)))
wk = ImageTk.PhotoImage(Image.open("imgs/wk.webp").resize((30, 30)))
bq = ImageTk.PhotoImage(Image.open("imgs/bq.webp").resize((30, 30)))
wq = ImageTk.PhotoImage(Image.open("imgs/wq.webp").resize((30, 30)))
bb = ImageTk.PhotoImage(Image.open("imgs/bb.webp").resize((30, 30)))
wb = ImageTk.PhotoImage(Image.open("imgs/wb.webp").resize((30, 30)))
b = ImageTk.PhotoImage(Image.open("imgs/b.webp").resize((30, 30)))
w = ImageTk.PhotoImage(Image.open("imgs/w.webp").resize((30, 30)))
blank = ImageTk.PhotoImage(Image.open("imgs/blank.webp").resize((30, 30)))

style = ttk.Style()
style.theme_use("classic")
style.configure("BW.TButton", foreground="white", background="red")
style.configure("BWSelected.TButton", foreground="white", background="red")
style.configure("Color.TButton", background="gray")
style.configure("NoColor.TButton", background="white")

frm = ttk.Frame(root)
frame = ttk.Frame(stats)
frm.grid()
frame.grid()

county = 0
countx = 0

selection = []

points_dict = {"p": 1, "k": 3, "b": 3, "r": 5, "q": 9}


def points(color):
    points = 0
    for i in cb.state:
        for j in i:
            if j[0] == color and len(j) == 2:
                print(j)
                points += points_dict[j[1]]
    return points


def select(x, y):
    global selection
    if selection == [int(x), int(y)]:
        selection = []
        render_components()
    elif selection == []:
        selection = [int(x), int(y)]
        render_components()
    else:
        cb.move_piece(selection, [int(x), int(y)])
        selection = []
        render_components()


def clear():
    for widgets in frm.winfo_children():
        widgets.destroy()


def clearStats():
    for widgets in frame.winfo_children():
        widgets.destroy()


def render_components():
    clear()
    clearStats()
    ttk.Label(frame, text=f"turn:").grid(column=0, row=0)
    ttk.Label(frame, text=cb.turn).grid(column=1, row=0)
    ttk.Label(frame, text=f"white points:").grid(column=0, row=1)
    ttk.Label(frame, text=points("w")).grid(column=1, row=1)
    ttk.Label(frame, text=f"black points:").grid(column=0, row=2)
    ttk.Label(frame, text=points("b")).grid(column=1, row=2)
    for y in range(0, 8):
        for x in range(0, 8):
            if (x + y) % 2 == 1:
                s = "Color.TButton"
                sW = "BWSelected.TButton"
            else:
                s = "NoColor.TButton"
                sW = "BW.TButton"
            if selection == [x, y]:
                print(cb.state[x][y])
                match cb.state[x][y]:
                    case "wp":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=wp,
                            style=sW,
                        ).grid(column=y, row=x + 1)
                    case "bp":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=bp,
                            style=sW,
                        ).grid(column=y, row=x + 1)
                    case "br":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=br,
                            style=sW,
                        ).grid(column=y, row=x + 1)
                    case "wr":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=wr,
                            style=sW,
                        ).grid(column=y, row=x + 1)
                    case "wk":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=wk,
                            style=sW,
                        ).grid(column=y, row=x + 1)
                    case "bk":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=bk,
                            style=sW,
                        ).grid(column=y, row=x + 1)
                    case "wq":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=wq,
                            style=sW,
                        ).grid(column=y, row=x + 1)
                    case "bq":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=bq,
                            style=sW,
                        ).grid(column=y, row=x + 1)
                    case "w":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=w,
                            style=sW,
                        ).grid(column=y, row=x + 1)
                    case "b":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=b,
                            style=sW,
                        ).grid(column=y, row=x + 1)
                    case "bb":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=bb,
                            style=sW,
                        ).grid(column=y, row=x + 1)
                    case "wb":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=wb,
                            style=sW,
                        ).grid(column=y, row=x + 1)
                    case _:
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=blank,
                            style=sW,
                        ).grid(column=y, row=x + 1)
            else:
                match cb.state[x][y]:
                    case "wp":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            image=wp,
                            style=s,
                        ).grid(column=y, row=x + 1)
                    case "bp":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            width=20,
                            style=s,
                            image=bp,
                        ).grid(column=y, row=x + 1)
                    case "br":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            style=s,
                            width=20,
                            image=br,
                        ).grid(column=y, row=x + 1)
                    case "wr":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            style=s,
                            width=20,
                            image=wr,
                        ).grid(column=y, row=x + 1)
                    case "wk":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            style=s,
                            width=20,
                            image=wk,
                        ).grid(column=y, row=x + 1)
                    case "bk":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            style=s,
                            width=20,
                            image=bk,
                        ).grid(column=y, row=x + 1)
                    case "wq":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            style=s,
                            width=20,
                            image=wq,
                        ).grid(column=y, row=x + 1)
                    case "bq":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            padding=20,
                            style=s,
                            width=20,
                            image=bq,
                        ).grid(column=y, row=x + 1)
                    case "w":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            style=s,
                            padding=20,
                            width=20,
                            image=w,
                        ).grid(column=y, row=x + 1)
                    case "b":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            style=s,
                            padding=20,
                            width=20,
                            image=b,
                        ).grid(column=y, row=x + 1)
                    case "bb":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            style=s,
                            padding=20,
                            width=20,
                            image=bb,
                        ).grid(column=y, row=x + 1)
                    case "wb":
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            style=s,
                            padding=20,
                            width=20,
                            image=wb,
                        ).grid(column=y, row=x + 1)
                    case _:
                        ttk.Button(
                            frm,
                            command=lambda a=x, b=y: select(a, b),
                            style=s,
                            padding=20,
                            width=20,
                            image=blank,
                        ).grid(column=y, row=x + 1)


if __name__ == "__main__":
    render_components()
    root.mainloop()
