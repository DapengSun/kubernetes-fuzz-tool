# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/22
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

import json

import wfuzz
from fuzz_tool_factory.interface import AbstractFactory


class WfuzzFactory(AbstractFactory):
    """wfuzz factory

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def api_caller(self, *args, **kwargs):
        """wfuzz api caller

        :param args: api args
        :param kwargs: api kwargs
        :return:
        """
        tool_parameters = kwargs.get("tool_parameters")
        command = f"{tool_parameters} -u {self.target_url}"
        print(f"command: wfuzz {command}")

        with wfuzz.get_session(command) as s:
            for r in s.fuzz():
                result = {"code": r.code,
                          "url": r.url,
                          "raw_request": r.history.raw_request,
                          "raw_content": r.history.raw_content,
                          }
                print(json.dumps(result, ensure_ascii=False))
