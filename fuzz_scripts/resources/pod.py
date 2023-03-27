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


class Pod(ResourceBase):
    """pod resource

    """

    def get(self):
        # GET /api/v1/namespaces/{namespace}/pods/{name}
        print("pod instance: fuzz [name] start.")
        options = generate_fuzz_options("%s" % wfuzz,
                                        f"-z list,{FuzzVars.NAMESPACE} " \
                                        f"-z file,{FUZZ_ALL_ATTACK_FILE_PATH} " \
                                        f"--sc {FUZZ_CODE_RANGE} " \
                                        f"{CONNECT_DELAY} " \
                                        f"{RESPONSE_DELAY}",
                                        f"{kubernetes_base}{kubernetes_api_base}/v1/namespace/FUZZ/pods/FUZ2Z?pretty=true")
        api_caller_entry(options)
        print("pod instance: fuzz [name] finish.")

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass