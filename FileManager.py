import json

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
            with open(json_file_path, "r") as file:
                data = json.load(file)

            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                return data
            else:
                raise ValueError("Give JSON file does not contain a list of dictionaries")
        except FileNotFoundError:
            print(f"The file {json_file_path} was not found")
        except json.JSONDecodeError:
            print("The file does not have a valid JSON format")
        except Exception as e:
            print(f"The following error has been encountered: {e}")
        
    def write_json(self, list_of_dicts, json_file_path):
        # TODO:
        # Implement a process that writes a list of dictionaries from list_of_dicts to the `json_file_path` file
        try:
            if isinstance(list_of_dicts, list) and all(isinstance(item, dict) for item in list_of_dicts):
                with open(json_file_path, "w") as file:
                    json.dump(list_of_dicts, file, indent = 4)
                print(f"The list of dictionaries was written to {json_file_path}")
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
        try:
            if not isinstance(data, dict):
                raise ValueError("The given data does not have the proper dictionary format")
            try:
                with open(json_file_path, "r") as file:
                    file_content = json.load(file)

                    if not isinstance(file_content, list) and not all(isinstance(item, dict) for item in file_content):
                        raise ValueError(f"The given file path does not contain a list of dictionaries. Please check format")
                                
            except FileNotFoundError:
                print(f"The file {json_file_path} was not found")
            except Exception as e:
                print(f"The following error occured: {e}")

            file_content.append(data)

            with open(json_file_path, "w") as file:
                json.dumps(file_content, file, indent = 4)
                print(f"Dictionary was succesfully added to the file {json_file_path}")

        except PermissionError:
            print(f"You do not have permission to write to {json_file_path} file")
        except Exception as e:
            print(f"The following error occured: {e}")




            