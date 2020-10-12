#!/usr/bin/python3
# -*- coding: utf-8 -*
import tkinter as tk
from tkinter import *
from tkinter import ttk
from time import strftime
from pathlib import Path
from tkinter import Menu
import sqlite3
import datetime as dt


class Program:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1024x768")
        self.root.title("Przypominacz 3.0")
        self.root.configure(background="black")

    # -----------------Położenie kwadratu pod datą----------
        canvas = tk.Canvas(self.root, width=300, height=300)
        canvas.place(x=10, y=10)
        canvas.create_rectangle((1, 1, 300, 300), fill="#ffffff", width=0)

    # -----------------Położenie zegara------------------
        self.lb_clock = tk.Label(self.root, font=(
            "Times New Roman", 30), fg="green", bg="white")
        self.lb_clock.place(x=75, y=220)

        self.timer()  # pierwsze wywołanie metody timer
        self.MenuRozwijane()  # wywołanie menu
        self.Data()  # wywołanie daty
        self.imieniny()  # wywołanie imienin
        self.WyswietlaniePlanuLekcji()# wywołanie planu lekcji
        self.Powiadomienia() # wywołanie powiadomień

        self.root.mainloop()

#  -------------Definicje class-y Program--------------
    def timer(self):
        self.lb_clock.config(text=str(dt.datetime.now().time()).split(".")[0])
        # ustawienie kolejnego wywołania metody timer
        self.root.after(1000, self.timer)

    def MenuRozwijane(self):
        menu = Menu(self.root)

        new_item = Menu(menu)
        menu.add_cascade(label="Przypomnienia", menu=new_item)
        new_item.add_command(
            label="Dodaj przypomnienie godzinowe", command=self.dodajPrzypomnienie)
        new_item.add_separator()
        new_item.add_command(label="Usuń przypomnienie",
                             foreground="red", font="bold", command=self.UsunPrzypomnienie)

        new_waga = Menu(menu)
        menu.add_cascade(label="Plan lekcji", menu=new_waga)
        new_waga.add_command(label="Dodaj nową lekcję",
                             command=self.DodajPlanLekcji)
        new_waga.add_separator()
        new_waga.add_command(label="Usuń lekcję",
                             foreground="red", font="bold", command=self.UsuwaniePlanuLekcji)

        self.root.config(menu=menu)

    def WyswietlaniePlanuLekcji(self):
        x_planLekcji = 10
        y_planLekcji = 340
        z = strftime('%w')
        if z == "1":
            kolor_poniedzialek = "yellow"
            kolor_wtorek = "green"
            kolor_sroda = "green"
            kolor_czwartek = "green"
            kolor_piatek = "green"
        elif z == "2":
            kolor_poniedzialek = "green"
            kolor_wtorek = "yellow"
            kolor_sroda = "green"
            kolor_czwartek = "green"
            kolor_piatek = "green"
        elif z == "3":
            kolor_poniedzialek = "green"
            kolor_wtorek = "green"
            kolor_sroda = "yellow"
            kolor_czwartek = "green"
            kolor_piatek = "green"
        elif z == "4":
            kolor_poniedzialek = "green"
            kolor_wtorek = "green"
            kolor_sroda = "green"
            kolor_czwartek = "yellow"
            kolor_piatek = "green"
        elif z == "5":
            kolor_poniedzialek = "green"
            kolor_wtorek = "green"
            kolor_sroda = "green"
            kolor_czwartek = "green"
            kolor_piatek = "yellow"
        else:
            kolor_poniedzialek = "green"
            kolor_wtorek = "green"
            kolor_sroda = "green"
            kolor_czwartek = "green"
            kolor_piatek = "green"

        i = 1
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        c.execute('SELECT * , oid FROM plan_lekcji WHERE dzien="Poniedziałek"')
        rec = c.fetchall()
        for r in rec:
            # poniedzialek
            tk.Label(self.root, text=str(r[1]), font=(
                "Ariel", 10), fg=kolor_poniedzialek, bg="black").place(x=x_planLekcji, y=y_planLekcji)
            tk.Label(self.root, text=str(i)+". "+str(r[2])+" - "+str(r[3]+"  "+str(r[4])), font=(
                "Arial", 11), fg=kolor_poniedzialek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[5])+" - "+str(r[6]+"  "+str(r[7])), font=(
                "Arial", 11), fg=kolor_poniedzialek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[8])+" - "+str(r[9]+"  "+str(r[10])), font=(
                "Arial", 11), fg=kolor_poniedzialek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[11])+" - "+str(r[12]+"  "+str(r[13])), font=(
                "Arial", 11), fg=kolor_poniedzialek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[14])+" - "+str(r[15]+"  "+str(r[16])), font=(
                "Arial", 11), fg=kolor_poniedzialek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[17])+" - "+str(r[18]+"  "+str(r[19])), font=(
                "Arial", 11), fg=kolor_poniedzialek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[20])+" - "+str(r[21]+"  "+str(r[22])), font=(
                "Arial", 11), fg=kolor_poniedzialek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[23])+" - "+str(r[24]+"  "+str(r[25])), font=(
                "Arial", 11), fg=kolor_poniedzialek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[26])+" - "+str(r[27]+"  "+str(r[28])), font=(
                "Arial", 11), fg=kolor_poniedzialek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)

        conn.close()

        x_planLekcji = 210
        y_planLekcji = 340
        i = 1
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        c.execute('SELECT * , oid FROM plan_lekcji WHERE dzien="Wtorek"')
        rec = c.fetchall()
        for r in rec:
            # wtorek
            tk.Label(self.root, text=str(r[1]), font=(
                "Ariel", 10), fg=kolor_poniedzialek, bg="black").place(x=x_planLekcji, y=y_planLekcji)
            tk.Label(self.root, text=str(i)+". "+str(r[2])+" - "+str(r[3]+"  "+str(r[4])), font=(
                "Arial", 11), fg=kolor_wtorek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[5])+" - "+str(r[6]+"  "+str(r[7])), font=(
                "Arial", 11), fg=kolor_wtorek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[8])+" - "+str(r[9]+"  "+str(r[10])), font=(
                "Arial", 11), fg=kolor_wtorek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[11])+" - "+str(r[12]+"  "+str(r[13])), font=(
                "Arial", 11), fg=kolor_wtorek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[14])+" - "+str(r[15]+"  "+str(r[16])), font=(
                "Arial", 11), fg=kolor_wtorek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[17])+" - "+str(r[18]+"  "+str(r[19])), font=(
                "Arial", 11), fg=kolor_wtorek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[20])+" - "+str(r[21]+"  "+str(r[22])), font=(
                "Arial", 11), fg=kolor_wtorek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[23])+" - "+str(r[24]+"  "+str(r[25])), font=(
                "Arial", 11), fg=kolor_wtorek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text="D. "+str(r[26])+" - "+str(r[27]+"  "+str(r[28])), font=(
                "Arial", 11), fg=kolor_wtorek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)

        conn.close()

        x_planLekcji = 410
        y_planLekcji = 340
        i = 1
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        c.execute('SELECT * , oid FROM plan_lekcji WHERE dzien="Środa"')
        rec = c.fetchall()
        for r in rec:
            # środa
            tk.Label(self.root, text=str(r[1]), font=(
                "Ariel", 10), fg=kolor_sroda, bg="black").place(x=x_planLekcji, y=y_planLekcji)
            tk.Label(self.root, text=str(i)+". "+str(r[2])+" - "+str(r[3]+"  "+str(r[4])), font=(
                "Arial", 11), fg=kolor_sroda, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[5])+" - "+str(r[6]+"  "+str(r[7])), font=(
                "Arial", 11), fg=kolor_sroda, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[8])+" - "+str(r[9]+"  "+str(r[10])), font=(
                "Arial", 11), fg=kolor_sroda, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[11])+" - "+str(r[12]+"  "+str(r[13])), font=(
                "Arial", 11), fg=kolor_sroda, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[14])+" - "+str(r[15]+"  "+str(r[16])), font=(
                "Arial", 11), fg=kolor_sroda, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[17])+" - "+str(r[18]+"  "+str(r[19])), font=(
                "Arial", 11), fg=kolor_sroda, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[20])+" - "+str(r[21]+"  "+str(r[22])), font=(
                "Arial", 11), fg=kolor_sroda, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[23])+" - "+str(r[24]+"  "+str(r[25])), font=(
                "Arial", 11), fg=kolor_sroda, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[26])+" - "+str(r[27]+"  "+str(r[28])), font=(
                "Arial", 11), fg=kolor_sroda, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)

        conn.close()

        x_planLekcji = 610
        y_planLekcji = 340
        i = 1
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        c.execute('SELECT * , oid FROM plan_lekcji WHERE dzien="Czwartek"')
        rec = c.fetchall()
        for r in rec:
            # czwartek
            tk.Label(self.root, text=str(r[1]), font=(
                "Ariel", 10), fg=kolor_czwartek, bg="black").place(x=x_planLekcji, y=y_planLekcji)
            tk.Label(self.root, text=str(i)+". "+str(r[2])+" - "+str(r[3]+"  "+str(r[4])), font=(
                "Arial", 11), fg=kolor_czwartek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[5])+" - "+str(r[6]+"  "+str(r[7])), font=(
                "Arial", 11), fg=kolor_czwartek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[8])+" - "+str(r[9]+"  "+str(r[10])), font=(
                "Arial", 11), fg=kolor_czwartek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[11])+" - "+str(r[12]+"  "+str(r[13])), font=(
                "Arial", 11), fg=kolor_czwartek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[14])+" - "+str(r[15]+"  "+str(r[16])), font=(
                "Arial", 11), fg=kolor_czwartek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[17])+" - "+str(r[18]+"  "+str(r[19])), font=(
                "Arial", 11), fg=kolor_czwartek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[20])+" - "+str(r[21]+"  "+str(r[22])), font=(
                "Arial", 11), fg=kolor_czwartek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[23])+" - "+str(r[24]+"  "+str(r[25])), font=(
                "Arial", 11), fg=kolor_czwartek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[26])+" - "+str(r[27]+"  "+str(r[28])), font=(
                "Arial", 11), fg=kolor_czwartek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)

        conn.close()

        x_planLekcji = 810
        y_planLekcji = 340
        i = 1
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        c.execute('SELECT * , oid FROM plan_lekcji WHERE dzien="Piątek"')
        rec = c.fetchall()
        for r in rec:
            # piątek
            tk.Label(self.root, text=str(r[1]), font=(
                "Ariel", 10), fg=kolor_piatek, bg="black").place(x=x_planLekcji, y=y_planLekcji)
            tk.Label(self.root, text=str(i)+". "+str(r[2])+" - "+str(r[3]+"  "+str(r[4])), font=(
                "Arial", 11), fg=kolor_piatek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[5])+" - "+str(r[6]+"  "+str(r[7])), font=(
                "Arial", 11), fg=kolor_piatek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[8])+" - "+str(r[9]+"  "+str(r[10])), font=(
                "Arial", 11), fg=kolor_piatek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[11])+" - "+str(r[12]+"  "+str(r[13])), font=(
                "Arial", 11), fg=kolor_piatek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[14])+" - "+str(r[15]+"  "+str(r[16])), font=(
                "Arial", 11), fg=kolor_piatek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[17])+" - "+str(r[18]+"  "+str(r[19])), font=(
                "Arial", 11), fg=kolor_piatek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[20])+" - "+str(r[21]+"  "+str(r[22])), font=(
                "Arial", 11), fg=kolor_piatek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[23])+" - "+str(r[24]+"  "+str(r[25])), font=(
                "Arial", 11), fg=kolor_piatek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
            i += 1
            y_planLekcji += 25
            tk.Label(self.root, text=str(i)+". "+str(r[26])+" - "+str(r[27]+"  "+str(r[28])), font=(
                "Arial", 11), fg=kolor_piatek, bg="black").place(x=x_planLekcji, y=y_planLekcji+30)
        conn.close()

