# 电子书管理工具 (book-man)

一个简单的电子书管理工具，目前支持将epub格式的电子书转换为txt格式。

## 功能特点

- 将epub电子书转换为txt纯文本格式
- 保留章节结构
- 支持中文内容处理
- 命令行操作简单方便
- 默认将转换后的文件存放在`output`目录中

## 安装

### 依赖项

- Python 3.8+
- ebooklib
- beautifulsoup4

### 安装步骤

1. 克隆本仓库：

```bash
git clone https://github.com/yourusername/book-man.git
cd book-man
```

2. 安装依赖：

```bash
# 使用uv安装
uv pip install -e .

# 或者使用pip安装
pip install -e .
```

## 使用方法

### 将epub转换为txt

安装后，可以直接使用命令行工具：

```bash
# 基本用法 - 转换后的文件将保存在'output'目录中
book-man epub2txt 你的电子书.epub

# 指定输出文件路径
book-man epub2txt 你的电子书.epub -o 自定义路径/输出文件.txt
```

或者也可以使用Python模块的方式：

```bash
python -m book_man epub2txt 你的电子书.epub
```

## 输出目录

默认情况下，转换后的txt文件将保存在工作目录下的`output`文件夹中。此文件夹会在首次转换时自动创建。

## 注意事项

- 转换后的txt文件使用UTF-8编码
- 转换过程会去除所有HTML标签和格式，只保留纯文本内容
- 对于复杂排版的epub文件，转换后可能会有一些格式上的差异

## 许可证

MIT
