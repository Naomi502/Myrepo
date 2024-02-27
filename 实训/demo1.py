import tkinter
from tkinter import filedialog, messagebox
import jieba.analyse
from wordcloud import WordCloud, ImageColorGenerator
import tempfile
import numpy as np
from PIL import Image, ImageTk

text1 = None
text2 = None

root = tkinter.Tk()
root.title('python主窗口')
root.geometry('1000x530+300+500')

def open_file():
    global text1
    filename = filedialog.askopenfilename()
    if filename != '':
        with open(filename, 'r', encoding='UTF-8') as f:
            for line in f:
                text1.insert(tkinter.END, line)

def open_word():
    global text1, text2
    # 从text1中获取文本内容
    text = text1.get("1.0", "end-1c")
    keywords = jieba.analyse.extract_tags(text, topK=100, withWeight=True)
    word_freq = {word: weight for word, weight in keywords}
    # 生成词云
    wordcloud = WordCloud(font_path="simsun.ttc", width=600, height=600, background_color='white', mask=np.array(Image.open("heart.png"))).generate_from_frequencies(word_freq)
    # 生成颜色
    image_colors = ImageColorGenerator(np.array(Image.open("heart.png")))
    # 保存词云为临时文件
    tmp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    wordcloud.recolor(color_func=image_colors).to_file(tmp_file.name)
    # 加载临时文件中的图片
    img = Image.open(tmp_file.name)
    img = img.resize((600, 600))  # 调整图片大小
    photo = ImageTk.PhotoImage(img)
    # 清空text2中的内容并显示图片
    text2.delete("1.0", "end")
    text2.image_create(tkinter.END, image=photo)
    text2.image = photo  # 保持图片引用，防止被垃圾回收

def show_info():
    messagebox.showinfo("软件信息", "这是一个词云生成器软件，用于从文本生成词云图像。")

def exit_app():
    root.destroy()

menu = tkinter.Menu(root)
root.config(menu=menu)

text1 = tkinter.Text(root, height=20, width=55)
text1.pack(side='left', anchor='n')

text2 = tkinter.Text(root, height=40, width=80)
text2.pack(side='right', anchor='n')

file_menu = tkinter.Menu(menu)
menu.add_cascade(label='文件', menu=file_menu)
file_menu.add_command(label='打开', command=open_file)
file_menu.add_command(label='退出', command=exit_app)

word_menu = tkinter.Menu(menu)
menu.add_cascade(label='词云', menu=word_menu)
word_menu.add_command(label='从当前文章生成词云', command=open_word)

help_menu = tkinter.Menu(menu)
menu.add_cascade(label='帮助', menu=help_menu)
help_menu.add_command(label='关于', command=show_info)

root.mainloop()