# ---------------------------------------------Wyświetlenie przypomnień--------------------------------------------
    def Powiadomienia(self):
        x_powiadomienie= 30
        y_powiadomienie= 650
        dzien_powiad=strftime('%w')
        dzien = strftime('%e')
        dzien=int(dzien)
        dzien=str(dzien)
        miesiac_r = strftime('%m')
        miesiac_r=str(miesiac_r)
        if miesiac_r=="01":
            miesiac_r="Styczeń"
        elif miesiac_r=="02":
            miesiac_r="Luty"
        elif miesiac_r=="03":
            miesiac_r="Marzec"
        elif miesiac_r=="04":
            miesiac_r="Kwiecień"
        elif miesiac_r=="05":
            miesiac_r="Maj"
        elif miesiac_r=="06":
            miesiac_r="Czerwiec"
        elif miesiac_r=="07":
            miesiac_r="Lipiec"
        elif miesiac_r=="08":
            miesiac_r="Sierpień"
        elif miesiac_r=="09":
            miesiac_r="Wrzesień"
        elif miesiac_r=="10":
            miesiac_r="Październik"
        elif miesiac_r=="11":
            miesiac_r="Listopad"
        elif miesiac_r=="12":
            miesiac_r="Grudzień"
            
        tk.Label(self.root, text="Dziś:", font=("Arial", 16), fg="Blue", bg="black").place(x=30, y=620)
        
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        if dzien_powiad=="1":
            c.execute('SELECT * , oid FROM przypomnij WHERE dzien_tygodnia="Poniedziałek"')
            reco = c.fetchall()
            for a in reco:
                tk.Label(self.root, text=str(a[1]+"   "+str(a[4])),font=("Arial", 13), fg="blue", bg="black").place(x=x_powiadomienie, y=y_powiadomienie)
                y_powiadomienie+=30
        elif dzien_powiad=="2":
            c.execute('SELECT * , oid FROM przypomnij WHERE dzien_tygodnia="Wtorek"')
            reco = c.fetchall()
            for a in reco:
                tk.Label(self.root, text=str(a[1]+"   "+str(a[4])),font=("Arial", 13), fg="blue", bg="black").place(x=x_powiadomienie, y=y_powiadomienie)
                y_powiadomienie+=30
        elif dzien_powiad=="3":
            c.execute('SELECT * , oid FROM przypomnij WHERE dzien_tygodnia="Środa"')
            reco = c.fetchall()
            for a in reco:
                tk.Label(self.root, text=str(a[1]+"   "+str(a[4])),font=("Arial", 13), fg="blue", bg="black").place(x=x_powiadomienie, y=y_powiadomienie)
                y_powiadomienie+=30
        elif dzien_powiad=="4":
            c.execute('SELECT * , oid FROM przypomnij WHERE dzien_tygodnia="Czwartek"')
            reco = c.fetchall()
            for a in reco:
                tk.Label(self.root, text=str(a[1]+"   "+str(a[4])),font=("Arial", 13), fg="blue", bg="black").place(x=x_powiadomienie, y=y_powiadomienie)
                y_powiadomienie+=30
        elif dzien_powiad=="5":
            c.execute('SELECT * , oid FROM przypomnij WHERE dzien_tygodnia="Piątek"')
            reco = c.fetchall()
            for a in reco:
                tk.Label(self.root, text=str(a[1]+"   "+str(a[4])),font=("Arial", 13), fg="blue", bg="black").place(x=x_powiadomienie, y=y_powiadomienie)
                y_powiadomienie+=30
        elif dzien_powiad=="6":
            c.execute('SELECT * , oid FROM przypomnij WHERE dzien_tygodnia="Sobota"')
            reco = c.fetchall()
            for a in reco:
                tk.Label(self.root, text=str(a[1]+"   "+str(a[4])),font=("Arial", 13), fg="blue", bg="black").place(x=x_powiadomienie, y=y_powiadomienie)
                y_powiadomienie+=30
        elif dzien_powiad=="0":
            c.execute('SELECT * , oid FROM przypomnij WHERE dzien_tygodnia="Niedziela"')
            reco = c.fetchall()
            for a in reco:
                tk.Label(self.root, text=str(a[1]+"   "+str(a[4])),font=("Arial", 13), fg="blue", bg="black").place(x=x_powiadomienie, y=y_powiadomienie)
                y_powiadomienie+=30
        conn.close()

        x_poz=30
        y_poz=685
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        cz = conn.cursor()
        cz.execute('SELECT * , oid FROM przypomnij')
        re=cz.fetchall()
        for b in re:
            dana1=str(b[2])
            dana2=str(b[3])
            if dana1==dzien and dana2==miesiac_r:
                tk.Label(self.root, text=str(b[2])+" "+str(b[3])+"  "+str(b[4]), font=("Arial", 13), fg="#00FF00", bg="black").place(x=x_poz, y=y_poz)
                y_poz+=25
        conn.close()

