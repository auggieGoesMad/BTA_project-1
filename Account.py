import json
import os

from FileManager import FileManager
from HistoryMessages import HistoryMessages

class Account:
    def __init__(self, balance = 0):
        self.balance = balance
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
        # TODO:
        # Comment and refine the code below so that the dictionary 
        # from hist_dict is added to hist.json
        if not isinstance(hist_dict, dict):
                raise ValueError("The given history dictionary parameter value is not a proper dictionary")
        
        file_content = []
        try:
            if os.path.exists(self.hist_file_path) and os.path.getsize(self.hist_file_path) > 0:
                with open(self.hist_file_path, "r") as file:
                    file_content = json.load(file)
                    
                if not isinstance(file_content, list) and not all(isinstance(item, dict) for item in file_content):
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
        file_content.append(hist_dict)

        try:
            with open(self.hist_file_path, "w") as file:
                json.dump(file_content, file)
                #print("New history dictionary was added to hist.json file")
        
        except PermissionError:
            print("You do not have permission to write to hist.json file")

        except Exception as e:
            print(f"The following error occured when trying to open for writing for/in hist.json file: {e}")



        # self.file_manager 

    def deposit(self, amount):
        # TODO:
        # implement the deposit process with all necessary checks
        # amount must be a integer greater than 0
        
        # in case of a positive outcome, use this construct to write it to a JSON file

        # history_message = HistoryMessages.deposit("success", amount, self.balance)
        # self.write_to_history(history_message)

        # in case of a negative outcome, use this construct to write to the JSON file
            
        # history_message = HistoryMessages.deposit("failure", amount, self.balance)
        # self.write_to_history(history_message)
        if not isinstance(amount, float):
             print ("Invalid amount for deposit!")
             history_message = HistoryMessages.deposit("failure", amount, self.balance)
             self.write_to_history(history_message)
             return
        
        if amount <= 0:
            print("Invalid amount for deposit!")
            history_message = HistoryMessages.deposit("failure", amount, self.balance)
            self.write_to_history(history_message)
            return
        
        try:
            self.balance += amount
            isTransactionMade = True
            
            if isTransactionMade:
                history_message = HistoryMessages.deposit("success", amount, self.balance)
                self.write_to_history(history_message)
            else:
                history_message = HistoryMessages.deposit("failure", amount, self.balance)
                self.write_to_history(history_message)
        except Exception as e:
            print(f"The following error ocurred during deposit: {e}")
            history_message = HistoryMessages.deposit("failure", amount, self.balance)
            self.write_to_history(history_message)
        
    def debit(self, amount):
        pass
        # TODO:
        # implement account debits with all necessary checks
        # amount must be a integer greater than 0
        # if amount is greater than the amount in the account (insufficient funds) the operation should not work

        # in case of positive outcome use this construct to write to JSON file

        # history_message = HistoryMessages.debit("success", amount, self.balance)
        # self.write_to_history(history_message)

        # in case of a negative outcome, use this construct to write to a JSON file
        
        # history_message = HistoryMessages.debit("failure", amount, self.balance)
        # self.write_to_history(history_message)
        #if amount <= 0:
            # history_message = HistoryMessages.deposit("failure", amount, self.balance)
            # self.write_to_history(history_message)
            # raise ValueError(f"The value to be deposited is too low")
        

    def get_balance(self):
        return self.balance

    def dict_to_string(self, dict):
        if dict["operation_type"] != "exchange":
            return f'type: {dict["operation_type"]} status: {dict["status"]} amount: {dict["amount_of_deposit"]} balance: {dict["total_balance"]}'
        else:
            return f'type: {dict["operation_type"]} status: {dict["status"]} pre exchange amount: {dict["pre_exchange_amount"]} exchange amount: {dict["exchange_amount"]} currency from: {dict["currency_from"]} currency to: {dict["currency_to"]}'
        

    def get_history(self):
        pass
        # TODO:
        # implement a process that returns transaction history line by line
        # use the dict_to_string method to create a string from a dictionary