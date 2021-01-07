import json
import logging
import os
import sys
import numbers
import collections
import pkgutil
import semver

from .asset_capabilities import AssetCapabilities

logger = logging.getLogger('palazzetti_sdk_asset_parser')

class AssetParser(object):
    """Parse dynamic and static data to obtain Product capabilities

    Args:
        get_alls (dict, optional): GET ALLS response data payload
        get_stdt (dict, optional): GET STDT reponse data payload

    """

    def __init__(self, get_alls=None, get_stdt=None):
        self._grammar = json.loads(pkgutil.get_data(__name__, "data/asset_parser.json").decode())
        self._alls = get_alls
        self._stdt = get_stdt

    @property
    def alls(self):
        """dict: Dynamic data structure."""
        return self._alls

    @property
    def stdt(self):
        """dict: Static data structure."""
        return self._stdt

    @alls.setter
    def alls(self, value):
        self._alls = {**self._alls, **value}

    @stdt.setter
    def stdt(self, value):
        self._stdt = {**self._stdt, **value}

    @property
    def parsed_data(self):
        """dict: Parsed data structure."""
        return AssetCapabilities(self.__parse())

    def __dict(self, key):
        _dict = {'GET_ALLS': self.alls, 'GET_STDT': self.stdt}

        return _dict[key]

    def __value(self, dict_name, key):
        k = key
        source_dict = self.__dict(dict_name)

        if (k is None) or (source_dict is None):
            return None

        if (k in source_dict) is False:
            return None

        return source_dict[k]

    def __formatted_version(self, raw_version=""):

        version_parts = raw_version.replace('\n','').replace('\r','').split(".")

        version = collections.defaultdict(int) # default to zero, change as needed
        for n, x in enumerate(version_parts):
            version[n] = x

        return (version[0] or "0") + "." + (version[1] or "0") + "." + (version[2] or "0")

    def __evaluate(self, statement):

        optional_value = self.__value(statement["path"], statement["key"])
        operator = statement["operator"].lower()

        if optional_value is None:
            return False

        if operator == "in":
            try:
                return True if int(optional_value) in map(int, statement["value"]) else False
            except:
                return False

        if operator == "nin":
            try:
                return True if int(optional_value) not in map(int, statement["value"]) else False
            except Exception as e:
                return False

        if operator == "eq":
            try:
                return True if int(optional_value) == int(statement["value"]) else False
            except Exception as e:
                return False

        if operator == "neq":
            try:
                return True if int(optional_value) != int(statement["value"]) else False
            except:
                return False

        if operator == "gt":
            try:
                return True if int(optional_value) > int(statement["value"]) else False
            except:
                return False

        if operator == "lt":
            try:
                return True if int(optional_value) < int(statement["value"]) else False
            except:
                return False

        if operator == "gte":
            try:
                return True if int(optional_value) >= int(statement["value"]) else False
            except:
                return False

        if operator == "lte":
            try:
                return True if int(optional_value) <= int(statement["value"]) else False
            except:
                return False

        if operator == "vgt":
            try:
                return True if semver.compare(self.__formatted_version(optional_value), self.__formatted_version(statement["value"])) > 0 else False
            except Exception as e:
                return False

        if operator == "vgte":
            try:
                return True if semver.compare(self.__formatted_version(optional_value), self.__formatted_version(statement["value"])) >= 0 else False
            except:
                return False

        return False  

    def __parse(self):

        parsed_object = {}

        for curr_key in self._grammar.keys():
            curr_value = self._grammar[curr_key]

            if isinstance(curr_value, list):

                evaluation_result = list(filter(lambda x: False if self.__evaluate(x) else True, curr_value))

                if not evaluation_result: parsed_object[curr_key] = True
                else: parsed_object[curr_key] = False

                continue

            if isinstance(curr_value, dict):

                raw_value = self.__value(curr_value["path"], curr_value["key"])

                if raw_value is None:
                    continue

                if (("map_keys" not in curr_value) or (curr_value["map_keys"] is None)) and (isinstance(raw_value, list) is False):
                    try:
                        parsed_object[curr_key] = raw_value
                    except:
                        continue
                    continue

                # support array of int
                if (("map_keys" not in curr_value) or (curr_value["map_keys"] is None)) and (isinstance(raw_value, list) is True):
                    try:
                        parsed_object[curr_key] = list(map(int, raw_value))
                    except:
                        continue
                    continue

                source_array = curr_value["map_keys"]
                index = int(raw_value)

                if (source_array is None) or (isinstance(index, numbers.Number) is False):
                    continue

                if (index >= len(source_array)):
                    continue

                if (("map_path" not in curr_value) or (curr_value["map_path"] is None)):
                    parsed_object[curr_key] = source_array[index]
                    continue

                computed_value = self.__value(curr_value["map_path"], source_array[index])
                parsed_object[curr_key] = computed_value if computed_value is not None else ""
                
                continue

            if isinstance(curr_value, numbers.Number):
                parsed_object[curr_key] = int(curr_value) if type(curr_value) == int else float("{:.2f}".format(curr_value))

                continue

            if type(curr_value) == bool:
                parsed_object[curr_key] = True if curr_value else False

                continue

            parsed_object[curr_key] = curr_value

        return json.loads(json.dumps(parsed_object))
