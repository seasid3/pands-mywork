# test the module myfunctions
# Author: Orla Woods

# this is a module

import logging
logging.basicConfig(filename="./bank.log",
                    level = logging.DEBUG,
                    format="%(asctime)s-%(levelname)s-%(message)s-%(filename)s-%(lineno)d")

balance = 100

def withdraw(amount):
    global balance
    if amount < 0:
        logging.critical(f"the ({amount}) should never be less than 0") 
        raise ValueError("amount should always be greater than 0")
    if amount > balance:
        logging.warning(f"trying to withdraw more ({amount}) that is in account ({balance})")
        raise ValueError("anot enough funds")
    balance = balance - amount
    logging.info(f"we have just withdrawn {amount}, new balance is {balance}")
    return balance

if __name__ == "__main__":  # this line lets me put code/test cases in here and the code will only run here 
     # and not if i bring this module/function into my code via import the function. gives me space
     # to test the code
     assert withdraw(20) == 80, "incorrect calculation"
     try:
         withdraw(-1)
         assert False, "should have thrown a value error"
     except ValueError as ve:
         pass
     
     try:
        withdraw(110)
        assert False, "cant withdraw more than in balance"
     except ValueError as ve:
        pass 
     
     print("all good")

     # i can modify my code and test cases here 