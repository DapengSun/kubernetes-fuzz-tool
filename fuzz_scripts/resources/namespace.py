# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/27
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

from fuzz_scripts.resources.resource_base import ResourceBase

FUZZ_ALL_ATTACK_FILE_PATH_NAME = "FUZZ_ALL_ATTACK_FILE_PATH"


class Namespace(ResourceBase):
    """namespace resource

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._post_body = kwargs.get("body")

    def get(self):
        pass

    def post(self):
        body = """
            {
                "kind":"Namespace",
                "apiVersion":"v1",
                "metadata":{
                    "name":"fuzz-dev",
                    "labels":{
                        "name":"fuzz-dev"
                    }
                }
            }
        """

        options = ResourceBase.generate_fuzz_options("%s" % self.wfuzz,
                                                     f"-z file,{self.attack_file_path} " \
                                                     f"-d,{body}"
                                                     f"--sc {self.fuzz_code_range} " \
                                                     f"{self.connect_delay} " \
                                                     f"{self.response_delay}",
                                                     f"{self.kubernetes_base}{self.kubernetes_api_base}/v1/namespaces")
        ResourceBase.api_caller(options)

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
