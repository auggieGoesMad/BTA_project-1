import json

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
        
        file_content = self.file_manager.read_json(self.hist_file_path)
        file_content.append(hist_dict)
        self.file_manager.write_json(file_content, self.hist_file_path) 

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

        try:
            given_amount = int(amount)
            
            if given_amount <= 0:
                print("Invalid amount for deposit!")
                history_message = HistoryMessages.deposit("failure", given_amount, self.balance)
                self.write_to_history(history_message)
                return
        
            try:
                self.balance += given_amount
                isTransactionMade = True
                
                if isTransactionMade:
                    history_message = HistoryMessages.deposit("success", given_amount, self.balance)
                    self.write_to_history(history_message)
                else:
                    history_message = HistoryMessages.deposit("failure", given_amount, self.balance)
                    self.write_to_history(history_message)
            except Exception as e:
                print(f"The following error ocurred during deposit: {e}")
                history_message = HistoryMessages.deposit("failure", given_amount, self.balance)
                self.write_to_history(history_message)
        except Exception:
            print ("Invalid amount for deposit!")
            history_message = HistoryMessages.deposit("failure", amount, self.balance)
            self.write_to_history(history_message)
            return
            
        
        
    def debit(self, amount):
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

        try:
            given_amount = int(amount)

            if given_amount <= 0 or given_amount > self.balance:
                print ("Invalid amount for debit!")
                history_message = HistoryMessages.debit("failure", given_amount, self.balance)
                self.write_to_history(history_message)
                return
            try:
                self.balance -= given_amount
                isTransactionMade = True
                
                if isTransactionMade:
                    history_message = HistoryMessages.debit("success", given_amount, self.balance)
                    self.write_to_history(history_message)
                else:
                    history_message = HistoryMessages.debit("failure", given_amount, self.balance)
                    self.write_to_history(history_message)
            except Exception as e:
                print(f"The following error ocurred during debit: {e}")
                history_message = HistoryMessages.debit("failure", given_amount, self.balance)
                self.write_to_history(history_message)
        
        except Exception:
            print ("Invalid amount for debit!")
            history_message = HistoryMessages.debit("failure", amount, self.balance)
            self.write_to_history(history_message)
            return

    
    def get_balance(self):
        return self.balance

    def dict_to_string(self, dict):
        if dict["operation_type"] != "exchange":
            return f'type: {dict["operation_type"]} status: {dict["status"]} amount: {dict["amount_of_deposit"]} balance: {dict["total_balance"]}'
        else:
            return f'type: {dict["operation_type"]} status: {dict["status"]} pre exchange amount: {dict["pre_exchange_amount"]} exchange amount: {dict["exchange_amount"]} currency from: {dict["currency_from"]} currency to: {dict["currency_to"]}'
        

    def get_history(self):
        # TODO:
        # implement a process that returns transaction history line by line
        # use the dict_to_string method to create a string from a dictionary
        with open(self.hist_file_path, "r") as file:
            try:
                file_content = json.load(file)
                
                for item in file_content:
                    item_string = self.dict_to_string(item)
                    print(item_string)
            except json.JSONDecodeError as e:
                print (f"The following error ocuured while reading from the hist.json file: {e}")


