# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/24
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

from src import api_caller_entry

TOOL_TYPE = "tool_type"
TOOL_PARAMETERS = "tool_parameters"
TARGET_URL = "target_url"


def kubernetes_api_fuzz(tool_type: str, tool_parameters: str, target_url: str):
    values = {
        ("%s" % TARGET_URL): tool_type,
        ("%s" % TOOL_PARAMETERS): tool_parameters,
        ("%s" % TOOL_TYPE): target_url
    }
    api_caller_entry(values)


def kubernetes_apis_fuzz():
    pass


def kubernetes_other_fuzz():
    pass


if __name__ == '__main__':
    print("fuzz kubernetes api start.")
    kubernetes_api_fuzz("wfuzz", "a", "b")
    kubernetes_apis_fuzz()
    kubernetes_other_fuzz()
    print("fuzz kubernetes api successful.")
    print("finish.")
