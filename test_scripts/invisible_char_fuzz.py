# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/4/3
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

import copy
import json
from time import sleep

import requests

from fuzz_scripts import base_dir

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Host": "192.168.75.105:8080",
    "Accept": "*/*",
    "Content-Type": "application/json; charset=UTF-8"
}

invisible_char_ls = list(set([chr(int(a, 16)) for a in """
00 90 ff 53 4d 72 18 c8 6d 02 50 43 20 4e 45 54 57 4f 52 4b 20 50 4e 47 52 41 4d 31 2e 30 02 4c 4e 41 4d 57 69 6e 64 6f 
77 73 66 6f 72 57 6b 67 70 73 33 31 61 4c 32 58 30 41 32 
""".split()]))


def generate_fuzz_string(target_value, fuzz_values, fuzz_functon):
    target_value_ls = list(target_value)
    if isinstance(fuzz_values, list):
        for fuzz_ in fuzz_values:
            yield from fuzz_functon(target_value_ls, fuzz_)


def insert_fuzz_value(target_value_ls, fuzz_value):
    for index in range(len(target_value_ls) + 1):
        new_target_value_ls = copy.deepcopy(target_value_ls)
        new_target_value_ls.insert(index, fuzz_value)
        res = ''.join(new_target_value_ls)
        yield res


def replace_fuzz_value(target_value_ls, fuzz_value):
    for index in range(len(target_value_ls)):
        new_target_value_ls = copy.deepcopy(target_value_ls)
        new_target_value_ls[index] = fuzz_value
        res = ''.join(new_target_value_ls)
        yield res


def generate_fuzz_headers():
    for key, value in headers.items():
        for fuzz_value in generate_fuzz_string(headers.get(key), invisible_char_ls, insert_fuzz_value):
            new_headers = copy.deepcopy(headers)
            new_headers[key] = fuzz_value
            yield new_headers
        for fuzz_value in generate_fuzz_string(headers.get(key), invisible_char_ls, replace_fuzz_value):
            new_headers = copy.deepcopy(headers)
            new_headers[key] = fuzz_value
            yield new_headers


if __name__ == '__main__':
    for fuzz_header in generate_fuzz_headers():
        pod_metadata_path = base_dir / "fuzz_scripts/resource_metadata/actual_metadata/pod.json"
        with open(pod_metadata_path, 'r') as load_f:
            body = json.load(load_f)
        response = requests.post("http://192.168.75.100:8080", headers=fuzz_header, json=body, timeout=2)
        # 查看响应状态码
        print(response.status_code)
        # 查看响应头部字符编码
        print(response.encoding)
        # 查看完整url地址
        print(response.url)
        # 查看响应内容，response.text 返回的是Unicode格式的数据
        print(response.text)
        sleep(10)
