"""参数说明
Usage:
  Cv2qt hk ((-u|--username) <username>) ((-w|--password) <password>) ((-i|--ip) <ip>) ((-p|port) <port>)
  Cv2qt dh ((-u|--username) <username>) ((-w|--password) <password>) ((-i|ip) <ip>)
  Cv2qt -h | --help
  Cv2qt --version

Options:
    -h --help   帮助.
    -v --version    查看版本号.
    -u --username   用户名
    -w --password   密码
    -i --ip     ip地址
    -p --port   端口号

Examples:
    Cv2qt hk -u admin -w Admin12345 -i 192.168.3.252 -p 554
    Cv2qt dh -u admin -w abc123++ -i 172.16.248.70
"""
import sys
from docopt import docopt

arguments = docopt(__doc__, version="1.0.0")
print(sys.argv[1] + "\n\n")
print(arguments)
# for i in arguments:
#     print(i)
