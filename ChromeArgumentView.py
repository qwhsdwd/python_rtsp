import sys
from tkinter import *

# str1 = sys.argv[0].split("//")
str1 = sys.argv[1][8:]
str2 = str1.replace("%20", " ")[:-1]
arguments = str2.split(" ")

root = Tk()
root.geometry("500x500")
text = Text(root, height=10, width=50, pady=10)
text.pack()
text.insert(END, arguments[0])
text.insert(END, arguments[1])
text.insert(END, arguments[2])
text.insert(END, arguments[3])

root.mainloop()
