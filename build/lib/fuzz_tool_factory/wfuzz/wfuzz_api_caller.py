# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/24
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

from .wfuzz_factory import WfuzzFactory

class WfuzzApiCaller(WfuzzFactory):
    """use api call fuzz api

    """

    def api_caller(self, *args, **kwargs):
        """wfuzz api caller

        :param args: api args
        :param kwargs: api kwargs
        :return:
        """
        print(*args, **kwargs)