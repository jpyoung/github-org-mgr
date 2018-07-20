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
