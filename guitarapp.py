import tkinter as tk

from tkinter import ttk  

import webbrowser


window = tk.Tk()

window.geometry("450x600")

window.title("Buy a Guitar, please sir")

label1 = tk.Label(text = "Gibson335")

label2 = tk.Label(text = "Fender Stratocaster")

label3 = tk.Label(text = "MartinD28")

label1.grid(column=0,row=0)
label2.grid(column=0,row=1)
label3.grid(column=0,row=2)

button1 = tk.Button(window, text = "Price")
button2 = tk.Button(window, text = "Price")
button3 = tk.Button(window, text = "Price")

button4 = tk.Button(window, text = "Website")
button5 = tk.Button(window, text = "Website")
button6 = tk.Button(window, text = "Website")

button1.grid(column=3, row = 0)
button2.grid(column=3, row = 1)
button3.grid(column=3, row = 2)

button4.grid(column = 4, row = 0)
button5.grid(column = 4, row = 1)
button6.grid(column = 4, row = 2)





def purchase1(event):
	print("A Gibson 335 costs $2219")

def purchase2(event):
	print("A Fender Statocaster costs $1299")

def purchase3(event):
	print("A Martin D28 costs $3000")

def open_gibson(event):
	webbrowser.open_new_tab('http://Gibson.com')

def open_fender(event):
	webbrowser.open_new_tab('http://Fender.com')

def open_martin(event):
	webbrowser.open_new_tab('http://Martinguitar.com')



button1.bind("<Button-1>", purchase1)
button2.bind("<Button-1>", purchase2)
button3.bind("<Button-1>", purchase3)

button4.bind("<Button-1>", open_gibson)
button5.bind("<Button-1>", open_fender)
button6.bind("<Button-1>", open_martin)


window.mainloop()

