import hashlib
import argparse
from tqdm import tqdm
import os


def calculate_md5(file_path):
    # 创建 md5 对象
    md5_hash = hashlib.md5()

    # 获取文件大小
    file_size = os.path.getsize(file_path)

    try:
        with open(file_path, "rb") as f:
            # 创建一个 tqdm 进度条对象，设置总大小为文件大小
            with tqdm(total=file_size, unit="B", unit_scale=True, desc="计算MD5") as pbar:
                # 每次读取文件的一部分
                while chunk := f.read(8192):
                    md5_hash.update(chunk)  # 更新 md5 对象
                    pbar.update(len(chunk))  # 更新进度条
        return md5_hash.hexdigest()
    except FileNotFoundError:
        return f"文件 {file_path} 未找到。"
    except Exception as e:
        return f"计算MD5时发生错误: {e}"


def main():
    # 创建命令行解析器
    parser = argparse.ArgumentParser(description="计算文件的MD5值")
    parser.add_argument("file_path", help="要计算MD5的文件路径")

    # 解析命令行参数
    args = parser.parse_args()

    # 输出文件的MD5值
    print("文件的MD5值是:", calculate_md5(args.file_path))


if __name__ == "__main__":
    main()
