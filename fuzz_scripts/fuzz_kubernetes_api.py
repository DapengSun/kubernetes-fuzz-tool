# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/24
   Description :
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

import copy
import json

import requests as requests
import yaml
from kubernetes_fuzz_tool.fuzz_scripts import base_dir
from kubernetes_fuzz_tool.fuzz_scripts.fuzz_kubernetes_vars import FuzzVars
from kubernetes_fuzz_tool.fuzz_scripts.resources.pod import Pod

from fuzz_scripts.resources.persistent_volume import PersistentVolume

WFUZZ = "wfuzz"
TOOL_TYPE = "tool_type"
TOOL_PARAMETERS = "tool_parameters"
TARGET_URL = "target_url"
FUZZ_ALL_ATTACK_FILE_PATH_NAME = "FUZZ_ALL_ATTACK_FILE_PATH"
APPLICATION_JSON = "application/json"
CONTENT_TYPE = "Content-Type"


def initialize_resources(kubernetes_base: str, kubernetes_api_base: str):
    """initialize_resources

    The fuzzing api needs to initialize some resources in advance.
    :param kubernetes_base: kubernetes base url path
    :param kubernetes_api_base: kubernetes api base url path
    """
    # initialize namespace resource
    namespace_metadata_path = base_dir / "fuzz_scripts/resource_metadata/actual_metadata/namespace.json"
    send_request_to_initialize_resource(
        request_url=f"{kubernetes_base}{kubernetes_api_base}/v1/namespaces",
        header={
            ("%s" % CONTENT_TYPE): ("%s" % APPLICATION_JSON)
        },
        metadata_path=namespace_metadata_path)

    # initialize pod resource
    pod_metadata_path = base_dir / "fuzz_scripts/resource_metadata/actual_metadata/pod.json"
    send_request_to_initialize_resource(
        request_url=f"{kubernetes_base}{kubernetes_api_base}/v1/namespaces/{FuzzVars.NAMESPACE}/pods",
        header={
            ("%s" % CONTENT_TYPE): ("%s" % APPLICATION_JSON)
        },
        metadata_path=pod_metadata_path)


