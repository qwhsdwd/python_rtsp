import cv2

# 用户名
username = "admin"
# 密码
password = "Admin12345"
# password = "abc123++"
# 摄像头ip
ip = "192.168.3.252"
# ip = "172.16.248.70"
# 端口
port = "554"
# port = "80"
rtmp_str = "rtsp://" + username + ":" + password + "@" + ip + ":" + port + "/Streaming/Channels/1"
hk_video = "rtsp://{}:{}@{}:{}/Streaming/Channels/1".format(username, password, ip, port)
dh_video = "rtsp://{}:{}@{}/cam/realmonitor?channel=1&subtype=0".format(username, password, ip)
url = rtmp_str
cap = cv2.VideoCapture(url)
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
