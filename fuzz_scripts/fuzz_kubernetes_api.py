# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/24
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

from src import api_caller_entry
from fuzz_scripts import base_dir
from fuzz_kubernetes_vars import FuzzVars

WFUZZ = "wfuzz"

TOOL_TYPE = "tool_type"
TOOL_PARAMETERS = "tool_parameters"
TARGET_URL = "target_url"
FUZZ_CODE_RANGE = "301,302,404,500,501,502"
FUZZ_ALL_ATTACK_FILE_PATH = base_dir / "src/words/wordlist/Injections/All_attack.txt"

def kubernetes_api_fuzz(kubernetes_base: str, kubernetes_api_base: str):
    """kubernetes core api

    ref: https://kubernetes.io/zh-cn/docs/reference/kubernetes-api/workload-resources/pod-v1/
    :param kubernetes_base:
    :param kubernetes_api_base:
    :return:
    """

    CONNECT_DELAY = "--conn-delay 5"
    RESPONSE_DELAY = "--req-delay 5"

    # region pod
    # region pod instance
    # region pod instance get
    # GET /api/v1/namespaces/{namespace}/pods/{name}
    print("pod instance: fuzz [name] start.")
    options = generate_fuzz_options("%s" % WFUZZ,
                                    f"-z list,{FuzzVars.NAMESPACE} " \
                                    f"-z file,{FUZZ_ALL_ATTACK_FILE_PATH} " \
                                    f"--sc {FUZZ_CODE_RANGE} " \
                                    f"{CONNECT_DELAY} " \
                                    f"{RESPONSE_DELAY}",
                                    f"{kubernetes_base}{kubernetes_api_base}/v1/namespace/FUZZ/pods/FUZ2Z?pretty=true")
    api_caller_entry(options)
    print("pod instance: fuzz [name] finish.")

    # print("pod instance: fuzz [namespace, name] start.")
    # options = generate_fuzz_options("%s" % WFUZZ,
    #                                 f"-z list,{FuzzVars.NAMESPACE} " \
    #                                 f"-z list,{FuzzVars.FAKE_POD_NAME} " \
    #                                 f"--sc {FUZZ_CODE_RANGE}",
    #                                 f"{kubernetes_base}{kubernetes_api_base}/v1/namespace/FUZZ/pods/FUZ2Z?pretty=true")
    # api_caller_entry(options)
    # print("pod instance: fuzz [namespace, name] finish.")
    #
    # print("pod instance: fuzz [name, pretty] start.")
    # options = generate_fuzz_options("%s" % WFUZZ,
    #                                 f"-z list,{FuzzVars.NAMESPACE} " \
    #                                 f"-z list,{FuzzVars.FAKE_POD_NAME} " \
    #                                 f"--sc {FUZZ_CODE_RANGE}",
    #                                 f"{kubernetes_base}{kubernetes_api_base}/v1/namespace/FUZZ/pods/FUZ2Z?pretty=FUZ3Z")
    # api_caller_entry(options)
    # print("pod instance: fuzz [name, pretty] finish.")
    #
    # print("pod instance: fuzz [namespace, name, pretty] start.")
    # options = generate_fuzz_options("%s" % WFUZZ,
    #                                 f"-z list,{FuzzVars.NAMESPACE} " \
    #                                 f"-z list,{FuzzVars.FAKE_POD_NAME} " \
    #                                 f"--sc {FUZZ_CODE_RANGE}",
    #                                 f"{kubernetes_base}{kubernetes_api_base}/v1/namespace/FUZZ/pods/FUZ2Z?pretty=FUZ3Z")
    # api_caller_entry(options)
    # print("pod instance: fuzz [namespace, name, pretty] finish.")

    # endregion

    # region pod instance post
    # endregion

    # region pod instance put
    # endregion

    # region pod instance patch
    # endregion

    # region pod instance delete
    # endregion
    # endregion
    # region pod ephemeralcontainers
    # region pod ephemeralcontainers get
    # endregion

    # region pod ephemeralcontainers put
    # endregion

    # region pod ephemeralcontainers patch
    # endregion
    # endregion
    # region pod log
    # region pod log get
    # endregion

    # endregion
    # region pod status
    # region pod status get
    # endregion

    # region pod status put
    # endregion

    # region pod status patch
    # endregion
    # endregion
    # region pod list
    # region pod list get
    # endregion

    # region pod list delete
    # endregion
    # endregion
    # endregion


def generate_fuzz_options(tool_type: str, tool_parameters: str, target_url: str) -> dict:
    values = {
        ("%s" % TOOL_TYPE): tool_type,
        ("%s" % TOOL_PARAMETERS): tool_parameters,
        ("%s" % TARGET_URL): target_url
    }
    return values


def kubernetes_apis_fuzz(kubernetes_base: str, kubernetes_apis_base: str):
    pass


def kubernetes_other_fuzz():
    pass


if __name__ == '__main__':
    print("fuzz kubernetes api start.")
    kubernetes_base = "http://192.168.75.100:8080"
    kubernetes_api_base = "/api"
    kubernetes_apis_base = "/apis"
    kubernetes_api_fuzz(kubernetes_base, kubernetes_api_base)
    kubernetes_apis_fuzz(kubernetes_base, kubernetes_apis_base)
    kubernetes_other_fuzz(kubernetes_base)
    print("fuzz kubernetes api successful.")
    print("finish.")
