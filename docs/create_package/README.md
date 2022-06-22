# toy_repository
create a new package

## 创建空仓库
github创建空仓库，git clone到本地
<img style="float: center;" src="./pics/new_repository.png" width="80%">

settings:
- .gitignore: Python
- license: apache liscence 2.0

## 创建基本的包并安装

- 创建包的基本结构，添加必要文件：
	- requirements.txt
	- toy_repository各级目录下添加 __init__.py，toy_repository/__init__.py 中添加版本 __version__ == "0.0.1"
	- setup.py
<img style="float: center;" src="./pics/repository_structure.png">
	
- develop安装
<img style="float: center;" src="./pics/setup.png">

## 函数开发

- 定义与调用
	- 定义函数
	- 函数的简单使用
<img style="float: center;" src="./pics/function_def.png">

- 函数调试：使用pdb.set_trace()，具体用法参考 [pdb](https://docs.python.org/3/library/pdb.html)
<img style="float: center;" src="./pics/function_debug.png">

- 函数测试：[test_statistics.py](../test/test_statistics.py)
<img style="float: center;" src="./pics/test.png">

- 函数用例：[use_statistics.py](../example/use_statistics.py)
<img style="float: center;" src="./pics/example.png">



