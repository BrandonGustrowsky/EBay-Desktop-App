# Brandon Gustrowsky
# first draft 2021-11-29: append_to_json_file and create_json_file added, no doctests
# All functions accessing, modifying, creating, or deleting json files are developed here
import json

def overwrite_json_file(path, overwrite_with_this) -> None:
    '''
    Overwrites the data inside of a json file with new data.
    \n***Parameters***
    \path - The path to the json file who's contents will be overwritten.
    \noverwrite_with_this - What will be put inside the json file after the old data is removed.
    '''
    with open(path, "w") as file:
        json.dump(overwrite_with_this, file, indent=4)

def append_to_json_file(path, element): #If time add: Ability to enter in a list for the 'path' parameter to allow for
                                        #appending to multiple json files with one function call
    '''
Writes data in dictionary form to an already existing json file. To create a new json file, use 'create_json_file'.\n
***Parameters***
\npath - The path to the json file needed to be updated
\nelement - Where the data is stored that will be dumped into the json file.

    '''
    with open(path, "r+") as file:
        data = json.load(file)
        data.append(element)
        file.seek(0)
        json.dump(data, file, indent=4)

def create_json_file(path, file_name):
    '''
Creates new json file, putting an empty list into the file.
\n***Parameters***
\npath - The inclusive path to the json file
\nfile_name - The name of the json file being created
    '''
    with open(f"{path}/{file_name}", "w") as file:
        json.dump([], file)

def read_json_file(path):
    '''
    Reads in a json file as a list object and returns the object
    \n***Parameters***
    \npath - The inclusive path to the json file.
    '''
    with open(path, "r") as file:
            data = list(json.load(file))
            return data
