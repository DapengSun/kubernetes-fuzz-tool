# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/23
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'


class FuzzToolException(Exception):
    """ fuzz tool exception
    """

    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo
