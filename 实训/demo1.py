import tkinter
from tkinter import filedialog, messagebox
import jieba.analyse
from wordcloud import WordCloud, ImageColorGenerator
import tempfile
import numpy as np
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
from tkinter import ttk

def open_file():
    filename = filedialog.askopenfilename()
    if filename:
        with open(filename, 'r', encoding='UTF-8') as f:
            text1.delete('1.0', 'end')
            for line in f:
                text1.insert('end', line)


def open_word():
    # 获取文本框1中的内容
    text = text1.get("1.0", "end-1c")
    # 使用结巴分词提取关键词
    keywords = jieba.analyse.extract_tags(text, topK=100, withWeight=True)
    # 构建关键词和权重的字典
    word_freq = {word: weight for word, weight in keywords}
    # 生成词云对象
    wordcloud = WordCloud(font_path="simsun.ttc", width=400, height=400, background_color='white',mask=np.array(Image.open("heart.png"))).generate_from_frequencies(word_freq)
    # 生成词云颜色
    image_colors = ImageColorGenerator(np.array(Image.open("heart.png")))
    # 生成临时文件保存词云图像
    tmp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    wordcloud.recolor(color_func=image_colors).to_file(tmp_file.name)
    # 打开词云图像并显示在文本框2中
    img = Image.open(tmp_file.name)
    img = img.resize((400, 400))
    photo = ImageTk.PhotoImage(img)
    text2.delete("1.0", "end")
    text2.image_create(tkinter.END, image=photo)
    text2.image = photo


def show_info():
    messagebox.showinfo("软件信息", "这是一个词云生成器软件，用于从文本生成词云图像。")

def exit_app():
    root.destroy()


def web_crawl():
    # 获取用户输入的网址
    url = url_entry.get()
    # 发起网络请求
    response = requests.get(url)
    response.encoding = 'utf-8'
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    # 提取<p>标签中的文本内容并拼接
    text = ''
    for paragraph in soup.find_all('p'):
        text += paragraph.get_text() + '\n'
    # 清空文本框1并插入爬取到的文本内容
    text1.delete('1.0', 'end')
    text1.insert('1.0', text)


root = tkinter.Tk()
root.title('词云生成器')
root.geometry('800x600+300+100')

# 设置主题样式
style = ttk.Style()
style.theme_use('clam')

# 设置窗口背景颜色
root.configure(background='#FFF')

# 设置标签样式
style.configure('TLabel', font=('Arial', 12), background='#FFF', foreground='#333')

# 设置按钮样式
style.configure('TButton', font=('Arial', 12), background='#EEE', borderwidth=1)
style.map('TButton', background=[('active', '#DDD')])

frame1 = tkinter.Frame(root, bg='#FFF')
frame1.pack(pady=10)

text1 = tkinter.Text(frame1, height=20, width=40, bg='#FFF', fg='#333', bd=2)
text1.pack(side='left', padx=10)

text2 = tkinter.Text(frame1, height=20, width=40, bg='#FFF', fg='#333', bd=2)
text2.pack(side='right', padx=10)

url_frame = tkinter.Frame(root, bg='#FFF')
url_frame.pack(pady=10)

url_label = ttk.Label(url_frame, text="请输入网址：")
url_label.pack(side='left', padx=10)

url_entry = ttk.Entry(url_frame, width=50)
url_entry.pack(side='left', padx=10)

button_frame = tkinter.Frame(root, bg='#FFF')
button_frame.pack(pady=10)

open_button = ttk.Button(button_frame, text="打开文件", command=open_file)
open_button.pack(side='left', padx=10)

word_button = ttk.Button(button_frame, text="生成词云", command=open_word)
word_button.pack(side='left', padx=10)

crawl_button = ttk.Button(button_frame, text="爬取网页内容", command=web_crawl)
crawl_button.pack(side='left', padx=10)

info_button = ttk.Button(button_frame, text="关于", command=show_info)
info_button.pack(side='left', padx=10)

exit_button = ttk.Button(button_frame, text="退出", command=exit_app)
exit_button.pack(side='left', padx=10)

root.mainloop()