# ----------------------------------Moduł daty------------------------------------
    def Data(self):
        dzien = strftime('%e')
        dzienTygodnia = strftime('%w')
        miesiac = strftime('%m')
        dzienRoku = strftime('%j')
        dzienRoku2 = int(dzienRoku)
        dzienRoku2 = 366-dzienRoku2
        dzienRoku2 = str(dzienRoku2)
        # ------- Przekształcenie dni --------
        if dzienTygodnia == "0":
            dzienTygodnia = "Niedziela"
            kolor1 = "red"
        elif dzienTygodnia == "1":
            dzienTygodnia = "Poniedziałek"
            kolor1 = "black"
        elif dzienTygodnia == "2":
            dzienTygodnia = "Wtorek"
            kolor1 = "black"
        elif dzienTygodnia == "3":
            dzienTygodnia = "Środa"
            kolor1 = "black"
        elif dzienTygodnia == "4":
            dzienTygodnia = "Czwartek"
            kolor1 = "black"
        elif dzienTygodnia == "5":
            dzienTygodnia = "Piątek"
            kolor1 = "black"
        elif dzienTygodnia == "6":
            dzienTygodnia = "Sobota"
            kolor1 = "black"
        # --------- Przekształcenie miesięcy -----------
        if miesiac == "01":
            miesiac = "Styczeń"
        elif miesiac == "02":
            miesiac = "Luty"
        elif miesiac == "03":
            miesiac = "Marzec"
        elif miesiac == "04":
            miesiac = "Kwiecień"
        elif miesiac == "05":
            miesiac = "Maj"
        elif miesiac == "06":
            miesiac = "Czerwiec"
        elif miesiac == "07":
            miesiac = "Lipiec"
        elif miesiac == "08":
            miesiac = "Sierpień"
        elif miesiac == "09":
            miesiac = "Wrzesień"
        elif miesiac == "10":
            miesiac = "Październik"
        elif miesiac == "11":
            miesiac = "Listopad"
        elif miesiac == "12":
            miesiac = "Grudzień"

        l1 = tk.Label(self.root, text=dzien, font=(
            "Arial", 60, "bold"), fg=kolor1, bg="white")
        l1.place(x=100, y=40)
        l2 = tk.Label(self.root, text=dzienTygodnia, font=(
            "Arial", 40, "bold"), fg=kolor1, bg="white")
        l2.place(x=40, y=120)
        l3 = tk.Label(self.root, text=miesiac, font=(
            "Arial", 30), fg="green", bg="black")
        l3.place(x=350, y=30)
        l4 = tk.Label(self.root, text=dzienRoku, font=(
            "Arial", 30), fg="#00FF00", bg="black")
        l4.place(x=590, y=30)
        l5 = tk.Label(self.root, text="dzień roku.", font=(
            "Ariel", 30), fg="green", bg="black")
        l5.place(x=680, y=30)
        l6 = tk.Label(self.root, text="Do końca roku pozostało",
                      font=("Arial", 30), fg="green", bg="black")
        l7 = tk.Label(self.root, text=dzienRoku2, font=(
            "Arial", 30), fg="#00FF00", bg="black")
        l8 = tk.Label(self.root, text="dni.", font=(
            "Arial", 30), fg="green", bg="black")
        l6.place(x=350, y=90)
        l7.place(x=830, y=90)
        l8.place(x=890, y=90)

