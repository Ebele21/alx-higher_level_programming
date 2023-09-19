#!/usr/bin/python3
"""
This function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """This is crate and object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
