from FileManager import FileManager
from HistoryMessages import HistoryMessages

import requests

class CurrencyExchange:

    def __init__(self, balance = 0):
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        
    def write_to_history(self, hist_dict):
        # TODO:
        # Comment and refine the code below so that the dictionary 
        # from hist_dict is added to hist.json

        self.file_manager.add_to_json(hist_dict, self.hist_file_path)

    def get_exchange_rates(self):
        # Implement a process that sends a get request to the link 
        # and returns the resulting dictionary.

        url = "https://fake-api.apps.berlintech.ai/api/currency_exchange"

        try:
            response = requests.get(url)

            response.raise_for_status()

            try:
                data = response.json()
                return data
            except ValueError as e:
                raise ValueError("Response content is not valid") from e
        except requests.exceptions.RequestException as e:
            print(f"The following error ocurred durin getting the exchange rates: {e}")
    
    def exchange_currency(self, currency_from, currency_to, amount):

        # implement a process that transfers the specified amount from currency `currency_from` 
        # to currency `currency_to` and, if positive, returns the amount in the new currency

        # with a positive outcome, the record of history looks like this 
        # history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
        # self.write_to_history(history_message)
        
        # in case of a negative outcome, the history entry looks like this
        # - if currency_from or currency_to is specified incorrectly
        # - if amount is not a number
        # history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
        # self.write_to_history(history_message)

        get_exchange_rates = self.get_exchange_rates()
        try:
            given_amount = int(amount)

            if given_amount <= 0:
                print ("The given amount is not a positive number")
                history_message = HistoryMessages("failure", amount, None, currency_from, currency_to)
                self.write_to_history(history_message)
                return
            
            #if currency_from not in self.get_exchange_rates:
            if get_exchange_rates.get(currency_from) is None:
                print("Currency exchange failed!")
                history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
                self.write_to_history(history_message)
                return None
            
            #if currency_from not in self.get_exchange_rates:
            if get_exchange_rates.get(currency_to) is None:
                print("Currency exchange failed!")
                history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
                self.write_to_history(history_message)
                return None
            
            extract_currency_from = get_exchange_rates[currency_from]
            extract_currency_to = get_exchange_rates[currency_to]
            converted_amount = (given_amount * extract_currency_to)/extract_currency_from

            history_message = HistoryMessages.exchange("success", given_amount, converted_amount, currency_from, currency_to)   
            self.write_to_history(history_message)
            return converted_amount

        except Exception:
            print("Currency exchange failed!")
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return