# ------------------------------------------Moduł imienin---------------------------------------
    def imieniny(self):
        styczen = ["Mieszka, Mieczysława, Marii",
                   "Izydora, Bazylego, Grzegorza",
                   "Arlety, Genowefy, Danuty",
                   "Tytusa, Anieli, Eugeniusza",
                   "Hanny, Szymona, Edwarda",
                   "Kacpra, Melchiora, Baltazara", "Juliana, Lucjana, Rajmunda",
                   "Seweryna, M?cisława, Juliusza", "Marceliny, Marianny, Juliana",
                   "Wilhelma, Dobrosława, Danuty", "Honoraty, Teodozjusza, Matyldy",
                   "Grety, Arkadiusza, Rajmunda",
                   "Bogumiły, Weroniki, Hilarego",
                   "Feliksa, Domosława, Niny",
                   "Pawła, Arnolda, Izydora",
                   "Marcelego, Włodzimierza, Waldemara",
                   "Antoniego, Ro?cisława, Jana",
                   "Piotra, Małgorzaty",
                   "Henryka, Mariusza, Marty",
                   "Fabiana, Sebastiana",
                   "Agnieszki, Jarosława",
                   "Anastazego, Wincentego",
                   "Ildefonsa, Rajmunda",
                   "Felicji, Franciszka, Rafała",
                   "Pawła, Miłosza, Elwiry",
                   "Tymoteusza, Michała, Tytusa",
                   "Przybysława, Anieli, Jerzego",
                   "Walerego, Radomira, Tomasza",
                   "Zdzisława, Franciszka, Józefa",
                   "Macieja, Martyny, Teofila",
                   "Marceli, Ludwiki, Jana"]

        luty = ["Brygidy, Ignacego, Seweryna",
                "Marii, Miłosława",
                "Błażeja, Oskara",
                "Andrzeja, Weroniki, Joanny",
                "Agaty, Adelajdy",
                "Doroty, Bogdana, Pawła",
                "Ryszarda, Teodora, Romana",
                "Hieronima, Sebastiana, Ireny",
                "Apolonii, Eryki, Cyryla",
                "Elwiry, Jacka, Scholastyki",
                "Lucjana, Olgierda",
                "Eulalii, Radosława, Modesta",
                "Grzegorza, Katarzyny",
                "Cyryla, Metodego, Walentego",
                "Jowity, Faustyna, Zygfryda",
                "Danuty, Julianny, Daniela",
                "Aleksego, Zbigniewa, Lukasza",
                "Szymona, Konstancji, Flawiana",
                "Arnolda, Konrada, Marcelego",
                "Leona, Ludomira, Zenobiusza",
                "Eleonory, Fortunata, Roberta",
                "Marty, Małgorzaty, Piotra",
                "Romany, Damiana, Polikarpa",
                "Macieja, Bogusza, Sergiusza",
                "Wiktora, Cezarego",
                "Mirosława, Aleksandra",
                "Gabriela, Anastazji",
                "Romana, Ludomira, Lecha",
                "Lecha, Lutosława"]

        marzec = ["Antoniny, Radosława, Dawida",
                  "Heleny, Halszki, Pawła",
                  "Maryny, Kunegundy, Tycjana",
                  "Lucji, Kazimierza, Eugeniusza",
                  "Adriana, Fryderyka, Teofila",
                  "Róży, Jordana, Agnieszki",
                  "Tomasza, Perpetuy, Felicyty",
                  "Beaty, Wincentego, Jana",
                  "Franciszki, Brunona",
                  "Cypriana, Marcela, Aleksandra",
                  "Ludosława, Konstantyna, Benedykta",
                  "Grzegorza, Justyna, Alojzego",
                  "Bożeny, Krystyny",
                  "Leona, Matyldy, Łazarza",
                  "Longina, Klemensa, Ludwiki",
                  "Izabeli, Oktawii, Hilarego",
                  "Patryka, Zbigniewa, Gertrudy",
                  "Cyryla, Edwarda, Boguchwały",
                  "Józefa, Bogdana",
                  "Klaudii, Eufemii, Maurycego",
                  "Lubomira, Benedykta",
                  "Katarzyny, Bogusława",
                  "Pelagii, Oktawiana, Feliksa",
                  "Marka, Gabriela, Katarzyny",
                  "Marioli, Wieczysława, Ireneusza",
                  "Larysy, Emanyela, Teodora",
                  "Lidii, Ernesta",
                  "Anieli, Sykstusa, Jana",
                  "Wiktoryna, Helmuta, Eustachego",
                  "Anieli, Kwiryna, Leonarda",
                  "Beniamina, Dobromierza, Leonarda"]

        kwiecien = ["Teodory, Grażyny, Ireny",
                    "Władysława, Franciszka, Teodozji",
                    "Ryszarda, Pankracego, Ingi",
                    "Izydora, Wacława",
                    "Ireny, Wincentego",
                    "Izoldy, Celestyna, Wilhelma",
                    "Rufina, Celestyna, Jana",
                    "Cezaryny, Dionizego, Julii",
                    "Marii, Dymitra, Heliodora",
                    "Michała, Makarego",
                    "Filipa, Leona",
                    "Juliusza, Lubosława, Zenona",
                    "Przemysława, Hermenegildy, Marcina",
                    "Bereniki, Waleriana, Justyny",
                    "Ludwiny, Wacławy, Anastazji",
                    "Kseni, Cecylii, Bernardety",
                    "Rudolfa, Roberta",
                    "Bogusławy, Apoloniusza",
                    "Adolfa, Tymona, Leona",
                    "Czesława, Agnieszki, Mariana",
                    "Anzelma, Bartosza, Feliksa",
                    "Kai, Leonii, Sotera",
                    "Jerzego, Wojciecha",
                    "Horacego, Feliksa, Grzegorza",
                    "Marka, Jarosława, Wasyla",
                    "Marzeny, Klaudiusza, Marii",
                    "Zyty, Teofila, Felicji",
                    "Piotra, Walerii, Witalisa",
                    "Rity, Katarzyny, Bogusława",
                    "Mariana, Donaty, Tamary"]

        maj = ["Józefa, Jeremiasza, Filipa",
               "Zygmunta, Atanazego, Anatola",
               "Marii, Antoniny",
               "Moniki, Floriana, Władysława",
               "Ireny, Waldemara",
               "Judyty, Jakuba, Filipa",
               "Gizeli, Ludmiły, Benedykta",
               "Stanisława, Lizy, Wiktora",
               "Bożydara, Grzegorza, Karoliny",
               "Izydora, Antoniny, Symeona",
               "Igi, Miry, Władysławy",
               "Pankracego, Dominika, Achillesa",
               "Serwacego, Roberta, Glorii",
               "Bonifacego, Dobiesława, Macieja",
               "Zofii, Nadziei, Izydora",
               "Andrzeja, Jedrzeja, Szymona",
               "Paschalisa, Sławomira, Weroniki",
               "Eryka, Feliksa, Jana",
               "Iwa, Piotra, Celestyna",
               "Bazylego, Bernardyna, Aleksandra",
               "Wiktora, Kryspina, Tymoteusza",
               "Heleny, Wiesławy, Ryty",
               "Iwony, Dezyderego, Kryspina",
               "Joanny, Zuzanny",
               "Grzegorza, Urbana, Magdaleny",
               "Filipa, Pauliny",
               "Augustyna, Juliana, Magdaleny",
               "Jaromira, Justa, Justyny",
               "Magdaleny, Bogumiły, Urszuli",
               "Ferdynanda, Karola, Jana",
               "Anieli, Petroneli"]

        czerwiec = ["Justyna, Anieli, Konrada",
                    "Marianny, Marcelina, Piotra",
                    "Leszka, Tamary, Karola",
                    "Kwiryny, Franciszka",
                    "Waltera, Bonifacego, Walerii",
                    "Norberta, Laurentego, Bogumiła",
                    "Roberta, Wiesława",
                    "Medarda, Maksyma, Seweryna",
                    "Pelagii, Dominika, Efrema",
                    "Bogumiła, Małgorzaty, Diany",
                    "Barnaby, Radomiła, Feliksa",
                    "Janiny, Onufrego, Leona",
                    "Lucjana, Antoniego",
                    "Bazylego, Elwiry, Michała",
                    "Wita, Jolanty",
                    "Aliny, Benona, Anety",
                    "Laury, Marcjana, Alberta",
                    "Marka, Elżbiety",
                    "Gerwazego, Protazego",
                    "Diny, Bogny, Florentyny",
                    "Alicji, Alojzego",
                    "Pauliny, Tomasza, Jana",
                    "Wandy, Zenona",
                    "Jana, Danuty",
                    "Lucji, Wilhelma, Doroty",
                    "Jana, Pawła",
                    "Maryli, Władysława, Cyryla",
                    "Leona, Ireneusza",
                    "Piotra, Pawła",
                    "Emilii, Lucyny"]

        lipiec = ["Haliny, Mariana, Marcina",
                  "Jagody, Urbana, Marii",
                  "Jacka, Anatola, Tomasza",
                  "Odona, Malwiny, Elżbiety",
                  "Marii, Antoniego",
                  "Gotarda, Dominiki, Lucji",
                  "Cyryla, Estery, Metodego",
                  "Edgara, Elżbiety, Eugeniusza",
                  "Lukrecji, Weroniki, Zenona",
                  "Sylwany, Witalisa, Antoniego",
                  "Olgi, Kaliny, Benedykta",
                  "Jana, Brunona, Bonifacego",
                  "Henryka, Kingi, Andrzeja",
                  "Ulryka, Bonawentury, Kamila",
                  "Henryka, Włodzimierza, Dawida",
                  "Mariki, Benity, Eustachego",
                  "Anety, Bogdana, Jadwigi",
                  "Erwina, Kamila, Szymona",
                  "Wincentego, Wodzisława, Marcina",
                  "Czesława, Hieronima, Małgorzaty",
                  "Daniela, Dalidy, Wawrzyńca",
                  "Marii, Magdaleny",
                  "Stwosza, Bogny, Brygidy",
                  "Kingi, Krystyny",
                  "Walentyny, Krzysztofa, Jakuba",
                  "Anny, Mirosławy, Grażyny",
                  "Lilii, Julii, Natalii",
                  "Aidy, Marceli, Wiktora",
                  "Olafa, Marty, Ludmiły",
                  "Julity, Piotra, Aldony",
                  "Ignacego, Lubomira, Heleny"]

        sierpien = ["Nadii, Justyna, Juliana",
                    "Kariny, Gustawa, Euzebiusza",
                    "Lidii, Augusta, Nikodema",
                    "Dominika, Protazego, Jana",
                    "Oswalda, Marii, Mariana",
                    "Sławy, Jakuba, Oktawiana",
                    "Kajetana, Doroty, Sykstusa",
                    "Cypriana, Emiliana, Dominika",
                    "Romana, Ryszarda, Edyty",
                    "Borysa, Filomeny, Wawrzyńca",
                    "Klary, Zuzanny, Lecha",
                    "Innocentego, Lecha, Euzebii",
                    "Diany, Hipolita, Poncjana",
                    "Alfreda, Euzebiusza, Maksymiliana",
                    "Napoleona, Stelii",
                    "Rocha, Stefana, Joachima",
                    "Żanny, Mirona, Jacka",
                    "Ilony, Bronisława, Heleny",
                    "Bolesława, Juliana",
                    "Bernarda, Samuela, Sobiesława",
                    "Joanny, Kazimiery, Piusa",
                    "Cezarego, Tymoteusza",
                    "Apolinarego, Filipa",
                    "Jerzego, Bartosza, Haliny",
                    "Luizy, Ludwika, Józefa",
                    "Marii, Aleksandra",
                    "Cezarego, Józefa, Moniki",
                    "Patrycji, Wyszomira, Augustyna",
                    "Beaty, Jana, Sabiny, Racibora",
                    "Róży, Szczęsnego, Feliksa",
                    "Bogdana, Ramony, Rajmunda"]

        wrzesien = ["Idziego, Bronisława, Melecjusza",
                    "Juliana, Stefana, Wilhelma",
                    "Grzegorza, Izabeli, Szymona",
                    "Idy, Julianny, Rozalii, Róży",
                    "Doroty, Teodora, Wawrzyńca",
                    "Beaty, Eugeniusza",
                    "Domosławy, Melchiora, Reginy",
                    "Marii, Adrianny, Serafiny",
                    "?cibora, Sergiusza, Piotra",
                    "Lukasza, Aldony, M?cisława",
                    "Jacka, Prota, Dagny, Hiacynta",
                    "Gwidona, Radzimira, Marii",
                    "Eugenii, Aureliusza, Jana",
                    "Roksany, Bernarda, Cypriana",
                    "Albina, Nikodema, Marii",
                    "Edyty, Korneliusza, Cypriana",
                    "Franciszka, Roberta, Justyna",
                    "Irmy, Stanisława, Ireny",
                    "Januarego, Konstancji, Teodora",
                    "Filipiny, Eustachego, Euzebii",
                    "Jonasza, Mateusza, Hipolita",
                    "Tomasza, Maurycego, Joachima",
                    "Tekli, Bogusława, Linusa",
                    "Gerarda, Ruperta, Tomiry",
                    "Aurelii, Władysława, Kleofasa",
                    "Wawrzyńca, Kosmy, Damiana",
                    "Wincentego, Mirabeli, Justyny",
                    "Wacława, Tymona, Marka",
                    "Michała, Gabriela, Rafała",
                    "Wery, Honoriusza, Hieronima"]

        pazdziernik = ["Danuty, Remigiusza, Teresy",
                       "Teofila, Dionizego, Sławomira",
                       "Teresy, Heliodora, Jana",
                       "Rozalii, Edwina, Franciszka",
                       "Placyda, Apolinarego",
                       "Artura, Brunona",
                       "Marii, Marka, Mirelli",
                       "Pelagii, Brygidy, Walerii",
                       "Amolda, Dionizego, Wincentego",
                       "Pauliny, Danieli, Leona",
                       "Aldony, Aleksandra, Dobromiry",
                       "Eustachego, Maksymiliana, Edwina",
                       "Geralda, Edwarda, Honorata",
                       "Liwii, Kaliksta, Bernarda",
                       "Jadwigi, Teresy, Florentyny",
                       "Gawła, Ambrożego",
                       "Wiktora, Marity, Ignacego",
                       "Juliana, Łukasza",
                       "Ziemowita, Jana, Pawła",
                       "Ireny, Kleopatry, Jana",
                       "Urszuli, Hilarego, Jakuba",
                       "Halki, Filipa, Salomei",
                       "Marleny, Seweryna, Igi",
                       "Rafała, Marcina, Antoniego",
                       "Darii, Wilhelminy, Bonifacego",
                       "Lucjana, Ewarysta, Damiana",
                       "Iwony, Sabiny",
                       "Szymona, Tadeusza",
                       "Euzebii, Wioletty, Felicjana",
                       "Zenobii, Przemysława, Edmunda",
                       "Urbana, Saturnina, Krzysztofa"]

        listopad = ["Bohdany, Bożydara",
                    "Sylwii, Marcina, Huberta",
                    "Karola, Olgierda",
                    "Elżbiety, Sławomira, Dominika",
                    "Feliksa, Leonarda, Ziemowita",
                    "Antoniego, Żytomira, Ernesta",
                    "Seweryna, Bogdana, Klaudiusza",
                    "Aleksandra, Ludwika, Teodora",
                    "Leny, Ludomira, Leona",
                    "Marcina, Batłomieja, Teodora",
                    "Renaty, Witolda, Jozafata",
                    "Mateusza, Izaaka, Stanisława",
                    "Rogera, Serafina, Wawrzyńca",
                    "Alberta, Leopolda",
                    "Gertrudy, Edmunda, Marii",
                    "Salomei, Grzegorza, Elżbiety",
                    "Romana, Klaudyny, Karoliny",
                    "Seweryny, Maksyma, Salomei",
                    "Anatola, Sedzimira, Rafała",
                    "Alberta, Janusza, Konrada",
                    "Cecylii, Wszemiły, Stefana",
                    "Adelii, Klemensa, Felicyty",
                    "Flory, Emmy, Chryzogona",
                    "Erazma, Katarzyny",
                    "Delfiny, Sylwestra, Konrada",
                    "Waleriana, Wirgiliusza, Maksyma",
                    "Lesława, Zdzisława, Stefana",
                    "Błażeja, Saturnina",
                    "Andrzeja, Maury, Konstantego"]

        grudzien = ["Natalii, Eligiusza, Edmunda",
                    "Balbiny, Bibianny, Pauliny",
                    "Franciszka, Ksawerego, Kasjana",
                    "Barbary, Krystiana, Jana",
                    "Sabiny, Krystyny, Edyty",
                    "Mikołaja, Jaremy, Emiliana",
                    "Marcina, Ambrożego, Teodora",
                    "Marii, ?wiatozara, Makarego",
                    "Wiesława Leokadii Joanny",
                    "Julii, Danieli, Bogdana",
                    "Damazego, Waldemara, Daniela",
                    "Dagmary, Aleksandra, Ady",
                    "Lucji, Otylii",
                    "Alfreda, Izydora, Jana",
                    "Niny, Celiny, Waleriana",
                    "Albiny, Zdzisławy, Alicji",
                    "Olimpii, Lazarza, Floriana",
                    "Gracjana, Bogusława, Laurencji",
                    "Gabrieli, Dariusza, Eleonory",
                    "Bogumiły, Dominika",
                    "Tomisława, Seweryna, Piotra",
                    "Zenona, Honoraty, Franciszki",
                    "Wiktorii, Sławomiry, Jana",
                    "Adama, Ewy, Eweliny",
                    "Anastazji, Eugenii",
                    "Dionizego, Szczepana",
                    "Jana, Żanety, Maksyma",
                    "Teofilii, Godzisława, Cezarego",
                    "Dawida, Tomasza, Dominika",
                    "Rainera, Eugeniusza, Irmy",
                    "Sylwestra, Melanii, Mariusza"]
        # *** zmiana na wartości w tablicach ***
        dzienMiesiaca = strftime('%d')
        if dzienMiesiaca == "01":
            x = 0
        elif dzienMiesiaca == "02":
            x = 1
        elif dzienMiesiaca == "03":
            x = 2
        elif dzienMiesiaca == "04":
            x = 3
        elif dzienMiesiaca == "05":
            x = 4
        elif dzienMiesiaca == "06":
            x = 5
        elif dzienMiesiaca == "07":
            x = 6
        elif dzienMiesiaca == "08":
            x = 7
        elif dzienMiesiaca == "09":
            x = 8
        elif dzienMiesiaca == "10":
            x = 9
        elif dzienMiesiaca == "11":
            x = 10
        elif dzienMiesiaca == "12":
            x = 11
        elif dzienMiesiaca == "13":
            x = 12
        elif dzienMiesiaca == "14":
            x = 13
        elif dzienMiesiaca == "15":
            x = 14
        elif dzienMiesiaca == "16":
            x = 15
        elif dzienMiesiaca == "17":
            x = 16
        elif dzienMiesiaca == "18":
            x = 17
        elif dzienMiesiaca == "19":
            x = 18
        elif dzienMiesiaca == "20":
            x = 19
        elif dzienMiesiaca == "21":
            x = 20
        elif dzienMiesiaca == "22":
            x = 21
        elif dzienMiesiaca == "23":
            x = 22
        elif dzienMiesiaca == "24":
            x = 23
        elif dzienMiesiaca == "25":
            x = 24
        elif dzienMiesiaca == "26":
            x = 25
        elif dzienMiesiaca == "27":
            x = 26
        elif dzienMiesiaca == "28":
            x = 27
        elif dzienMiesiaca == "29":
            x = 28
        elif dzienMiesiaca == "30":
            x = 29
        elif dzienMiesiaca == "31":
            x = 30
        else:
            print("Prawdopodobnie Masz żle ustawioną datę!")
            print("Twój czas to: ", strftime('%c'))

        # *** przypisanie do nazwy tablic według miesięcy ***
        x_x = 350  # położenie imienin x
        y_y = 170  # połozenie imenin y
        font_x = 25  # wielkość fontu
        miesiac = strftime('%m')
        if miesiac == "01":
            linia = tk.Label(self.root, text="Imieniny:  " +
                             styczen[x], font=("Times", font_x), fg="#00FFFF", bg="black")
            linia.place(x=x_x, y=y_y)
        elif miesiac == "02":
            linia = tk.Label(self.root, text="Imieniny:  " +
                             luty[x], font=("Times", font_x), fg="#00FFFF", bg="black")
            linia.place(x=x_x, y=y_y)
        elif miesiac == "03":
            linia = tk.Label(self.root, text="Imieniny:  " +
                             marzec[x], font=("Times", font_x), fg="#00FFFF", bg="black")
            linia.place(x=x_x, y=y_y)
        elif miesiac == "04":
            linia = tk.Label(self.root, text="Imieniny:  " +
                             kwiecien[x], font=("Times", font_x), fg="#00FFFF", bg="black")
            linia.place(x=x_x, y=y_y)
        elif miesiac == "05":
            linia = tk.Label(self.root, text="Imieniny:  " +
                             maj[x], font=("Times", font_x), fg="#00FFFF", bg="black")
            linia.place(x=x_x, y=y_y)
        elif miesiac == "06":
            linia = tk.Label(self.root, text="Imieniny:  " +
                             czerwiec[x], font=("Times", font_x), fg="#00FFFF", bg="black")
            linia.place(x=x_x, y=y_y)
        elif miesiac == "07":
            linia = tk.Label(self.root, text="Imieniny:  " +
                             lipiec[x], font=("Times", font_x), fg="#00FFFF", bg="black")
            linia.place(x=x_x, y=y_y)
        elif miesiac == "08":
            linia = tk.Label(self.root, text="Imieniny:  " +
                             sierpien[x], font=("Times", font_x), fg="#00FFFF", bg="black")
            linia.place(x=x_x, y=y_y)
        elif miesiac == "09":
            linia.tk.Label(self.root, text="Imieniny:  " +
                           wrzesien[x], font=("Times", font_x), fg="#00FFFF", bg="black")
            linia.place(x=x_x, y=y_y)
        elif miesiac == "10":
            linia = tk.Label(self.root, text="Imieniny:  " +
                             pazdziernik[x], font=("Times", font_x), fg="#00FFFF", bg="black")
            linia.place(x=x_x, y=y_y)
        elif miesiac == "11":
            linia = tk.Label(self.root, text="Imieniny:  " +
                             listopad[x], font=("Times", font_x), fg="#00FFFF", bg="black")
            linia.place(x=x_x, y=y_y)
        elif miesiac == "12":
            linia = tk.Label(self.root, text="Imieniny:  " +
                             grudzien[x], font=("Times", font_x), fg="#00FFFF", bg="black")
            linia.place(x=x_x, y=y_y)

