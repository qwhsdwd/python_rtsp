# -*- coding: utf-8 -*-
import winreg

# connecting to key in registry
access_registry = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)

access_key = winreg.OpenKey(access_registry, r"Cv2Qt")
# accessing the key to open the registry directories under
for n in range(20):
    try:
        x = winreg.EnumKey(access_key, n)
        y = winreg.EnumValue(access_key, n)
        print(x, y)
    except:
        break
# test = winreg.CreateKey(access_registry, r"Cv2Qt1")
# test1 = winreg.SetValue(access_registry, r"Cv2Qt1\command\\", winreg.REG_SZ,
# #                         "\"C:\\Users\\QWH\\Cv2QtChrome.exe\" \"%1\"")
# print(test)

"""







"""
