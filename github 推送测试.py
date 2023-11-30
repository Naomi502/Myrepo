ifpush = True
import os
import sys

def push():
    if ifpush:
        os.system("git add .")
        os.system("git commit -m '自动化测试'")
        os.system("git push")
        print("推送成功")
    else:
        sys.exit()

push()
