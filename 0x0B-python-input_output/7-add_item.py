#!/usr/bin/python3
"""
This script creates a JSON file and adds a list
of arguments to it
"""

if __name__ == "__main__":
    import sys
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file")\
        .load_from_json_file

    file_name = "add_items.json"

    try:
        json_list = load_from_json_file(file_name)
    except Exception as e:
        json_list = []

    arg_list = sys.argv[1:]
    save_to_json_file(json_list + arg_list, "add_items.json")
