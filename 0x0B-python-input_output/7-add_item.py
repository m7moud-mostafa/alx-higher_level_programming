#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file")\
        .load_from_json_file
    arg_list = sys.argv[1:]
    save_to_json_file(arg_list, "add_items.json")
