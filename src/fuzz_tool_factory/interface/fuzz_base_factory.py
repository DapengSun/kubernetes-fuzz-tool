# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/22
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

from abc import ABC, abstractmethod
from utils.fuzz_exception import FuzzToolException

TARGET_URL = "target_url"
TOOL_TYPE = "tool_type"


class AbstractFactory(ABC):
    """ Defines a abstract factory for use by other fuzz tools

    """

    def __init__(self, *args, **kwargs):
        try:
            self._tool_type = kwargs.get("%s" % TOOL_TYPE)
            self._target_url = kwargs.get("%s" % TARGET_URL)
        except Exception as ex:
            raise FuzzToolException("Requires a specified tool type or target URL.")

    @abstractmethod
    def api_caller(self, *args, **kwargs):
        """ call fuzz tool implementation apis

        :param args: request args
        :param kwargs: request kwargs
        :return:
        """
        pass

    @property
    def tool_type(self):
        return self._tool_type

    @property
    def target_url(self):
        return self._target_url
