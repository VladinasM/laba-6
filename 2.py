import threading
import time
from tkinter import *

delay = 0.01
def rect_move(event):
    while True:
        s = c.coords(circle)
        while s[2] > 251:
            c.move(circle, -2, 0)
            s = c.coords(circle)
            time.sleep(delay)
        
        while s[2] >= 251 and s[2] < 537 :
            c.move(circle, 2, 0)
            s = c.coords(circle)
            time.sleep(delay)


root = Tk()
c = Canvas(root, width=800, height=800, bg="white")
c.pack()

a = c.create_oval(500, 371, 537, 408, fill='green')
b = c.create_oval(214, 371, 251, 408, fill='red')
circle = c.create_rectangle(502, 374, 529, 400, fill='blue')
#button = Button(root, text="Start", command=rect_move)
#startButton = c.create_window(300, 100, window=button)
thread = threading.Thread(target=rect_move, name="Okno", args=[c])
thread.start()

root.mainloop()
