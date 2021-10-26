str_chrome = "cv2qt://hk%20-u%20admin%20-w%20Admin12345%20-i%20192.168.3.252%20-p%20554/"
str_chrome = r"{C:\Users\QWH\Cv2Qt.exe} cv2qt://hk%20-u%20admin%20-w%20Admin12345%20-i%20192.168.3.252%20-p%20554/"
# 浏览器传回来的参数做最终处理
# str1 = str_chrome.replace("%20", " ")[8:-1]
str1 = str_chrome.split("//")
# 以’//‘为分割线，对字符串进行分割
str2 = str1[1].replace("%20", " ")[:-1]
# 将‘%20’替换成空格
list1 = str2.split(" ")
# 以空格进行分割
print(list1)