# ----------------------------------Moduł dodaj przypomnienie-----------------------------
    def dodajPrzypomnienie(self):
        top = Toplevel()
        top.geometry("800x600")
        top.title("Dodaj nowe przypomnienie")
        t1 = tk.Label(top, text="Dzień tygodnia", font=("Arial", 13))
        t2 = tk.Label(top, text="Dzień miesiąca", font=("Arial", 13))
        t3 = tk.Label(top, text="Miesiąc", font=("Arial", 13))
        t4 = tk.Label(top, text="Treść przypomnienia", font=("Arial", 13))
        t1.place(x=100, y=30)
        t2.place(x=340, y=30)
        t3.place(x=600, y=30)
        t4.place(x=30, y=200)
        self.dzienMiesiaca = tk.StringVar()
        self.miesiac = tk.StringVar()
        self.dzienTygodnia = tk.StringVar()
        self.trescPrzypomnienia = tk.StringVar()
        # pobieranie dziennego przypomnienia
        spin1 = tk.Spinbox(
            top, from_=1, to=31, textvariable=self.dzienMiesiaca, width=3, font=("arial", 15))
        spin1.place(x=380, y=60)
        # pobieranie tygodniowego przypomnienia
        linia1e = ttk.Combobox(
            top, textvariable=self.dzienTygodnia, font=("arial", 15))
        linia1e['values'] = ("", "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek",
                             "Sobota", "Niedziela")
        linia1e.current(0)
        linia1e.place(x=50, y=60)
        # pobieranie corocznego przypomnienia
        linia2e = ttk.Combobox(
            top, textvariable=self.miesiac, font=("arial", 15))
        linia2e['values'] = ("", "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
                             "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień")
        linia2e.current(0)
        linia2e.place(x=520, y=60)
        # pobieranie treści przypomnienia
        e1 = tk.Entry(top, textvariable=self.trescPrzypomnienia,
                      font=("arial", 15), width=70)
        e1.place(x=12, y=240)
        # przycisk -----zapisz przypomnienie-----
        b1 = tk.Button(top, text="Zapisz przypomnienie", font=(
            "Arial", 13), fg="red", command=lambda: self.Zapisz_przypomnienie(top))
        b1.place(x=330, y=300)

