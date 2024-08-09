import json
import os

class FileManager:
    
    def load_data(self, filename):
        # TODO:
        # Implement a process that reads the contents of the `filename` file 
        # and returns the text.
        try:
            with open(filename, "r") as file:
                return file.read()
        except IOError:
            print ("File was not found")

    def save_data(self, filename, data):
        # TODO:
        # Implement a process that writes the contents of `data` to the file `filename`
        try:
            with open(filename, "w") as file:
                file.write(data)
        except Exception as e:
            print(f"The following exception occured when trying to write date to file: {e}")
        
    def read_json(self, json_file_path):
        # TODO:
        # Implement a process that reads the contents of a file whose path is stored in the `json_file_path` variable 
        # and returns a list of dictionaries

        try:
            if os.path.exists(json_file_path) and os.path.getsize(json_file_path) > 0:
                with open(json_file_path, "r") as file:
                    file_content = json.load(file)
                    
                if isinstance(file_content, list) and all(isinstance(item, dict) for item in file_content):
                    return file_content
                else:
                    raise ValueError("The json file hist.json contains improper data structure")
                
            else:
                print("File is empty or does not exist. A new list of dictionaries will be initialized")
                file_content = []

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}. A new list of dictionaries will be initialized")
            file_content = []
        except FileNotFoundError:
            print ("The hist.json could not be found. A new list of dictionaries will be initialized")
            file_content = []
        except Exception as e:
                print(f"The following exception occured when trying to open hist.json file: {e}")
                return
        
    def write_json(self, list_of_dicts, json_file_path):
        # TODO:
        # Implement a process that writes a list of dictionaries from list_of_dicts to the `json_file_path` file

        try:
            if isinstance(list_of_dicts, list) and all(isinstance(item, dict) for item in list_of_dicts):
                with open(json_file_path, "w") as file:
                    json.dump(list_of_dicts, file, indent = 4)
            else:
                raise ValueError("The given list of dictionary does not have the right format")
        except FileNotFoundError:
            print(f"The file {json_file_path} was not found")
        except PermissionError:
            print(f"You do not have permission to write to {json_file_path} file")
        except Exception as e:
            print(f"The following error occured: {e}")

    def add_to_json(self, data, json_file_path):
        # TODO:
        # Implement a process that gets the dictionary in the data variable and adds it to the JSON `json_file_path`

        if not isinstance(data, dict):
            raise ValueError("The given data does not have the proper dictionary format")
            
        file_content = self.read_json(json_file_path)
        file_content.append(data)
        self.write_json(file_content, json_file_path)

        




            