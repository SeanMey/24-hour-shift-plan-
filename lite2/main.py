import json
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.filedialog import asksaveasfile
import pytest

from tkcalendar import *

from datetime import datetime

root = tk.Tk()
root.title("Vagt plans app")
root.geometry("800x700")

choice = []

#Create frame to calendar
frame = tk.LabelFrame(root, text="Kalender", padx=20, pady=5)
frame.grid(row=8, column=0, padx=20, pady=70)


# Create calendar
cal = Calendar(frame, selectmode="day",
               locale="da_DK",
               year=2021, month=1, day=1)
cal.grid(row=8, column=0, pady=20)
cal.tag_config('selection', foreground='green')


# Create Text Box Labelsd
vellcome_label = tk.Label(root, text="Velkommen til Vagt plan lægning af døgnvagter på 7631")
vellcome_label.grid(row=0, column=0, pady=(10))

user_pick = tk.Label(root, text="Vælg bruger:")
user_pick.grid(row=1, column=0, pady=(10,0))

def user_c():
    user_s = tk.Label(root, text="Hej " + combo_user.get() + " vælg den måned du vil ønske vagter i: ").grid(row=3, column=0, pady=10)


def mound():
    user_s = tk.Label(root, text="Ønsk vagter i " + combo_period.get() + " : ").grid(row=6, column=0, pady=10)


def show_date(event=None):
    print(event)
    day = cal.selection_get()

    if cal.get_calevents(date=day):
        cal.calevent_remove(date=day)
    else:
        cal.calevent_create(day, "Hej", "selection")

    print("---- 8< ----")
    for calevid in cal.get_calevents(tag="selection"):
        print(cal.calevent_cget(calevid, "date"))
    print("---- 8< ----")


# tjeck your dates
def save_date():
    root2 = tk.Tk()
    root2.title("Ønskede dage!")
    root2.geometry("600x600")

    choice = []
    for calevid in cal.get_calevents():
        choice.append(cal.calevent_cget(calevid, "date"))

    def save():
        a = combo_user.get()
        b = combo_period.get()
        c = list(map(str, choice))
        print(a)
        print(b)
        print(c)
        data = {}
        data['User'] = a
        data['Mound'] = b
        data['Dates'] = c
        with open("Wiches.json", "a") as file:
            json.dump(data, file)
            print("", file=file)



    def writeToJSONFile(path, fileName, data):
        json.dump(data, path)

    def makefil():
        a = combo_user.get()
        b = combo_period.get()
        c = list(map(str, choice))
        print(a)
        print(b)
        print(c)
        data = {}
        data['User'] = a
        data['Mound'] = b
        data['Dates'] = c
        files = [('JSON File', '*.json')]
        fileName = 'Wiches'
        filepos = asksaveasfile(filetypes=files, defaultextension=json, initialfile='Wiches')
        writeToJSONFile(filepos, fileName, data)

    def back():
        root2.destroy()

    def back2():
        root2.destroy()
        # fjern alle afmærket dage

    dates_label2 = tk.Label(root2, text="I " + combo_period.get() + " har du valgt disse dage: ")
    dates_label2.grid(row=1, column=1, pady=5)

    dates_label3 = tk.Label(root2, text=choice)
    dates_label3.grid(row=3, column=1, pady=5)

    bnt_ok = tk.Button(root2, text="OK", command=save).grid(row=4, column=2, pady=10)
    bnt_back = tk.Button(root2, text="Tilbage", command=back).grid(row=4, column=3, pady=10)
    bnt_new_mound = tk.Button(root2, text=" Tilføj ny måned ", command=back2).grid(row=4, column=4, pady=5)



#chouis user
options_user = [
        "Mie", "Hanne", "Randi","Maja", "Marie", "Joulanta", "Marina",
        "Maria", "Line","Charlotte", "Tinna", "Linda"
        ]

options_mound = [
        "Januar", "Februar", "Marst", "April",
        "Maj", "Juni", "Juli", "August",
        "September", "Oktober",
        "November", "December"
        ]

combo_user = ttk.Combobox(root, width=20, height=20, value=options_user)
combo_user.current(1)
combo_user.grid(row=1, column=1, pady=10)


#chouis mound
combo_period = ttk.Combobox(root, width=20, height=20, value=options_mound)
combo_period.current(1)
combo_period.grid(row=3, column=1, pady=10)

cal.bind("<<CalendarSelected>>", show_date)

bnt_select = tk.Button(root, text="Vælg", command=user_c).grid(row=1, column=3, pady=10)
bnt_mound = tk.Button(root, text="Vælg", command=mound).grid(row=3, column=3, pady=10)
bnt_save_days = tk.Button(root, text=" Gem valgte dage ", command=save_date).grid(row=9, column=4, pady=5)







root.mainloop()