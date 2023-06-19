from tkinter import *
font = ("arial",24,'bold')
kilo = 0


def calc():
    miles = miles_input.get()
    kilo_label.config(text=f"is equal to   {int(miles) * 1.609}    Km")


window = Tk()
window.title("Miles to Km Converter")
window.config(width=300,height=500)
miles_input = Entry()
miles_label = Label(text="Miles")
kilo_label = Label(text=f"is equal to   {kilo}    Km")
calc_button = Button(text="Calculate", font=font, command=calc)

miles_input.grid(column=0,row=0)
miles_label.grid(column=1,row=0)
kilo_label.grid(column=0,row=1)
calc_button.grid(column=0,row=2)

window.mainloop()

