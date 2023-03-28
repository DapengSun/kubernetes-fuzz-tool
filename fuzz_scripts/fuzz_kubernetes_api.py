# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/24
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

import json

import requests as requests
import yaml
from kubernetes_fuzz_tool.fuzz_scripts import base_dir
from kubernetes_fuzz_tool.fuzz_scripts.fuzz_kubernetes_vars import FuzzVars
from kubernetes_fuzz_tool.fuzz_scripts.resources.pod import Pod

WFUZZ = "wfuzz"

TOOL_TYPE = "tool_type"
TOOL_PARAMETERS = "tool_parameters"
TARGET_URL = "target_url"
FUZZ_ALL_ATTACK_FILE_PATH_NAME = "FUZZ_ALL_ATTACK_FILE_PATH"


def create_fuzz_resources(kubernetes_base: str, kubernetes_api_base: str):
    create_fuzz_namespace(kubernetes_base, kubernetes_api_base)


def create_fuzz_namespace(kubernetes_base: str, kubernetes_api_base: str):
    with open(base_dir / "fuzz_scripts/resource_metadata/fuzz_namespace.json", 'r') as load_f:
        body = json.load(load_f)
    request_url = f"{kubernetes_base}{kubernetes_api_base}/v1/namespaces"
    header = {
        "Content-Type": "application/json"
    }
    # 发送post请求
    try:
        response = requests.post(url=request_url, json=body, headers=header, timeout=5)
        if response.json().get("code") == 409:
            print(response.json().get("message"))
        else:
            print(response.json())
    except Exception as ex:
        print(ex)


def kubernetes_api_fuzz(kubernetes_base: str, kubernetes_api_base: str, fuzz_configure: dict):
    """kubernetes core api

    ref: https://kubernetes.io/zh-cn/docs/reference/kubernetes-api/workload-resources/pod-v1/
    :param kubernetes_base:
    :param kubernetes_api_base:
    :return:
    """
    metadata_path = base_dir / "fuzz_scripts/resource_metadata"
    injection_file_path = base_dir / "src/words/wordlist/Injections/All_attack.txt"
    general_file_path = base_dir / "src/words/wordlist/general/big.txt"

    # region pre handle: create fuzz namespace, create fuzz pods...
    create_fuzz_resources(kubernetes_base, kubernetes_api_base)
    # endregion

    # region pod
    # region pod instance
    # region pod instance POST
    with open(metadata_path / "fuzz_pod.json", 'r') as load_f:
        body = json.load(load_f)


    pod_fuzz_injections = Pod(kubernetes_base=kubernetes_base,
                              kubernetes_api_base=kubernetes_api_base,
                              fuzz_configure=fuzz_configure,
                              attack_file_path=injection_file_path,
                              namespace=FuzzVars.NAMESPACE,
                              body=body)
    pod_fuzz_injections.post()

    pod_fuzz_general = Pod(kubernetes_base=kubernetes_base,
                           kubernetes_api_base=kubernetes_api_base,
                           fuzz_configure=fuzz_configure,
                           attack_file_path=general_file_path,
                           namespace=FuzzVars.NAMESPACE,
                           body=body)
    pod_fuzz_general.post()
    # endregion

    # region pod instance GET
    # GET /api/v1/namespaces/{namespace}/pods/{name}
    # pod = Pod(kubernetes_base=kubernetes_base,
    #           kubernetes_api_base=kubernetes_api_base,
    #           fuzz_configure=fuzz_configure,
    #           namespace=NAMESPACE)
    # pod.get()

    # print("pod instance: fuzz [namespace, name, pretty] start.")
    # options = generate_fuzz_options("%s" % WFUZZ,
    #                                 f"-z list,{FuzzVars.NAMESPACE} " \
    #                                 f"-z list,{FuzzVars.FAKE_POD_NAME} " \
    #                                 f"--sc {FUZZ_CODE_RANGE}",
    #                                 f"{kubernetes_base}{kubernetes_api_base}/v1/namespace/FUZZ/pods/FUZ2Z?pretty=FUZ3Z")
    # api_caller_entry(options)
    # print("pod instance: fuzz [namespace, name, pretty] finish.")

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

    # region pre handle: clear fuzz namespace, create fuzz pods...
    # endregion


def kubernetes_apis_fuzz(kubernetes_base: str, kubernetes_apis_base: str, fuzz_configure: dict):
    pass


def kubernetes_other_fuzz(kubernetes_base: str):
    pass


if __name__ == '__main__':
    print("fuzz kubernetes api start.")
    kubernetes_base = "http://192.168.75.100:8080"
    kubernetes_api_base = "/api"
    kubernetes_apis_base = "/apis"

    fuzz_config = base_dir / "fuzz_config.yaml"
    with open(fuzz_config) as f:
        fuzz_configure = yaml.load(f, Loader=yaml.FullLoader)

    kubernetes_api_fuzz(kubernetes_base, kubernetes_api_base, fuzz_configure)
    kubernetes_apis_fuzz(kubernetes_base, kubernetes_apis_base, fuzz_configure)
    kubernetes_other_fuzz(kubernetes_base)
    print("fuzz kubernetes api successful.")
    print("finish.")
