# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Authors :       sundapeng.sdp
   Date：          2023/3/22
   Description :   fuzz tool project entry file
-------------------------------------------------
"""
__author__ = 'sundapeng.sdp'

import optparse

import pkg_resources
from fuzz_tool_factory import AbstractFactory, WfuzzFactory
from utils import FuzzToolException, CALLER_TYPE

TARGET_URL = "target_url"
TOOL_PARAMETERS = "tool_parameters"
TOOL_TYPE = "tool_type"
FUZZ_TOOL_TYPE_NOT_SPECIFIED = "The fuzz tool type should be specified."
NO_FUZZ_TOOL_LOADED = "At least one fuzz tool is loaded."
FUZZ_TOOL_TYPES = "fuzz_types"


def get_fuzz_tool(tool_type: str, usage: str, caller_type: CALLER_TYPE) -> AbstractFactory:
    """ get fuzz tools from installed plugins

    :param tool_type: fuzz tool type (wfuzz...)
    :param usage: fuzz tool usage
    :param caller_type: CALLER_TYPE(API / SCRIPT...)
    :return: factory class integrating AbstractFactory
    """
    tools = {}
    # load installed fuzz tools into tools dict
    for entry_point in pkg_resources.iter_entry_points("%s" % FUZZ_TOOL_TYPES):
        tools[entry_point.name] = entry_point.load()

    if not tool_type:
        if usage:
            print(usage)
        return

    if len(tools) == 0:
        raise FuzzToolException(NO_FUZZ_TOOL_LOADED)

    # get tool by type and return tool instance
    # caller_type_lower_name = caller_type.name.lower()
    # tool = tools[f"{tool_type}_{caller_type_lower_name}"]
    tool = tools[f"{tool_type}"]
    return tool


def script_entry(options: optparse.Values, usage: str):
    """ script entry

    When the user uses the command line as input, call this method to execute the script
    :param options: parameters
    :return:
    """
    # accept the specified parameters for script execution
    target_url, tool_parameters, tool_type = parser_fuzz_parameters(options, CALLER_TYPE.SCRIPT)
    call_fuzz_tool_api(target_url, tool_parameters, tool_type, usage, CALLER_TYPE.SCRIPT)


def api_caller_entry(values: dict):
    """ api caller entry

    When the user uses api as input, call this method to execute the script
    :param values: parameters
    :return:
    """
    # accept the specified parameters for api caller
    target_url, tool_parameters, tool_type = parser_fuzz_parameters(values, CALLER_TYPE.API)
    # call fuzz tool api
    call_fuzz_tool_api(target_url, tool_parameters, tool_type, None, CALLER_TYPE.API)


def call_fuzz_tool_api(tool_type: str, tool_parameters: str, target_url: str, usage: str, caller_type: CALLER_TYPE):
    """ call fuzz tool api

    :param tool_type: tool type
    :param tool_parameters: tool parameters
    :param target_url: target url
    :param usage: usage
    :param caller_type: CALLER_TYPE
    :return:
    """
    # abstract factory generates tool instance
    tool = get_fuzz_tool(tool_type, usage, caller_type)
    if tool:
        try:
            tool(tool_type=tool_type, target_url=target_url).api_caller(tool_parameters=tool_parameters)
        except Exception as ex:
            raise ex


def parser_fuzz_parameters(options, caller_type: CALLER_TYPE):
    """ parser fuzz parameters

    :param options: options
    :param caller_type: CALLER_TYPE
    :return:
    """
    if caller_type is CALLER_TYPE.SCRIPT:
        tool_type = options.tool_type
        tool_parameters = options.tool_parameters
        target_url = options.target_url
    else:
        tool_type = options.get("%s" % TOOL_TYPE)
        tool_parameters = options.get("%s" % TOOL_PARAMETERS)
        target_url = options.get("%s" % TARGET_URL)
    return tool_type, tool_parameters, target_url


if __name__ == '__main__':
    usage = """
                usage: [-t <tool_type>] -p <tool_parameters> -u <url>

                usage: -t wfuzz -p "-c -z file, wordlist/general/big.txt" -u https://xxxx.xxxx.xxxx
                """
    parser = optparse.OptionParser(usage)

    parser.add_option("-t", "--tool_type", dest="tool_type", help="The fuzz tool name of your chosen.")
    parser.add_option("-p", "--tool_parameters", dest="tool_parameters",
                      help="The fuzz tool executes the specified parameters.")
    parser.add_option("-u", "--target_url", dest="target_url", help="The target URL to be fuzzed.")
    (options, args) = parser.parse_args()
    script_entry(options, usage)
