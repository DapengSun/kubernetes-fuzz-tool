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


class AbstractFactory(ABC):
    """ Defines a abstract factory for use by other fuzz tools

    """

    @abstractmethod
    def api_caller(self, *args, **kwargs):
        """ call fuzz tool implementation apis

        :param args: request args
        :param kwargs: request kwargs
        :return:
        """
        pass
