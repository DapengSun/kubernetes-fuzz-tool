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
from kubernetes_fuzz_tool.fuzz_scripts.resources.resource_base import exception_capture

BODY = "body"
NAMESPACE = "namespace"
POD_NAME = "name"


class Pod(ResourceBase):
    """pod resource

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.body = kwargs.get("%s" % BODY)

    @exception_capture
    def get(self, fuzz_payload: list[str], fuzz_expression: str):
        # GET /api/v1/namespaces/{namespace}/pods/{name}
        print("pod instance: get method fuzzing start.")
        options = ResourceBase.generate_fuzz_options("%s" % self.wfuzz,
                                                     f"-X GET " \
                                                     f'{" ".join(_ for _ in fuzz_payload)} ' \
                                                     f"--sc {self.fuzz_code_range} " \
                                                     f"--hc {self.fuzz_hide_code_range} " \
                                                     f"--conn-delay {self.connect_delay} " \
                                                     f"--req-delay {self.response_delay}",
                                                     f"{self.kubernetes_base}{self.kubernetes_api_base}{fuzz_expression}")
        ResourceBase.api_caller(options)
        print("pod instance: get method fuzzing finish.")

    @exception_capture
    def post(self, fuzz_payload: list[str], fuzz_expression: str):
        # POST /api/v1/namespaces/{namespace}/pods
        print("pod instance: post method fuzzing start.")
        options = ResourceBase.generate_fuzz_options("%s" % self.wfuzz,
                                                     f"-X POST " \
                                                     f'{" ".join(_ for _ in fuzz_payload)} ' \
                                                     f'-H Content-Type:application/json ' \
                                                     f"-d '{json.dumps(self.body, ensure_ascii=False).replace(' ', '')}' " \
                                                     f"--sc {self.fuzz_code_range} " \
                                                     f"--hc {self.fuzz_hide_code_range} " \
                                                     f"--conn-delay {self.connect_delay} " \
                                                     f"--req-delay {self.response_delay}",
                                                     f"{self.kubernetes_base}{self.kubernetes_api_base}{fuzz_expression}")

        ResourceBase.api_caller(options)
        print("pod instance: post method fuzzing finish.")

    @exception_capture
    def put(self, fuzz_payload: list[str], fuzz_expression: str):
        # PUT /api/v1/namespaces/{namespace}/pods/{name}
        print("pod instance: put method fuzzing start.")
        options = ResourceBase.generate_fuzz_options("%s" % self.wfuzz,
                                                     f"-X PUT " \
                                                     f'{" ".join(_ for _ in fuzz_payload)} ' \
                                                     f'-H Content-Type:application/json ' \
                                                     f"-d '{json.dumps(self.body, ensure_ascii=False).replace(' ', '')}' " \
                                                     f"--sc {self.fuzz_code_range} " \
                                                     f"--hc {self.fuzz_hide_code_range} " \
                                                     f"--conn-delay {self.connect_delay} " \
                                                     f"--req-delay {self.response_delay}",
                                                     f"{self.kubernetes_base}{self.kubernetes_api_base}{fuzz_expression}")

        ResourceBase.api_caller(options)
        print("pod instance: put method fuzzing finish.")

    @exception_capture
    def patch(self):
        pass

    @exception_capture
    def delete(self):
        pass
