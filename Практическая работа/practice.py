from tkinter import *

import gspread
from time import strftime, gmtime
from oauth2client.service_account import ServiceAccountCredentials


def function(event):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('Practice SUSU-beefa1e2febc.json', scope)

    gc = gspread.authorize(credentials)

    wks = gc.open("Table").sheet1
    print(wks.get_all_records())

    data = strftime("%d.%m.%y", gmtime())
    wks.append_row([data])


master = Tk()

master.geometry("300x300")

master.title("Окно с кнопкой")

button = Button(master, text="Запись в таблицу")
button.bind("<Button-1>", function)

button.pack()

master.mainloop()
