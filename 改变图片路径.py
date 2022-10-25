import os
import shutil
path = "./相似矩阵及二次型"  # 文件夹目录
files = os.listdir(path)  # 得到文件夹下的所有文件名

# 创建文件夹
if not (os.path.exists(path+"/pictures")):
    os.mkdir(path+"/pictures")

for file in files:
    # 移动图片到指定目录
    if file.endswith(".png") or file.endswith(".jpg"):
        shutil.move(path+"/"+file, path + "/pictures")

    # 为markdown文件中图片添加路径
    elif file.endswith(".md"):

        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            rf = open(path+"/"+file, mode='r', encoding="utf-8")  # 打开文件
            iter_f = iter(rf)  # 创建迭代器
            str = ""
            for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                path_exists = line.rfind("![](pictures/")
                if path_exists == -1:
                    i = line.rfind("![](")
                    if i != -1:
                        str_list = list(line)
                        str_list.insert(i+4, "pictures/")
                        str += "".join(str_list)
                    else:
                        str += line   

                else:
                    str += line

            rf.close()

            wf = open(path+"/"+file, mode='w', encoding="utf-8")  # 打开文件
            wf.write(str)
            wf.close()
