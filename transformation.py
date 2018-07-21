__author__ = 'john.young'


# Return a copy of the object, filtered to only have values for the
# whitelisted keys (or array of valid keys).
def include_keys(dictionary, keys):
    """
    Filters a dict by only including certain keys.
    :rtype: dict
    """
    key_set = set(keys) & set(dictionary.keys())
    return {key: dictionary[key] for key in key_set}


def exclude_keys(dictionary, keys):
    """
    Filters a dict by excluding certain keys.
    :rtype: dict
    """
    key_set = set(dictionary.keys()) - set(keys)
    return {key: dictionary[key] for key in key_set}


def list_diff(keys1, keys2):
    """
    Return the difference of two lists as a new list.
    :param keys1:
    :param keys2:
    :return: list
    """
    #return list(set(keys1) - set(keys2))
    return list(set(keys1).difference(set(keys2)))
