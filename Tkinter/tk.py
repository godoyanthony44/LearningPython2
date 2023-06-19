import tkinter as tk
font = ("Arial", 24, "bold")
window = tk.Tk()
window.minsize(500,300)
window.title("First Window")



label = tk.Label(text="I am a label", font=font)
inputs = tk.Entry(width=10)
inputs.grid(column=3,row=3)


def button_clicked():
    label.config(text=inputs.get())

button = tk.Button(text="click me", font=font, command=button_clicked)
button2 = tk.Button(text="click me", font=font, command=button_clicked)

label.grid(column=0,row=0)
button.grid(column=2,row=1)
button2.grid(column=3,row=0)




window.mainloop()