# -----------------------------Moduł usuwania przypomnienia--------------------------------
    def UsunPrzypomnienie(self):
        top = tk.Toplevel()
        top.geometry("800x600")
        top.title("Usuń rekord z przypomnieniem")
        # textbox przypomnień godzinowych
        sb_textbox = tk.Scrollbar(top)
        textbox = tk.Text(top, width=90, height=20,
                          yscrollcommand=sb_textbox.set)
        textbox.place(x=30, y=10)
        sb_textbox.place(in_=textbox, relx=1., rely=0, relheight=1.)
        textbox.place(x=30, y=10)
        textbox.insert(tk.END, "Baza przypomnień godzinowych: ", ("h2"))
        textbox.insert(tk.END, "\n\n")
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        c.execute('SELECT * , oid FROM przypomnij ORDER BY id DESC')
        rec = c.fetchall()
        for r in rec:
            textbox.insert(tk.END, str(
                r[0])+"""  """+str(r[1])+"""  """+str(r[2])+"""  """+str(r[3])+"""   """+str(r[4])+"""\n""", ("p"))
        textbox.tag_add("h1", "1.0", "1.0")
        textbox.tag_config("h1", font=("Times New Roman", 20))
        textbox.tag_add("p", "1.0", "1.0")
        textbox.tag_config("p", foreground="#808080")
        sb_textbox.config(command=textbox.yview)
        conn.close()
        linia_usun = tk.Label(
            top, text="Podaj index rekordu do usunięcia", font=("Ariel", 13), fg="green")
        linia_usun.place(x=20, y=400)
        self.rekordDoUsuniecia = StringVar()
        entry_usun = tk.Entry(
            top, textvariable=self.rekordDoUsuniecia, font=("Arial", 13), width=3)
        entry_usun.place(x=330, y=400)
        button_usun = tk.Button(top, text="Usuń rekord", font=(
            "Arial", 11), fg="red", command=lambda: self.UsunRekord(top))
        button_usun.place(x=400, y=400)

