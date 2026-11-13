from tkinter import *
from datetime import datetime
from tkinter import font

class PosPoint:
    def __init__(self, x, y):
        self.x = x * 2
        self.y = y * 2

    def GetGeo(self) -> str:
        return f"{self.x}x{self.y}"

def main():

    pos = PosPoint(250, int(300 / 3))
    root = Tk()
    root.geometry(pos.GetGeo())

    b_day_m = int(11)

    day = b_day_m - abs(datetime.now().month)
    b_day = abs(datetime.now().day - 17)

    fonts = font.Font(family="sans-serif", size=16, underline=True)

    Labels = Label(
        root,
        text=f"Your Birthday is in {b_day} Days & {day} Month",
        font=fonts,
        pady = 50 * 2,

    )

    Labels.pack()

    if datetime.now().month == 10 + 1 and datetime.now().day == 17:

        fonts = font.Font(family="sans-serif", size=16, underline=True)
        Label_1 = Label(
            root,
            text=f"Happy Birthday To You".upper(),
            font=fonts,
            pady=50 * 2,
            fg="green"
        )

        Label_1.pack()

    # root.configure(background="blue")

    root.mainloop()


if __name__ == "__main__":
    main()