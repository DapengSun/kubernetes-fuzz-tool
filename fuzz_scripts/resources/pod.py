# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/27
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

import json

from kubernetes_fuzz_tool.fuzz_scripts.resources.resource_base import ResourceBase

BODY = "body"
NAMESPACE = "namespace"


class Pod(ResourceBase):
    """pod resource

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.namespace = kwargs.get("%s" % NAMESPACE)
        self.body = kwargs.get("%s" % BODY)

    def get(self):
        # GET /api/v1/namespaces/{namespace}/pods/{name}
        print("pod instance: fuzz [name] start.")
        options = ResourceBase.generate_fuzz_options("%s" % self.wfuzz,
                                                     f'-z list,"{self.namespace}" ' \
                                                     f"-z file,{self.attack_file_path} " \
                                                     f"--sc {self.fuzz_code_range} " \
                                                     f"{self.connect_delay} " \
                                                     f"{self.response_delay}",
                                                     f"{self.kubernetes_base}{self.kubernetes_api_base}/v1/namespace/FUZZ/pods/FUZ2Z?pretty=true")
        ResourceBase.api_caller(options)
        print("pod instance: fuzz [name] finish.")

    def post(self):
        # POST /api/v1/namespaces/{namespace}/pods
        print("pod instance: fuzz [name] start.")
        options = ResourceBase.generate_fuzz_options("%s" % self.wfuzz,
                                                     f"-z file,{self.attack_file_path} " \
                                                     f'-z list,"{self.namespace}" ' \
                                                     f'-H "Content-Type:application/json" ' \
                                                     f"-d '{json.dumps(self.body, ensure_ascii=False).replace(' ', '')}' " \
                                                     f"--sc {self.fuzz_code_range} " \
                                                     f"{self.connect_delay} " \
                                                     f"{self.response_delay}",
                                                     f"{self.kubernetes_base}{self.kubernetes_api_base}/v1/namespaces/FUZ2Z/pods?dryRun=True")

        ResourceBase.api_caller(options)
        print("pod instance: fuzz [name] finish.")

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
