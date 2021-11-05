# trsp for python

![](.\image\show_image.png)
# 简介
基于python开发，使用pyqt5和opencv框架完成的rtsp流实时查看程序，支持远程查看海康和大华摄像头，**且支持在浏览器直接打开（附带windows写入注册表代码）**，由于涉及到对图像的实时处理，所以比较占用cpu和内存，建议一次性开启数量不要超过2个
## 代码文件介绍
- image：图片文件存放目录
- registry:写入注册表代码，如果如果不需要gui界面,操作RegistryDeal(path)函数
- Cv2Qt.py:命令行运行脚本
- Cv2QtChrome.py： 浏览器内运行的脚本
- Cv2Show.py：只有cv2模块实现的trsp流查看，图像不稳定(不推荐)
- Cv2Tk.py:用tkinter实现的trsp流查看（不推荐)
- StrDeal.py:处理浏览器的参数代码，由于浏览器传回来的参数会自动转换，需要额外进行处理一遍
- VideoSnap.py: rtsp流视频画面实时抓取
## 使用方式
- 命令运行: 运行Cv2Qt.py --help查看参数
- 浏览器内运行:进入open-video-on-browser文件夹，先运行Cv2Registry.exe 将私有协议写入注册表(用管理员打开，不然权限不够)，再直接在浏览器输入参数即可
>浏览器参数：Cv2qt:// hk -u admin -w Admin12345 -i 192.168.3.252 -p 554（海康)
>                    
              Cv2qt:// dh -u admin -w abc123++ -i 172.16.248.70（大华)