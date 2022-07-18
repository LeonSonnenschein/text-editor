import tkinter as tk
import menubar

ROW = 0
COLUMN = 0


def make_window():
    window = tk.Tk()
    window.title('Text Editor')
    window.configure(background="black")
    window.geometry("1366x768")

    menubar.make_menubar(window)

    return window


def run():
    window = make_window()

    text_entry = tk.Text(window, width=1000, height=1000, bg="white", fg="black", font="none 12")
    text_entry.grid(row=0, column=0)

    window.mainloop()
