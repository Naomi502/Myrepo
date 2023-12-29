#
# def create(filename):
#     with open(filename, 'w') as file:
#         file.write('')
#
#
#
# def write(filename, content):
#     with open(filename, 'a') as file:
#         file.write(content)
#
#
# def read(filename):
#     with open(filename, 'r') as file:
#         content = file.read()
#     return content
#
#
# filename = 'example.txt'
# create(filename)
# write(filename, 'python6666')
# print(read(filename))
#
# import csv
#
# data = [
#     ['Name', 'Age', 'Email'],
#     ['230404101', 30, 'A@example.com'],
#     ['230404102', 25, 'B@example.com'],
#     ['230405103', 26, 'C@example.com']
# ]
#
# with open('example.csv', 'w', newline='') as csvfile:
#
#     writer = csv.writer(csvfile)
#     writer.writerow(data[0])
#     writer.writerows(data[1:])
#
# with open('example.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)
#
#     for row in reader:
#         print(row)

with open('example.txt','r+',encoding='utf-8')as file:
    line = ['计算机应用','工程造价','云计算','会计']
    for i in range(len(line)-1):
        file.write(line[i])
        file.write(' ')
    print(file.read())