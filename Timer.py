from tkinter import *
import pygame


cor1 = "#242323"
cond = False


def timer():
    global hr, min, sec, cond
    
    if str(hr)[-2:] == "00" and str(min)[-2:] == "00" and str(sec)[-2:] == "00":
        label_crono["text"] = "00:00:00"
        pygame.init()
        pygame.mixer.music.load(r"./alarm.mp3")
        pygame.mixer.music.play()
        pygame.event.wait()

    else:
        if cond == True:

            if int(sec) <= 0:
                if int(min) > 0:
                    min = int(min) - 1
                    sec = 59
                
            if int(min) <= 0:
                if int(hr) > 0:
                    hr = int(hr) - 1
                    min = 59

            sec = str(0) + str(sec)
            min = str(0) + str(min)
            hr = str(0) + str(hr)

            label_crono["text"] = str(hr[-2:]) + ":" + str(min[-2:]) + ":" + str(sec[-2:])

        if int(sec) > 0:
            sec = int(sec) - 1
        label_crono.after(1000, timer)
        entry_hr.delete(0, END)
        entry_min.delete(0, END)
        entry_sec.delete(0, END)

def dados():
    global hr, min, sec
    hr = entry_hr.get()
    min = entry_min.get()
    sec = entry_sec.get()
    if hr == "":
        hr = "0"
    if min == "":
        min = "0"
    if sec == "":
        sec = "0"
    timer()

def start():    
    global cond
    cond = True
    button_start["state"] = "disabled"
    dados()

main = Tk()
main.title("Timer")
main.geometry("600x350+650+300")
main.configure(bg= cor1)
main.resizable(height=False,width=False)

label_hr = Label(main, width=15, text="Horas", bg=cor1, fg= "white", font=("Courier 15 bold"))
label_hr.grid(row=0, column= 0, padx=7, pady=20)

label_min = Label(main, width=15, text="Minutos", bg=cor1, fg= "white", font=("Courier 15 bold"))
label_min.grid(row=0, column= 1, padx=7, pady=20)

label_sec = Label(main, width=15, text="Segundos", bg=cor1, fg= "white", font=("Courier 15 bold"))
label_sec.grid(row=0, column= 2, padx=5, pady=20)

label_crono = Label(main, text= "00:00:00", bg=cor1, fg="#16f59f", font="Courier 85 bold")
label_crono.place(x=25, y=110)


entry_hr = Entry(main, width=7, font="Arial 15")
entry_hr.grid(row=1, column=0)

entry_min = Entry(main, width=7, font="Arial 15")
entry_min.grid(row=1, column=1)

entry_sec = Entry(main, width=7, font="Arial 15")
entry_sec.grid(row=1, column=2)

button_start = Button(main, text="Start", command=start, relief="solid", overrelief="ridge", bg=cor1, fg= "white", font="Courier 15 bold")
button_start.place(x=260, y=260)



main.mainloop()