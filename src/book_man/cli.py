#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
from book_man.epub_converter import convert_epub_to_txt


def main():
    """电子书管理工具主函数"""
    parser = argparse.ArgumentParser(description="电子书管理工具 - 支持epub转txt格式")

    # 添加子命令
    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # epub到txt转换命令
    epub_to_txt_parser = subparsers.add_parser(
        "epub2txt", help="将epub文件转换为txt格式"
    )
    epub_to_txt_parser.add_argument("epub_path", help="epub文件路径")
    epub_to_txt_parser.add_argument(
        "-o", "--output", dest="txt_path", help="输出txt文件路径"
    )

    # 解析命令行参数
    args = parser.parse_args()

    # 如果没有提供命令，显示帮助信息
    if args.command is None:
        parser.print_help()
        return

    # 执行对应的命令
    if args.command == "epub2txt":
        success = convert_epub_to_txt(args.epub_path, args.txt_path)
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
