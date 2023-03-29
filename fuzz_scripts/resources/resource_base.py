# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/27
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

import abc
from abc import ABC
from functools import wraps
from kubernetes_fuzz_tool.src import api_caller_entry


FUZZ_CONFIGURE = "fuzz_configure"
KUBERNETES_BASE = "kubernetes_base"
KUBERNETES_API_BASE = "kubernetes_api_base"
ATTACK_FILE_PATH = "attack_file_path"
FUZZ_CODE_RANGE_NAME = "FUZZ_CODE_RANGE"
FUZZ_HIDE_CODE_RANGE_NAME = "FUZZ_HIDE_CODE_RANGE"
FUZZ_ALL_ATTACK_FILE_PATH_NAME = "FUZZ_ALL_ATTACK_FILE_PATH"

TOOL_TYPE = "tool_type"
TOOL_PARAMETERS = "tool_parameters"
TARGET_URL = "target_url"


class ResourceBase(ABC):
    """resource base interface

    """

    def __init__(self, *args, **kwargs):
        self._kubernetes_base = kwargs.get("%s" % KUBERNETES_BASE)
        self._kubernetes_api_base = kwargs.get("%s" % KUBERNETES_API_BASE)
        self._fuzz_configure = kwargs.get("%s" % FUZZ_CONFIGURE)
        self._attack_file_path = kwargs.get("%s" % ATTACK_FILE_PATH)
        self._fuzz_code_range = self._fuzz_configure.get(FUZZ_CODE_RANGE_NAME)
        self._fuzz_hide_code_range = self._fuzz_configure.get(FUZZ_HIDE_CODE_RANGE_NAME)

    @abc.abstractmethod
    def get(self, fuzz_payload: list[str], fuzz_expression: str):
        pass

    @abc.abstractmethod
    def post(self, fuzz_payload: list[str], fuzz_expression: str):
        pass

    @abc.abstractmethod
    def put(self, fuzz_payload: list[str], fuzz_expression: str):
        pass

    @abc.abstractmethod
    def patch(self, fuzz_payload: list[str], fuzz_expression: str):
        pass

    @abc.abstractmethod
    def delete(self):
        pass

    @staticmethod
    def api_caller(options):
        """ caller api by options

        :param options: caller api options
        :return:
        """
        api_caller_entry(options)

    @staticmethod
    def generate_fuzz_options(tool_type: str, tool_parameters: str, target_url: str) -> dict:
        options = {
            ("%s" % TOOL_TYPE): tool_type,
            ("%s" % TOOL_PARAMETERS): tool_parameters,
            ("%s" % TARGET_URL): target_url
        }
        return options

    @property
    def wfuzz(self):
        return "wfuzz"

    @property
    def connect_delay(self):
        return "1"

    @property
    def response_delay(self):
        return "1"

    @property
    def kubernetes_base(self):
        return self._kubernetes_base

    @property
    def kubernetes_api_base(self):
        return self._kubernetes_api_base

    @property
    def fuzz_configure(self):
        return self._fuzz_configure

    @property
    def attack_file_path(self):
        return self._attack_file_path

    @attack_file_path.setter
    def attack_file_path(self, value):
        self._attack_file_path = value

    @property
    def fuzz_code_range(self):
        return ",".join('%s' % _ for _ in self._fuzz_code_range)

    @property
    def fuzz_hide_code_range(self):
        return ",".join('%s' % _ for _ in self._fuzz_hide_code_range)

def exception_capture(func):
    @wraps(func)
    def catch(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            if "Pycurl" in str(ex) and "Connection timed out" in str(ex):
                print("pycurl connection timed out.")
    return catch