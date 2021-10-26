# 这个代码注意点 设置好正确的用户名、密码、ip、端口，端口默认为554，
import cv2


#用户名
username = "admin"
#密码
password = "Admin12345"
#摄像头ip
ip = "192.168.3.252"
#端口
port = "554"
cap = cv2.VideoCapture("rtsp://" + username + ":" + password+ "@" + ip  + ":" + port + "/Streaming/Channels/1")
# 摄像头是否处于打开状态可以通过isOpened()方法进行判断
isOpened = cap.isOpened()
if isOpened :
  #  可以通过read() 方法读取图像
  ret, frame = cap.read()
  #再代码目录下生成tmp.jpg图片文件
  cv2.imwrite("tmp.jpg", frame)
cap.release()
print('完成抓拍')