# ---------------------------------Moduł dodawania lekcji---------------------------------
    def DodajPlanLekcji(self):
        top = tk.Toplevel()
        top.geometry("800x600")
        top.title("Dodal lekcje do planu")

        l_p0 = tk.Label(top, text="Dzień tygodnia", font=("Arial", 13))
        # pierwsza lekcja
        l_p1 = tk.Label(top, text="godz rozpoczęcia", font=("Arial", 13))
        l_p2 = tk.Label(top, text="godz zakończenia", font=("Arial", 13))
        l_p3 = tk.Label(top, text="lekcja 1", font=("Arial", 13))
        # druga lekcja
        l_p4 = tk.Label(top, text="godz rozpoczęcia", font=("Arial", 13))
        l_p5 = tk.Label(top, text="godz zakończenia", font=("Arial", 13))
        l_p6 = tk.Label(top, text="lekcja 2", font=("Arial", 13))
        # trzecia lekcja
        l_p7 = tk.Label(top, text="godz rozpoczęcia", font=("Arial", 13))
        l_p8 = tk.Label(top, text="godz zakończenia", font=("Arial", 13))
        l_p9 = tk.Label(top, text="lekcja 3", font=("Arial", 13))
        # czwarta lekcja
        l_p10 = tk.Label(top, text="godz rozpoczęcia", font=("Arial", 13))
        l_p11 = tk.Label(top, text="godz zakończenia", font=("Arial", 13))
        l_p12 = tk.Label(top, text="lekcja 4", font=("Arial", 13))
        # piąta lekcja
        l_p13 = tk.Label(top, text="godz rozpoczęcia", font=("Arial", 13))
        l_p14 = tk.Label(top, text="godz zakończenia", font=("Arial", 13))
        l_p15 = tk.Label(top, text="lekcja 5", font=("Arial", 13))
        # szósta lekcja
        l_p16 = tk.Label(top, text="godz rozpoczęcia", font=("Arial", 13))
        l_p17 = tk.Label(top, text="godz zakończenia", font=("Arial", 13))
        l_p18 = tk.Label(top, text="lekcja 6", font=("Arial", 13))
        # siódma lekcja
        l_p19 = tk.Label(top, text="godz rozpoczęcia", font=("Arial", 13))
        l_p20 = tk.Label(top, text="godz zakończenia", font=("Arial", 13))
        l_p21 = tk.Label(top, text="lekcja 7", font=("Arial", 13))
        # ósma lekcja
        l_p22 = tk.Label(top, text="godz rozpoczęcia", font=("Arial", 13))
        l_p23 = tk.Label(top, text="godz zakończenia", font=("Arial", 13))
        l_p24 = tk.Label(top, text="lekcja 8", font=("Arial", 13))
        # dodatkowa lekcja
        l_p25 = tk.Label(top, text="godz rozpoczęcia", font=("Arial", 13))
        l_p26 = tk.Label(top, text="godz zakończenia", font=("Arial", 13))
        l_p27 = tk.Label(top, text="dodatkowa", font=("Arial", 13))

        l_p0.place(x=10, y=10)
        l_p1.place(x=10, y=40)
        l_p2.place(x=250, y=40)
        l_p3.place(x=500, y=40)

        l_p4.place(x=10, y=70)
        l_p5.place(x=250, y=70)
        l_p6.place(x=500, y=70)

        l_p7.place(x=10, y=100)
        l_p8.place(x=250, y=100)
        l_p9.place(x=500, y=100)

        l_p10.place(x=10, y=130)
        l_p11.place(x=250, y=130)
        l_p12.place(x=500, y=130)

        l_p13.place(x=10, y=160)
        l_p14.place(x=250, y=160)
        l_p15.place(x=500, y=160)

        l_p16.place(x=10, y=190)
        l_p17.place(x=250, y=190)
        l_p18.place(x=500, y=190)

        l_p19.place(x=10, y=220)
        l_p20.place(x=250, y=220)
        l_p21.place(x=500, y=220)

        l_p22.place(x=10, y=250)
        l_p23.place(x=250, y=250)
        l_p24.place(x=500, y=250)

        l_p25.place(x=10, y=300)
        l_p26.place(x=250, y=300)
        l_p27.place(x=500, y=300)
        self.dzien = tk.StringVar()
        self.godz_rozpoczecia_1 = tk.StringVar()
        self.godz_zakonczenia_1 = tk.StringVar()
        self.lekcja_1 = tk.StringVar()

        self.godz_rozpoczecia_2 = tk.StringVar()
        self.godz_zakonczenia_2 = tk.StringVar()
        self.lekcja_2 = tk.StringVar()

        self.godz_rozpoczecia_3 = tk.StringVar()
        self.godz_zakonczenia_3 = tk.StringVar()
        self.lekcja_3 = tk.StringVar()

        self.godz_rozpoczecia_4 = tk.StringVar()
        self.godz_zakonczenia_4 = tk.StringVar()
        self.lekcja_4 = tk.StringVar()

        self.godz_rozpoczecia_5 = tk.StringVar()
        self.godz_zakonczenia_5 = tk.StringVar()
        self.lekcja_5 = tk.StringVar()

        self.godz_rozpoczecia_6 = tk.StringVar()
        self.godz_zakonczenia_6 = tk.StringVar()
        self.lekcja_6 = tk.StringVar()

        self.godz_rozpoczecia_7 = tk.StringVar()
        self.godz_zakonczenia_7 = tk.StringVar()
        self.lekcja_7 = tk.StringVar()

        self.godz_rozpoczecia_8 = tk.StringVar()
        self.godz_zakonczenia_8 = tk.StringVar()
        self.lekcja_8 = tk.StringVar()

        self.godz_rozpoczecia_9 = tk.StringVar()
        self.godz_zakonczenia_9 = tk.StringVar()
        self.lekcja_9 = tk.StringVar()

        linia2d = ttk.Combobox(
            top, textvariable=self.dzien, font=("arial", 13))
        linia2d['values'] = ("Poniedziałek", "Wtorek", "Środa",
                             "Czwartek", "Piątek")
        linia2d.current(0)
        linia2d.place(x=170, y=10)

        l_entry1 = tk.Entry(
            top, textvariable=self.godz_rozpoczecia_1, font=("Arial", 13), width=6)
        l_entry2 = tk.Entry(
            top, textvariable=self.godz_zakonczenia_1, font=("Arial", 13), width=6)
        l_entry3 = tk.Entry(top, textvariable=self.lekcja_1,
                            font=("Arial", 13), width=20)

        l_entry4 = tk.Entry(
            top, textvariable=self.godz_rozpoczecia_2, font=("Arial", 13), width=6)
        l_entry5 = tk.Entry(
            top, textvariable=self.godz_zakonczenia_2, font=("Arial", 13), width=6)
        l_entry6 = tk.Entry(top, textvariable=self.lekcja_2,
                            font=("Arial", 13), width=20)

        l_entry7 = tk.Entry(
            top, textvariable=self.godz_rozpoczecia_3, font=("Arial", 13), width=6)
        l_entry8 = tk.Entry(
            top, textvariable=self.godz_zakonczenia_3, font=("Arial", 13), width=6)
        l_entry9 = tk.Entry(top, textvariable=self.lekcja_3,
                            font=("Arial", 13), width=20)

        l_entry10 = tk.Entry(
            top, textvariable=self.godz_rozpoczecia_4, font=("Arial", 13), width=6)
        l_entry11 = tk.Entry(
            top, textvariable=self.godz_zakonczenia_4, font=("Arial", 13), width=6)
        l_entry12 = tk.Entry(top, textvariable=self.lekcja_4,
                             font=("Arial", 13), width=20)

        l_entry13 = tk.Entry(
            top, textvariable=self.godz_rozpoczecia_5, font=("Arial", 13), width=6)
        l_entry14 = tk.Entry(
            top, textvariable=self.godz_zakonczenia_5, font=("Arial", 13), width=6)
        l_entry15 = tk.Entry(top, textvariable=self.lekcja_5,
                             font=("Arial", 13), width=20)

        l_entry16 = tk.Entry(
            top, textvariable=self.godz_rozpoczecia_6, font=("Arial", 13), width=6)
        l_entry17 = tk.Entry(
            top, textvariable=self.godz_zakonczenia_6, font=("Arial", 13), width=6)
        l_entry18 = tk.Entry(top, textvariable=self.lekcja_6,
                             font=("Arial", 13), width=20)

        l_entry19 = tk.Entry(
            top, textvariable=self.godz_rozpoczecia_7, font=("Arial", 13), width=6)
        l_entry20 = tk.Entry(
            top, textvariable=self.godz_zakonczenia_7, font=("Arial", 13), width=6)
        l_entry21 = tk.Entry(top, textvariable=self.lekcja_7,
                             font=("Arial", 13), width=20)

        l_entry22 = tk.Entry(
            top, textvariable=self.godz_rozpoczecia_8, font=("Arial", 13), width=6)
        l_entry23 = tk.Entry(
            top, textvariable=self.godz_zakonczenia_8, font=("Arial", 13), width=6)
        l_entry24 = tk.Entry(top, textvariable=self.lekcja_8,
                             font=("Arial", 13), width=20)

        l_entry25 = tk.Entry(
            top, textvariable=self.godz_rozpoczecia_9, font=("Arial", 13), width=6)
        l_entry26 = tk.Entry(
            top, textvariable=self.godz_zakonczenia_9, font=("Arial", 13), width=6)
        l_entry27 = tk.Entry(top, textvariable=self.lekcja_9,
                             font=("Arial", 13), width=18)

        l_entry1.place(x=170, y=40)
        l_entry2.place(x=420, y=40)
        l_entry3.place(x=580, y=40)

        l_entry4.place(x=170, y=70)
        l_entry5.place(x=420, y=70)
        l_entry6.place(x=580, y=70)

        l_entry7.place(x=170, y=100)
        l_entry8.place(x=420, y=100)
        l_entry9.place(x=580, y=100)

        l_entry10.place(x=170, y=130)
        l_entry11.place(x=420, y=130)
        l_entry12.place(x=580, y=130)

        l_entry13.place(x=170, y=160)
        l_entry14.place(x=420, y=160)
        l_entry15.place(x=580, y=160)

        l_entry16.place(x=170, y=190)
        l_entry17.place(x=420, y=190)
        l_entry18.place(x=580, y=190)

        l_entry19.place(x=170, y=220)
        l_entry20.place(x=420, y=220)
        l_entry21.place(x=580, y=220)

        l_entry22.place(x=170, y=250)
        l_entry23.place(x=420, y=250)
        l_entry24.place(x=580, y=250)

        l_entry25.place(x=170, y=300)
        l_entry26.place(x=420, y=300)
        l_entry27.place(x=600, y=300)

        l_button = tk.Button(top, text="Zapisz lekcje", font=(
            "Arial", 13), fg="red", command=lambda: self.ZapiszPlanLekcji(top))
        l_button.place(x=345, y=370)

# ---------------------------------Moduł usuwania lekcji----------------------------------
    def UsuwaniePlanuLekcji(self):
        top = tk.Toplevel()
        top.geometry("800x600")
        top.title("Usuń rekord z lekcjami")
        # textbox przypomnień godzinowych
        sb_textbox = tk.Scrollbar(top)
        textbox = tk.Text(top, width=40, height=33,
                          yscrollcommand=sb_textbox.set)
        textbox.place(x=30, y=10)
        sb_textbox.place(in_=textbox, relx=1., rely=0, relheight=1.)
        textbox.place(x=30, y=10)
        textbox.insert(tk.END, "Baza lekcji: ", ("h2"))
        textbox.insert(tk.END, "\n\n")
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        c.execute('SELECT * , oid FROM plan_lekcji')
        rec = c.fetchall()
        for r in rec:
            textbox.insert(tk.END, """   """+str(r[0])+"""\n""", ("h3"))
            textbox.insert(tk.END, str(r[1])+"""\n"""+str(r[2])+""" - """+str(r[3])+"""    """+str(r[4]) +
                           """\n"""+str(r[5])+""" - """+str(r[6])+"""    """+str(r[7]) +
                           """\n"""+str(r[8])+""" - """+str(r[9])+"""    """+str(r[10]) +
                           """\n"""+str(r[11])+""" - """+str(r[12])+"""    """+str(r[13]) +
                           """\n"""+str(r[14])+""" - """+str(r[15])+"""    """+str(r[16]) +
                           """\n"""+str(r[17])+""" - """+str(r[18])+"""    """+str(r[19]) +
                           """\n"""+str(r[20])+""" - """+str(r[21])+"""    """+str(r[22]) +
                           """\n"""+str(r[23])+""" - """+str(r[24])+"""    """+str(r[25]) +
                           """\n"""+str(r[26])+""" - """+str(r[27])+"""    """+str(r[28])+"""\n\n""", ("p"))
        textbox.tag_add("h2", "1.0", "1.0")
        textbox.tag_config("h2", font=("Times New Roman", 20))
        textbox.tag_add("h3", "1.0", "1.0")
        textbox.tag_config("h3", font=(
            "Times New Roman", 15), foreground="red")
        textbox.tag_add("p", "1.0", "1.0")
        textbox.tag_config("p", foreground="#808080")
        sb_textbox.config(command=textbox.yview)
        conn.close()
        ulek = tk.Label(top, text="Wybierz index do usunięcia",
                        font=("Ariel", 13), fg="green")
        ulek.place(x=400, y=50)
        self.usunRekordLekcje = tk.StringVar()
        ulek_1 = tk.Entry(top, textvariable=self.usunRekordLekcje,
                          font=("Arial", 13), width=3)
        ulek_1.place(x=650, y=50)
        ulek_button = tk.Button(
            top, text="usuń", fg="red", command=lambda: self.UsunLekcje(top))
        ulek_button.place(x=700, y=50)


