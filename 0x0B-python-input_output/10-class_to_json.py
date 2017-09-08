#!/usr/bin/python3


def class_to_json(obj):
    """
    class_to_json - returns dictionary description w/simple data structure
    (list, dictionary, string, integer and boolean) for JSON object
    Args:
        obj(unk) - obj to get dictionary of
    Returns:
        dictionary desc of JSON obj
    """
    return obj.__dict__
