import winreg
from tkinter import *
import os, sys
from tkinter import messagebox
from time import sleep


# connecting to key in registry
def RegistryDeal(path):
    access_registry = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
    key1 = winreg.CreateKey(access_registry, "Cv2Qt")
    winreg.SetValue(key1, "", winreg.REG_SZ, "URL:Video for Pyqt")
    winreg.SetValueEx(key1, "URL Protocol", 0, winreg.REG_SZ, path)
    key2 = winreg.CreateKey(access_registry, r"Cv2Qt\Defaultlcon")
    winreg.SetValue(key2, "", winreg.REG_SZ, path + ",1")
    Key3 = winreg.CreateKey(access_registry, r"Cv2Qt\shell")
    key4 = winreg.CreateKey(access_registry, r"Cv2Qt\shell\open")
    Key5 = winreg.CreateKey(access_registry, r"Cv2Qt\shell\open\command")
    winreg.SetValue(Key5, "", winreg.REG_SZ, "\"" + path + "\" \"%1\"")
    access_registry.Close()


def DelRegistry(path):
    access_registry = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
    # key = winreg.OpenKey(access_registry, "Cv2Qt", 0, winreg.KEY_READ)
    winreg.DeleteKey(access_registry, "Cv2Qt")


def writeToRegistry():
    global e
    path = e.get()
    if os.path.isfile(path):
        RegistryDeal(path)
        messagebox.showinfo("完成", "写入成功，3秒后自动退出")
        sleep(3)
        sys.exit(0)
    else:
        messagebox.showerror("提示", "路径错误，请检查后输入")


# path = r"C:\\Users\\QWH\\Cv2QtChrome.exe"
root = Tk()
root.title("写入注册表")
root.geometry("350x250")
sw = root.winfo_screenwidth()
# 得到屏幕宽度
sh = root.winfo_screenheight()
# 得到屏幕高度
ww = 380
wh = 130
# 窗口宽高为100
x = (sw - ww) / 2
y = (sh - wh) / 2
root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
root.resizable(width=False, height=False)
l = Label(root, text="请输入Cv2QtChrome路径：")
e = Entry(root, width=40)
b = Button(root, text="写入注册表", command=writeToRegistry)
l.pack(pady=10)
e.pack()
b.pack(pady=15)
root.mainloop()
