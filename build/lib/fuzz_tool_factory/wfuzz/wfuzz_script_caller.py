# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/24
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

import wfuzz
from environs import base_dir
from .wfuzz_factory import WfuzzFactory

TARGET_URL = "target_url"


class WfuzzScriptCaller(WfuzzFactory):
    """use script call fuzz api

    """

    def api_caller(self, *args, **kwargs):
        """wfuzz script caller

        :param args: api args
        :param kwargs: api kwargs
        :return:
        """
        url = kwargs.get("%s" % TARGET_URL)
        wordlist_path = base_dir / "words" / "wordlist/general/common.txt"
        for r in wfuzz.fuzz(url=url,
                            hc=[404],
                            payloads=[("file", dict(fn=wordlist_path))]):
            print(r)
