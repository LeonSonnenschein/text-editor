import tkinter as tk


def menubar_command():
    print("command")


def make_menubar_file(window_menubar):
    file_menu = tk.Menu(window_menubar)
    window_menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="command", command=menubar_command)


def make_menubar_view(window_menubar):
    pass


def make_menubar_edit(window_menubar):
    pass


def make_menubar(window):
    window_menubar = tk.Menu(window)
    window.config(menu=window_menubar)
    make_menubar_file(window_menubar)
