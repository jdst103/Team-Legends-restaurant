from People_class import People

class Customer(People):
    def __init__(self, name, address=None):
        super().__init__(name)
        if address is None:
            address = []
        else:
            self.address = address
        self.__payment_details = {}

    def set_payment_details(self, address, card_no):
        self.__payment_details['address'] = address
        self.__payment_details['card number'] = card_no

    def get_payment_details(self):
        return self.__payment_details

    



#address details , payment details
#alter ingredient
#combo method?