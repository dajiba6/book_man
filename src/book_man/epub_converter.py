#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


# 默认输出目录
DEFAULT_OUTPUT_DIR = os.path.join(os.getcwd(), "output")


def epub_to_text(epub_path):
    """
    将epub文件转换为纯文本内容

    Args:
        epub_path: epub文件路径

    Returns:
        str: 提取的文本内容
    """
    try:
        # 打开epub文件
        book = epub.read_epub(epub_path)

        # 存储所有章节的文本
        chapters_text = []

        # 遍历所有文档
        for item in book.get_items():
            # 只处理文档内容
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                # 获取HTML内容
                html_content = item.get_content().decode("utf-8")

                # 使用BeautifulSoup解析HTML
                soup = BeautifulSoup(html_content, "html.parser")

                # 提取文本，去除HTML标签
                text = soup.get_text()

                # 清理文本（去除多余空白）
                text = "\n".join(
                    [line.strip() for line in text.split("\n") if line.strip()]
                )

                chapters_text.append(text)

        # 合并所有章节文本，用两个换行符分隔
        full_text = "\n\n".join(chapters_text)
        return full_text

    except Exception as e:
        print(f"转换过程中出错: {str(e)}")
        return None


def convert_epub_to_txt(epub_path, txt_path=None):
    """
    将epub文件转换为txt文件

    Args:
        epub_path: epub文件路径
        txt_path: 输出txt文件路径，如果为None，则使用默认输出目录中的同名txt文件

    Returns:
        bool: 转换是否成功
    """
    # 检查epub文件是否存在
    if not os.path.exists(epub_path):
        print(f"错误: 文件 '{epub_path}' 不存在")
        return False

    # 如果没有指定txt输出路径，则使用默认输出目录中的同名txt文件
    if txt_path is None:
        # 确保输出目录存在
        os.makedirs(DEFAULT_OUTPUT_DIR, exist_ok=True)

        # 获取epub文件名（不带路径和扩展名）
        epub_filename = os.path.basename(epub_path)
        epub_filename_no_ext = os.path.splitext(epub_filename)[0]

        # 构建输出文件路径
        txt_path = os.path.join(DEFAULT_OUTPUT_DIR, f"{epub_filename_no_ext}.txt")

    # 提取文本
    text_content = epub_to_text(epub_path)

    if text_content is None:
        return False

    # 确保输出文件所在目录存在
    output_dir = os.path.dirname(txt_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # 写入txt文件
    try:
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text_content)
        print(f"转换成功: '{epub_path}' -> '{txt_path}'")
        return True
    except Exception as e:
        print(f"写入文件时出错: {str(e)}")
        return False
