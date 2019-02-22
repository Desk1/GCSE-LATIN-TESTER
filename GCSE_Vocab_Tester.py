from tkinter import *
from vocab_la import *
from random import shuffle
truefailed = []
failtest = False
random = False
late = []
ente = []


def main_menu():
    failed = []
    mark = 0
    completed = 0
    test = "all"
    def allA():
        nonlocal test
        test = "a"
        tester()
    def allB():
        nonlocal test
        test = "b"
        tester()
    def allC():
        nonlocal test
        test = "c"
        tester()
    def allD():
        nonlocal test
        test = "d"
        tester()
    def allE():
        nonlocal test
        test = "e"
        tester()
    def allF():
        nonlocal test
        test = "f"
        tester()
    def tester():
        global failtest
        global random
        nonlocal ranvar
        if random:
            return "o"
        elif failtest:
            global ente
            global late
            lat = late
            ent = ente
            failtest = False
        else:
            tkmenu.destroy()
            nonlocal test
            if test == "a":
                lat = la[:la.index("finished a")]
                ent = en[:en.index("finished a")]
            elif test == "b":
                lat = la[la.index("finished a")+1:la.index("finished b")]
                ent = en[en.index("finished a")+1:en.index("finished b")]
            elif test == "c":
                lat = la[la.index("finished b")+1:la.index("finished c")]
                ent = en[en.index("finished b")+1:en.index("finished c")]
            elif test == "d":
                lat = la[la.index("finished c")+1:la.index("finished d")]
                ent = en[en.index("finished c")+1:en.index("finished d")]
            elif test == "e":
                lat = la[la.index("finished d")+1:la.index("finished e")]
                ent = en[en.index("finished d")+1:en.index("finished e")]
            elif test == "f":
                lat = la[la.index("finished e")+1:la.index("finished f")]
                ent = en[en.index("finished e")+1:en.index("finished f")]
            else:
                lat = la
                ent = en
            if ranvar.get() == 1:
                shuffle(lat)
                ent = []
                for i in lat:
                    ent.append(laen[i])


        laent = dict(zip(lat,ent))
        tk=Tk()
        def enter_input(event=None):
            inp = entry_1.get()
            nonlocal completed
            nonlocal mark
            nonlocal failed
            nonlocal lat
            nonlocal ent
            nonlocal laent
            if type(ent[completed]) == list:
                if inp.lower() in ent[completed]:
                    entry_1["bg"] = "Light Green"
                    entry_1["fg"] = "White"
                    mark += 1
                else:
                    entry_1["bg"] = "Red"
                    failed.append(label_1["text"])
                    label_2["text"] = ent[completed][0]
                    label_2["bg"] = "Light Green"
            else:
                if inp.lower() == laent[label_1["text"]]:
                    entry_1["bg"] = "Light Green"
                    entry_1["fg"] = "White"
                    mark += 1
                else:
                    entry_1["bg"] = "Red"
                    failed.append(label_1["text"])
                    label_2["text"] = laent[label_1["text"]]
                    label_2["bg"] = "Light Green"
            completed += 1
            tk.after(600, advance)

        def advance():
            nonlocal lat
            nonlocal ent
            nonlocal laent
            try:
                label_1["text"] = lat[lat.index(label_1["text"])+1]
                if "finished " in label_1["text"]:
                    advance()
                entry_1["bg"] = "White"
                entry_1["fg"] = "Black"
                entry_1.delete(0,"end")
                nonlocal label_2
                label_2.destroy()
                label_2=Label(tk,text="",font=("Calibri", 40),width=entry_1["width"],fg="White")
                label_2.grid(row=1,column=1)
            except IndexError:
                stop()


        def Quit():
            global failtest
            failtest = False
            tk.destroy()

        def mainmenu():
            tk.destroy()
            main_menu()

        def rest():
            nonlocal failed
            nonlocal completed
            nonlocal mark
            failed = []
            completed = 0
            mark = 0

        def failed_test():
            global truefailed
            if truefailed == []:
                #button_3["text"] = "None failed"
                return "null"
            else:
                nonlocal lat
                nonlocal ent
                global failtest
                global ente
                global late
                failtest = True
                late = truefailed
                ente = []
                for i in late:
                    ente.append(en[la.index(i)])
                tk.destroy()
                rest()
                tester()

        def stop(event=None):
            nonlocal button
            button.destroy()
            button = Button(tk,text="Quit",command=Quit,font=("Calibri", 25))
            button_2 = Button(tk,text="Main menu",command=mainmenu,font=("Calibri", 25))
            entry_1.destroy()
            stop_button.destroy()
            nonlocal label_2
            label_2.destroy()
            nonlocal label_1
            label_1.destroy()
            label_i = Label(tk,text="Mark : ",font=("Calibri", 40))
            label_mark = Label(tk,text=str(mark)+"/"+str(completed),font=("Calibri", 40))
            label_2 = Label(tk,text="Failed : ",font=("Calibri", 40))
            nonlocal failed
            global truefailed
            truefailed = []
            for i in failed:
                truefailed
                truefailed.append(i)
                if failed.index(i) != 0:
                    if failed.index(i) % 7 == 0:
                        failed.insert(failed.index(i),"\n")
            label_3 = Label(tk,text=" ".join(failed),font=("Calibri", 16))
            button_3 = Button(tk,text="Test on failed words",command=failed_test,font=("Calibri", 25))
            label_i.pack(side=LEFT,fill=BOTH)#mark=
            label_mark.pack(side=LEFT,fill=BOTH)#mark
            label_3.pack(side=RIGHT,fill=BOTH)#failed
            label_2.pack(side=RIGHT,fill=BOTH)#failed=
            button.pack(side=BOTTOM,fill=BOTH)#quit
            button_2.pack(fill=BOTH)#main menu
            button_3.pack(side=LEFT,fill=BOTH,expand=TRUE)#failed test

        tk.bind("<Return>", enter_input)
        tk.bind("<Escape>", stop)
        label_1=Label(tk,text=lat[0],font=("Calibri", 40))
        entry_1=Entry(tk,font=("Calibri", 40))
        label_2=Label(tk,text="",font=("Calibri", 40),width=entry_1["width"],fg="White")
        button=Button(tk,text="Enter \n(press return)",command=enter_input,font=("Calibri", 25))
        stop_button = Button(tk,text="Finish \n(press esc)",command=stop,font=("Calibri", 25))
        label_1.grid(row=0,column=0)
        label_2.grid(row=1,column=1)
        entry_1.grid(row=0,column=1)
        button.grid(row=0,column=2)
        stop_button.grid(row=1,column=0)

        tk.mainloop()


    tkmenu=Tk()
    tkmenu.title("GCSE Latin Vocab Tester - Cherian")
    ranvar = IntVar()
    label_1=Label(tkmenu,text="Main Menu" ,font=("Calibri", 40),width=35)
    allA=Button(tkmenu,text="Letter A",command=allA,font=("Calibri", 25),width=40)
    allB=Button(tkmenu,text="Letter B",command=allB,font=("Calibri", 25),width=40)
    allC=Button(tkmenu,text="Letter C",command=allC,font=("Calibri", 25),width=40)
    allD=Button(tkmenu,text="Letter D",command=allD,font=("Calibri", 25),width=40)
    allE=Button(tkmenu,text="Letter E",command=allE,font=("Calibri", 25),width=40)
    allF=Button(tkmenu,text="Letter F",command=allF,font=("Calibri", 25),width=40)
    allem=Button(tkmenu,text="All",command=tester,font=("Calibri", 25),width=40)
    ran=Checkbutton(tkmenu,text="Randomise",variable=ranvar,font=("Calibri", 15))
    label_1.grid(row=0,column=0)
    allA.grid(row=1,column=0)
    allB.grid(row=2,column=0)
    allC.grid(row=3,column=0)
    allD.grid(row=4,column=0)
    allE.grid(row=5,column=0)
    allF.grid(row=6,column=0)
    allem.grid(row=7,column=0)
    ran.grid(row=8,column=0)

    tkmenu.mainloop()

main_menu()
