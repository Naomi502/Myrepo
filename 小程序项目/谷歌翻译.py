import requests
import json

TRANSLATE_API_URL = "https://findmyip.net/api/translate.php"


import requests
import json


def translate():
    while True:
        text = input("请输入你需要翻译的文字（输入 'exit' 可以退出）: ")

        if text.lower() == 'exit':
            break

        translate_response = requests.get(f"{TRANSLATE_API_URL}?text={text}")

        if translate_response.status_code == 200:
            translation_data = translate_response.json()['data']
            response_time = translate_response.json()['processTime']

            print('CODE:', translate_response.status_code)
            print('谷歌翻译结果:', translation_data['translate_result'])
            print('原文本语言:', translation_data['source_lang'])
            print('翻译后语言:', translation_data['target_lang'])
            print('响应时间:', response_time)

            save_history({
                'data': translation_data,
                'processTime': response_time
            })

        else:
            print('翻译失败, 错误代码:', translate_response.status_code)


def save_history(translate_result):
    # 读取现有历史记录
    try:
        with open('history.txt', 'r') as f:
            history_dict = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history_dict = {}

    # 添加新的历史记录
    history_dict[str(len(history_dict) + 1)] = translate_result

    # 保存到文本文件
    with open('history.txt', 'w+') as f:
        json.dump(history_dict, f, ensure_ascii=False, indent=2, sort_keys=True)


def history():
    # 读取历史记录
    try:
        with open('history.txt', 'r') as f:
            history_dict = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print('没有历史记录')
        return

    # 打印历史记录列表
    print('历史记录列表:')
    for key, value in history_dict.items():
        print(f'{key}. {value["data"]["translate_result"]}')

    # 选择要查看的历史记录
    choice = input('请选择要查看的历史记录编号: ')
    selected_history = history_dict.get(choice)

    if selected_history:
        print('谷歌翻译结果:', selected_history['data']['translate_result'])
        print('原文本语言:', selected_history['data']['source_lang'])
        print('翻译后语言:', selected_history['data']['target_lang'])
        print('响应时间:', selected_history['processTime'])
    else:
        print('无效的选择')


def main():
    print('Google Translate')
    print('1.开始翻译')
    print('2.查看历史')

    choice = input('请选择操作（输入数字）: ')

    if choice == '1':
        translate()
    elif choice == '2':
        history()
    else:
        print('无效的选择')


if __name__ == "__main__":
    main()



def save_history(translate_result):
    # 读取现有历史记录
    try:
        with open('history.txt', 'r') as f:
            history_dict = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history_dict = {}

    # 添加新的历史记录
    history_dict[str(len(history_dict) + 1)] = translate_result

    # 保存到文本文件
    with open('history.txt', 'w+') as f:
        json.dump(history_dict, f, ensure_ascii=False, indent=2, sort_keys=True)


def history():
    while True:
        try:
            with open(HISTORY_FILE, 'r') as history_file:
                history_dict = json.load(history_file)
        except (FileNotFoundError, json.JSONDecodeError):
            print('没有历史记录')
            return

        print('历史记录列表:')
        for key, value in history_dict.items():
            print(f'{key}. {value["data"]["translate_result"]}')

        choice = input('请选择要查看的历史记录编号 (输入 "exit" 可以退出): ')

        if choice.lower() == 'exit':
            break

        selected_history = history_dict.get(choice)

        if selected_history:
            print('谷歌翻译结果:', selected_history['data']['translate_result'])
            print('原文本语言:', selected_history['data']['source_lang'])
            print('翻译后语言:', selected_history['data']['target_lang'])
            print('响应时间:', selected_history['processTime'])
        else:
            print('无效的选择')


def main():
    print('Google Translate')
    while True:
        print('1.开始翻译')
        print('2.查看历史')
        print('3.退出')

        choice = input('请选择操作（输入数字）: ')

        if choice == '1':
            translate()
        elif choice == '2':
            history()
        elif choice == '3':
            break
        else:
            print('无效的选择')

if __name__ == "__main__":
    main()
