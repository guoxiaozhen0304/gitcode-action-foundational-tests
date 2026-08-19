import os
import subprocess
import re

current_directory = os.getcwd()

# First 
# 将 wiki 中 `(../images` 全部批量替换成 `(/images` 

def process_md_file(file_path):
    # 读取文件内容
    with open(file_path, "r") as f:
        contents = f.read()

    # 搜索并替换标签
    contents = re.sub(r'\(\.\./images', '(/images', contents)

    # 将替换后的内容写回文件
    with open(file_path, "w") as f:
        f.write(contents)

def process_directory(directory):
    # 列出目录下的所有文件和子目录
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        # 如果是文件夹，则递归处理
        if os.path.isdir(item_path):
            process_directory(item_path)
        # 如果是Markdown文件，处理文件内容
        elif item.endswith(".md"):
            process_md_file(item_path)

# 获取当前工作目录
current_directory = os.getcwd()

# 调用处理函数，遍历所有文件和文件夹
process_directory(current_directory)


# 定义要执行的Git命令列表
git_commands = [
    "rm -rf .git",
    "pwd",
    "git init",
    "git branch -m main",
    "git remote add wiki git@gitcode.com:Gitcode-offical-team/GitCode-Docs.wiki.git",
    "git add .",
    "git commit -m '<docs:release> v0.1 release'",
    "git push wiki main -f",
    "rm -rf .git"
]

# 循环遍历并执行每条Git命令
for command in git_commands:
    try:
        # 执行Git命令并等待完成
        subprocess.run(command, shell=True, check=True)
        print(f"成功执行Git命令: {command}")
    except subprocess.CalledProcessError as e:
        print(f"执行Git命令时出错: {command}")
        print(f"错误信息: {e}")
