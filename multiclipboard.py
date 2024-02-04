import sys
import clipboard
import json


SAVED_DATA = "clipboard.json"


def save_data(filepath, data):    # Creating a function with filepath and dara as inputs
    with open(filepath, "w") as f:    # Opening/Creating that file in "w">write mode and aliasing it as f
        json.dump(data, f)    # Dumping the "data" passed in json file using the function


def load_data(filepath):    # This function take filepath as input
    try:    # this tries the code in it if it fails it moves to execute "except"
        with open(filepath, "r") as f:    # Opens it in read mode
            data = json.load(f)    # Gives us the data present in the json file as a python dictionary
            return data
    except:
        return {}


if len(sys.argv) == 2:    # Checks if theres 2 input arguments
    command = sys.argv[1]    # Takes the argument at index 1
    data = load_data(SAVED_DATA)    # loads the information resent in variable "data" in "SAVED_DATA"
     
    if command == "save":    # Takes the key from user and save anything which already exists on clipboard to save it as a value for that key
        key = input("Please enter key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")
    
    elif command == "load":    # Takes the key from user and loads the keys value on the clipboard (if it exists, otherwise prints message)
        key = input("Please enter key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard!")
        else:
            print("Key does not exist.")
    
    elif command == "list":    # Gives the python dictionary containing all the clipboard items user has saved
        print(data)
    
    else:    # Prints message if unknown command is passed
        print("Unknown Command")

else:    # Prints message if more than 1 command is passed
    print("Please enter exactly one command")

# The file is run on Mac Terminal
# Sample input output

# Automate_projects % python multiclipboard.py save  
# Please Enter Key: Name
# Data saved!
# Automate_projects % python multiclipboard.py load
# Please enter key: Name
# Data copied to clipboard!
    
# Automate_projects % python multiclipboard.py save
# Please enter key: Email
# Data saved!
# Automate_projects % python multiclipboard.py load
# Please enter key: Email
# Data copied to clipboard!
    
# Automate_projects % python multiclipboard.py list
# {'Name': 'Pranav Pulkundwar', 'Email': 'pulkundwar.p@northeastern.edu'}