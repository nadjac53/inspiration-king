#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抖音热点爬虫脚本
功能：从抖音热榜 API 获取热点数据，保存为 hot.json
用法：python douyin_hotspot.py
"""

import json
import time
import sys
from datetime import datetime, timezone

try:
    import requests
except ImportError:
    print("错误：未安装 requests 库，请运行 pip install requests")
    sys.exit(0)


# API 地址
API_URL = "https://api.xunjinlu.fun/api/rebang/douyin.php"

# 请求超时时间（秒）
TIMEOUT = 10

# 保存文件路径
OUTPUT_FILE = "hot.json"


def fetch_douyin_hot() -> dict:
    """
    从抖音热榜 API 获取热点数据

    Returns:
        dict: 包含更新时间和热点列表的字典
    """
    try:
        # 发送 GET 请求
        response = requests.get(API_URL, timeout=TIMEOUT)
        response.raise_for_status()  # 如果状态码不是 200，抛出异常

        # 解析 JSON 响应
        data = response.json()

        # 检查 API 返回状态
        if data.get("code") != 200:
            print(f"API 返回错误：{data.get('message', '未知错误')}")
            return None

        # 提取热点列表（取前10条）
        raw_list = data.get("data", {}).get("list", [])[:10]

        # 格式化热点数据
        hotspots = []
        for item in raw_list:
            hotspot = {
                "title": item.get("title", ""),
                "hot_value": item.get("hot_label", ""),
                "url": item.get("url", "")
            }
            hotspots.append(hotspot)

        # 构建返回结果
        result = {
            "update_time": datetime.now(timezone.utc).isoformat(),
            "source": "抖音热榜",
            "hotspots": hotspots
        }

        print(f"成功获取 {len(hotspots)} 条热点数据")
        return result

    except requests.exceptions.Timeout:
        print("错误：API 请求超时")
        return None
    except requests.exceptions.RequestException as e:
        print(f"错误：API 请求失败 - {str(e)}")
        return None
    except json.JSONDecodeError:
        print("错误：JSON 解析失败")
        return None
    except Exception as e:
        print(f"错误：未知异常 - {str(e)}")
        return None


def save_to_json(data: dict) -> bool:
    """
    将数据保存为 JSON 文件

    Args:
        data: 要保存的字典数据

    Returns:
        bool: 保存是否成功
    """
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"数据已保存到 {OUTPUT_FILE}")
        return True
    except IOError as e:
        print(f"错误：文件写入失败 - {str(e)}")
        return False
    except Exception as e:
        print(f"错误：保存失败 - {str(e)}")
        return False


def main():
    """主函数"""
    print("=" * 40)
    print("抖音热点爬虫启动")
    print("=" * 40)

    # 获取热点数据
    data = fetch_douyin_hot()

    # 即使请求失败也不中断程序（GitHub Actions 视为成功）
    if data is None:
        print("警告：无法获取热点数据，将创建空数据结构")
        # 创建空数据以保证 GitHub Actions 正常工作
        data = {
            "update_time": datetime.now(timezone.utc).isoformat(),
            "source": "抖音热榜",
            "hotspots": [],
            "error": "数据获取失败，请稍后重试"
        }

    # 保存数据
    save_to_json(data)

    print("=" * 40)
    print("爬虫执行完成")
    print("=" * 40)


if __name__ == "__main__":
    main()