def send_request_to_initialize_resource(request_url: str, header: dict, metadata_path: str):
    """send request

    :param request_url: reqeust url
    :param header: header
    :param metadata_path: resource metadata file path
    """
    with open(metadata_path, 'r') as load_f:
        body = json.load(load_f)
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
    :param kubernetes_base: kubernetes base url path
    :param kubernetes_api_base: kubernetes api base url path
    :return:
    """
    actual_metadata_path = base_dir / "fuzz_scripts/resource_metadata/actual_metadata"
    fuzz_metadata_path = base_dir / "fuzz_scripts/resource_metadata/fuzz_metadata"
    injection_file_path = base_dir / "src/words/wordlist/Injections/All_attack.txt"
    general_file_path = base_dir / "src/words/wordlist/general/big.txt"

    # region inti resources: create fuzz namespace, create fuzz pods...
    initialize_resources(kubernetes_base, kubernetes_api_base)
    # endregion

    # region pod
    # region pod instance
    pod_body = dict()
    with open(fuzz_metadata_path / "pod.json", 'r') as load_f:
        pod_body = json.load(load_f)

    # region pod instance GET
    fuzz_configure.update({
        "FUZZ_HIDE_CODE_RANGE": [422]
    })
    pod_fuzz_obj = Pod(kubernetes_base=kubernetes_base,
                       kubernetes_api_base=kubernetes_api_base,
                       fuzz_configure=fuzz_configure)
    fuzz_payload = [
        f"-z file,{injection_file_path}"
    ]
    fuzz_expression = f"/v1/namespaces/{FuzzVars.NAMESPACE}/pods/{FuzzVars.POD_NAME}?pretty=FUZZ"
    pod_fuzz_obj.get(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression)
    fuzz_payload = [
        f"-z file,{general_file_path}"
    ]
    pod_fuzz_obj.get(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression)
    # endregion

    # region pod instance POST
    pod_fuzz_obj = Pod(kubernetes_base=kubernetes_base,
                       kubernetes_api_base=kubernetes_api_base,
                       fuzz_configure=fuzz_configure,
                       body=pod_body)
    fuzz_payload = [
        f"-z file,{injection_file_path}"
    ]
    fuzz_expression = f"/v1/namespaces/{FuzzVars.NAMESPACE}/pods?dryRun=All"
    pod_fuzz_obj.post(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression)
    fuzz_payload = [
        f"-z file,{general_file_path}"
    ]
    pod_fuzz_obj.post(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression)
    # endregion

    # region pod instance PUT
    modify_pod_body = copy.deepcopy(pod_body)
    modify_pod_body["metadata"]["name"] = FuzzVars.POD_NAME
    pod_fuzz_obj = Pod(kubernetes_base=kubernetes_base,
                       kubernetes_api_base=kubernetes_api_base,
                       fuzz_configure=fuzz_configure,
                       body=modify_pod_body)
    fuzz_payload = [
        f"-z file,{injection_file_path}"
    ]
    fuzz_expression = f"/v1/namespaces/{FuzzVars.NAMESPACE}/pods/{FuzzVars.POD_NAME}?dryRun=All&fieldManager=FUZZ&pretty=True"
    pod_fuzz_obj.put(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression)
    fuzz_payload = [
        f"-z file,{general_file_path}"
    ]
    fuzz_expression = f"/v1/namespaces/{FuzzVars.NAMESPACE}/pods/{FuzzVars.POD_NAME}?dryRun=All&fieldValidation=FUZZ&pretty=True"
    pod_fuzz_obj.put(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression)
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

    # region persistent volume
    pv_body = dict()
    with open(fuzz_metadata_path / "persistent_volume/delete.json", 'r') as load_f:
        pv_body = json.load(load_f)

    # region persistent volume GET
    fuzz_configure.update({
        "FUZZ_HIDE_CODE_RANGE": [404]
    })
    persistent_volume_fuzz_obj = PersistentVolume(kubernetes_base=kubernetes_base,
                                                  kubernetes_api_base=kubernetes_api_base,
                                                  fuzz_configure=fuzz_configure)
    fuzz_payload = [
        f"-z file,{injection_file_path}"
    ]
    fuzz_expression = f"/v1/persistentvolumes/FUZZ"
    persistent_volume_fuzz_obj.get(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression)
    # endregion

    # region persistent volume DELETE
    fuzz_configure.update({
        "FUZZ_HIDE_CODE_RANGE": [404]
    })
    modify_body = copy.deepcopy(pv_body)
    persistent_volume_fuzz_obj = PersistentVolume(kubernetes_base=kubernetes_base,
                                                  kubernetes_api_base=kubernetes_api_base,
                                                  fuzz_configure=fuzz_configure,
                                                  body=pv_body)
    fuzz_payload = [
        f"-z file,{injection_file_path}"
    ]
    fuzz_expression = f"/v1/persistentvolumes/fake-pv-name"

    modify_body = copy.deepcopy(pv_body)
    modify_body["apiVersion"] = "FUZZ"
    persistent_volume_fuzz_obj.delete(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression, body=modify_body)

    modify_body = copy.deepcopy(pv_body)
    modify_body["kind"] = "FUZZ"
    persistent_volume_fuzz_obj.delete(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression, body=modify_body)

    modify_body = copy.deepcopy(pv_body)
    modify_body["gracePeriodSeconds"] = "FUZZ"
    persistent_volume_fuzz_obj.delete(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression, body=modify_body)

    modify_body = copy.deepcopy(pv_body)
    modify_body["orphanDependents"] = "FUZZ"
    persistent_volume_fuzz_obj.delete(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression, body=modify_body)

    modify_body = copy.deepcopy(pv_body)
    modify_body["preconditions"] = "FUZZ"
    persistent_volume_fuzz_obj.delete(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression, body=modify_body)

    modify_body = copy.deepcopy(pv_body)
    modify_body["propagationPolicy"] = "FUZZ"
    persistent_volume_fuzz_obj.delete(fuzz_payload=fuzz_payload, fuzz_expression=fuzz_expression, body=modify_body)
    # endregion

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