# ---------------------------------definicje zapisu---------------------------------------

    def Zapisz_przypomnienie(self, x):
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        c.execute("INSERT INTO przypomnij VALUES (NULL, :dzien_tygodnia, :dzien_miesiaca, :miesiac, :tresc_przypomnienia)",
                  {
                      'dzien_tygodnia': self.dzienTygodnia.get(),
                      'dzien_miesiaca': self.dzienMiesiaca.get(),
                      'miesiac': self.miesiac.get(),
                      'tresc_przypomnienia': self.trescPrzypomnienia.get()
                  })
        conn.commit()
        conn.close()
        x.destroy()

# ---------------------------------definicja zapisu planu lekcji-----------------------------------------
    def ZapiszPlanLekcji(self, x):
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        c.execute("INSERT INTO plan_lekcji Values (NULL, :dzien, :g_rozpoczecia_1, :g_zakonczenia_1, :przedmiot_1, :g_rozpoczecia_2, :g_zakonczenia_2, :przedmiot_2, :g_rozpoczecia_3, :g_zakonczenia_3, :przedmiot_3,:g_rozpoczecia_4, :g_zakonczenia_4, :przedmiot_4, :g_rozpoczecia_5, :g_zakonczenia_5, :przedmiot_5, :g_rozpoczecia_6, :g_zakonczenia_6, :przedmiot_6, :g_rozpoczecia_7, :g_zakonczenia_7, :przedmiot_7, :g_rozpoczecia_8, :g_zakonczenia_8, :przedmiot_8,:g_rozpoczecia_9, :g_zakonczenia_9, :przedmiot_9)",
                  {
                      'dzien': self.dzien.get(),
                      'g_rozpoczecia_1': self.godz_rozpoczecia_1.get(),
                      'g_zakonczenia_1': self.godz_zakonczenia_1.get(),
                      'przedmiot_1': self.lekcja_1.get(),
                      'g_rozpoczecia_2': self.godz_rozpoczecia_2.get(),
                      'g_zakonczenia_2': self.godz_zakonczenia_2.get(),
                      'przedmiot_2': self.lekcja_2.get(),
                      'g_rozpoczecia_3': self.godz_rozpoczecia_3.get(),
                      'g_zakonczenia_3': self.godz_zakonczenia_3.get(),
                      'przedmiot_3': self.lekcja_3.get(),
                      'g_rozpoczecia_4': self.godz_rozpoczecia_4.get(),
                      'g_zakonczenia_4': self.godz_zakonczenia_4.get(),
                      'przedmiot_4': self.lekcja_4.get(),
                      'g_rozpoczecia_5': self.godz_rozpoczecia_5.get(),
                      'g_zakonczenia_5': self.godz_zakonczenia_5.get(),
                      'przedmiot_5': self.lekcja_5.get(),
                      'g_rozpoczecia_6': self.godz_rozpoczecia_6.get(),
                      'g_zakonczenia_6': self.godz_zakonczenia_6.get(),
                      'przedmiot_6': self.lekcja_6.get(),
                      'g_rozpoczecia_7': self.godz_rozpoczecia_7.get(),
                      'g_zakonczenia_7': self.godz_zakonczenia_7.get(),
                      'przedmiot_7': self.lekcja_7.get(),
                      'g_rozpoczecia_8': self.godz_rozpoczecia_8.get(),
                      'g_zakonczenia_8': self.godz_zakonczenia_8.get(),
                      'przedmiot_8': self.lekcja_8.get(),
                      'g_rozpoczecia_9': self.godz_rozpoczecia_9.get(),
                      'g_zakonczenia_9': self.godz_zakonczenia_9.get(),
                      'przedmiot_9': self.lekcja_9.get(),
                  })
        conn.commit()
        conn.close()
        x.destroy()

# ---------------------------------definicje usuwania-------------------------------------
    def UsunRekord(self, x):
        index = self.rekordDoUsuniecia.get()
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        c.execute('DELETE FROM przypomnij WHERE id=?', (index,))
        conn.commit()
        conn.close()
        x.destroy()

    def UsunLekcje(self, x):
        index = self.usunRekordLekcje.get()
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        c.execute('DELETE FROM plan_lekcji WHERE id=?', (index,))
        conn.commit()
        conn.close()
        x.destroy()

# ********************************** tworzenie bazy **************************************


class TworzenieBaz:
    def __init__(self):
        okno = tk.Tk()
        okno.geometry("400x200")
        okno.title("Tworzenie Bazy")
        conn = sqlite3.connect('PRZYPOMINACZ.db')
        c = conn.cursor()
        c.execute(
            """CREATE TABLE przypomnij(
                id INTEGER PRIMARY KEY ASC,
                dzien_tygodnia text NOT NULL,
                dzien_miesiaca NOT NULL,
                miesiac text NOT NULL,
                tresc_przypomnienia text NOT NULL);"""
        )
        linia1 = tk.Label(okno, text="Baza przypomnień - utworzono!!!",
                          font=("Arial", 12), fg="blue")
        linia1.place(x=20, y=20)
        
        c.execute("""CREATE TABLE pamietnik (
                id INTEGER PRIMARY KEY ASC,
                data text NOT NULL,
                dzien_tyg text NOT NULL,
                wpis text NOT NULL);""")
        linia3 = tk.Label(okno, text = "Baza pamiętnik - utworzono!!!",
                          font=("Arial", 12), fg ="blue")
        linia3.place(x=20, y=80)
        
        c.execute(
            """CREATE TABLE plan_lekcji (
                id INTEGER PRIMARY KEY ASC,
                dzien text NOT NULL,
                g_rozpoczecia_1 text NOT NULL,
                g_zakonczenia_1 text NOT NULL,
                przedmiot_1 text NOT NULL,
                g_rozpoczecia_2 text NOT NULL,
                g_zakonczenia_2 text NOT NULL,
                przedmiot_2 text NOT NULL,
                g_rozpoczecia_3 text NOT NULL,
                g_zakonczenia_3 text NOT NULL,
                przedmiot_3 text NOT NULL,
                g_rozpoczecia_4 text NOT NULL,
                g_zakonczenia_4 text NOT NULL,
                przedmiot_4 text NOT NULL,
                g_rozpoczecia_5 text NOT NULL,
                g_zakonczenia_5 text NOT NULL,
                przedmiot_5 text NOT NULL,
                g_rozpoczecia_6 text NOT NULL,
                g_zakonczenia_6 text NOT NULL,
                przedmiot_6 text NOT NULL,
                g_rozpoczecia_7 text NOT NULL,
                g_zakonczenia_7 text NOT NULL,
                przedmiot_7 text NOT NULL,
                g_rozpoczecia_8 text NOT NULL,
                g_zakonczenia_8 text NOT NULL,
                przedmiot_8 text NOT NULL,
                g_rozpoczecia_9 text NOT NULL,
                g_zakonczenia_9 text NOT NULL,
                przedmiot_9 text NOT NULL
            );"""
        )
        conn.commit()
        conn.close()
        linia2 = tk.Label(okno, text="Paza planu lekcji - utworzono!!!",
                          font=("Arial", 12), fg="blue")
        linia2.place(x=20, y=50)
        button = tk.Button(okno, text="Zamknij okno", font=(
            "Arial", 13), fg="red", command=okno.destroy)
        button.place(x=130, y=120)

        okno.mainloop()


my_file = Path("PRZYPOMINACZ.db")
if my_file.is_file():
    Program()
else:
    TworzenieBaz()
