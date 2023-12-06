# python multi_clipboard.py save
# python multi_clipboard.py load
# python multi_clipboard.py list

import sys
import clipboard
import json

# data = clipboard.paste()
# print(data)
# print(sys.argv[1:])     # gives command line arguments

SAVED_DATA = "clipboard.json"

# keys clip board data
# save data to json file


def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file)

# save_data("test.json", {"key": "value_01"})

# read the data from json file


def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except:
        return {}


# save_data("test.json", {"key": "value"})
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    # print(command)

    if command == 'save':
        key = input("Enter key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        # print("save")

    elif command == 'load':
        key = input("Enter key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key not found")

        # print("load")

    elif command == 'list':
        print(data)
    else:
        print("Invalid command")

else:
    print("plese enter exactly one command")
