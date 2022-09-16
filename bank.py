 

class BankAccount :
    def __init__(self,holder_name,account_number,ifsc_code,address,account_type,mobile_number,atm_pin):
        self.__holder_name = holder_name
        self.__account_number = account_number
        self.__ifsc_code = ifsc_code
        self.__address = address
        self.__account_type = account_type
        self.mobile_number = mobile_number
        self.__atm_pin = atm_pin

    def show_details(self):
        print('Bank Account Information')
        print('account holder name :',self.__holder_name)
        print('Account No : ',self.__account_number)
        print('IFSC code : ',self.__ifsc_code)
        print('Address :',self.__address)
        print('Account Type :',self.__account_type)
        print('Mobile No. :',self.mobile_number)
        print('ATM Pin :',self.__atm_pin)

    def get_holder_name(self):
        return self.__holder_name

    def set_holder_name(self,new_name):
        if new_name == "":
            print('name cannot be empty')
        else :
            self.__holder_name = new_name

    def get_accoun_no(self):
        return self.__account_number
    
    def get_ifsc_code(self):
        return self.__ifsc_code
    
    def get_address(self):
        return self.__address

    def get_atm_pin(self):
        return self.__atm_pin

    def set_atm_pin(self,new_pin):
        if len(str(new_pin)) == 4 and new_pin.isdigit() == True:
            self.__atm_pin = new_pin
        else:
            print('invalid pin')
account1 = BankAccount('allan','160002345','sibn000234','link road','savings','8089594336','2345')

account1.set_atm_pin('hello')

account1.set_holder_name('')

print(account1.get_holder_name())

 
