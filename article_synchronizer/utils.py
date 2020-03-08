import os

import cson
import json
import yaml
from article_synchronizer.logger import error
from article_synchronizer.exceptions.base import *

SLANT = '/'

JSON = "JSON"
YAML = "YAML"
INI = "INI"
RAW = "RAW"
CSON = "CSON"


def get_excute_dir():
    return os.getcwd()


EXCUTE_DIR = get_excute_dir()


def get_all_files_in_dir(dir):
    """return a list of absolute path of files in dir"""
    entrys = os.listdir(dir)
    return [os.path.join(dir, entry)
            for entry in entrys if os.path.isfile(os.path.join(dir, entry))]


def get_all_dirs_in_dir(dir):
    """return a list of absolute path of dirs in dir"""
    return [os.path.join(dir, entry)
            for entry in os.listdir(dir) if os.path.isdir(entry)]

def is_dir_exits(dir):
    if not os.path.isdir(dir):
        dir = os.path.join(EXCUTE_DIR, dir)
        return os.path.isdir(dir)
    return True


def is_path_exists(file_path):
    """We try to find files in excute dir in case the file_path path is not an
    absolute path
    """
    if not os.path.isfile(file_path):
        file_path = os.path.join(EXCUTE_DIR, file_path)
        return os.path.isfile(file_path)
    return True


def get_abs_path(path):
    return os.path.abspath(path)


def remove_slant_before_str(string):
    if string.startswith(SLANT):
        string = string[1:]
    return string


def concatenate_path(root_path, *args):
    args = [remove_slant_before_str(arg) for arg in args]
    return os.path.join(root_path, *args)


def json2dict(content):
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        msg_sche = 'your content {} is not in the right json ' \
                   'style and details are {}'
        error(__file__, msg_sche.format(content, e))


def yaml2dict(content):
    try:
        return yaml.loads(content)
    except yaml.YAMLError as e:
        msg_sche = 'your content {} is not in the right yaml ' \
                   'style and details are {}'
        error(__file__, msg_sche.format(content, e))


def cson2dict(content):
    try:
        return cson.loads(content)
    except cson.ParseError as e:
        msg_sche = 'your content {} is not in the right cson ' \
                   'style and details are {}'
        error(__file__, msg_sche.format(content, e))


def get_file_content(file_path, file_type=RAW):
    """file_type can be json, yaml, ini, raw, cson"""
    file_content = ""
    with open(file_path, 'r') as f:
        file_content = f.read()
    if file_type == RAW:
        return file_content
    elif file_type == JSON:
        return json2dict(file_content)
    elif file_type == YAML:
        return yaml2dict(file_content)
    elif file_type == CSON:
        return cson2dict(file_content)
    else:
        raise UnknownFileTypeException
     
