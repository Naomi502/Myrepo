import os

def push_to_remote():
    # 检查当前目录是否为一个 Git 仓库
    if not os.path.exists(".git"):
        print("当前目录不是一个 Git 仓库，请进入正确的目录。")
        return

    # 执行 Git 操作
    os.system("git add .")
    os.system("git commit -m '本次自动化提交成功code34'")
    os.system("git push")

    print("本地代码成功推送到远程仓库。")

# 执行推送操作
push_to_remote()
