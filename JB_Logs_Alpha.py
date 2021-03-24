import matplotlib as plt
import pandas as pd
import tkinter as tk

# DEF statements and commands

# different searches
def player_search():
    players = ent_player.get()
    for c in list_play:
        if c == players:
            punishment = df[df['player'] == c]['punishment']
            lbl_punishment.config(text=punishment)
            date = df[df['player'] == c]['date']
            lbl_date.config(text=date)
            end_date = df[df['player'] == c]['end_date']
            lbl_date_end.config(text=end_date)
            steam = df[df['player'] == c]['steam_link']
            lbl_steam.config(text=steam)

def date_searches():
    date = date_entry.get()
    for d in list_dates:
        if d == date:
            player_on_date = df[df['date'] == d]['player']
            date_search_results.config(text=player_on_date)

# navigation through menus
def player_search_menu():
    frame_search.tkraise()
    frame_player.tkraise()
    frame_player2.tkraise()
    frame_player3.tkraise()
    frame_player4.tkraise()
    back_option_search.tkraise()

def date_search_menu():
    frame_date.tkraise()

def back_button():
    frame_menu_search.tkraise()
    frame_menu_date.tkraise()
    frame_menu_quit.tkraise()

def quit_gui():
    root.quit()

# creation of TK
df = pd.read_csv("logs.csv", header=0)
root = tk.Tk()
root.wm_geometry("350x350")
root.title("authorization")

# lists for searchin for dates and players
list_dates = df['date'].unique()
list_play = df['player'].unique()

# different frames
# main menu
frame_menu_search = tk.Frame(root)
frame_menu_search.grid(row=0, column=0, sticky="news")
lbl_menu = tk.Label(frame_menu_search, text="Kramers JB GUI", font=("Courier", 20))
lbl_menu.pack()
button = tk.Button(frame_menu_search, text="Search players", command=player_search_menu)
button.pack()
frame_menu_date = tk.Frame(root)
frame_menu_date.grid(row=1, rowspan=2, column=0, sticky="news")
button = tk.Button(frame_menu_date, text="Search dates", command=date_search_menu)
button.pack()
frame_menu_quit = tk.Frame(root)
frame_menu_quit.grid(row=3, rowspan=7, column=0, sticky="news")
button = tk.Button(frame_menu_quit, text="QUIT GUI", background="salmon", relief='solid', command=quit_gui)
button.pack()

# this is what you use to search up a player
frame_search = tk.Frame(root)
frame_search.grid(row=0, column=0, sticky="news")
lbl_player = tk.Label(frame_search, text='Enter Username of Player:', font="Courier")
lbl_player.pack()
ent_player = tk.Entry(frame_search, bd=3)
ent_player.pack(pady=5)
button = tk.Button(frame_search, text="Search", command=player_search)
button.pack()

frame_player = tk.Frame(root)
frame_player.grid(row=1, column=0, sticky="news")
lbl_punishment = tk.Label(frame_player, text="punishment:", font="Courier")
lbl_punishment.pack()

frame_player2 = tk.Frame(root)
frame_player2.grid(row=2, column=0, sticky="news")
lbl_date = tk.Label(frame_player2, text="date:", font="Courier")
lbl_date.pack()

frame_player3 = tk.Frame(root)
frame_player3.grid(row=3, column=0, sticky="news")
lbl_date_end = tk.Label(frame_player3, text="end date:", font="Courier")
lbl_date_end.pack()

frame_player4 = tk.Frame(root)
frame_player4.grid(row=4, column=0, sticky="news")
lbl_steam = tk.Label(frame_player4, text="steam account:", font=("Courier", 10))
lbl_steam.pack()

back_option_search = tk.Frame(root)
back_option_search.grid(row=5, column=0, sticky="news")
button = tk.Button(back_option_search, text="back", command=back_button)
button.pack()

# this is what you use to search up a date
frame_date = tk.Frame(root)
frame_date.grid(row=0, rowspan=6, column=0, sticky="news")
date_search = tk.Label(frame_date, text='Enter Date:', font="Courier")
date_search.pack()
date_entry = tk.Entry(frame_date, bd=3)
date_entry.pack(pady=5)
button = tk.Button(frame_date, text="search", command=date_searches)
button.pack()
date_search_results = tk.Label(frame_date, text='Person According to Date:', font="Courier")
date_search_results.pack()
button = tk.Button(frame_date, text="back", command=back_button)
button.pack()

# creates what you initially see
frame_menu_search.tkraise()
frame_menu_date.tkraise()
frame_menu_quit.tkraise()
# keeps code running
root.mainloop()