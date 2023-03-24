# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/22
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

from fuzz_tool_factory.interface import AbstractFactory


class WfuzzFactory(AbstractFactory):
    """wfuzz factory

    """

    def api_caller(self, *args, **kwargs):
        """wfuzz api caller

        :param args: api args
        :param kwargs: api kwargs
        :return:
        """
        pass
