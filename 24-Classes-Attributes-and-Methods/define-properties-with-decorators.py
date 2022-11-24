class Currency():
    def __init__(self,dollars):
        self._cents = dollars * 100

    @property
    def dollars(self):
        return self._cents / 100

    @dollars.setter # this tels python that this is the setter method for the property
    def dollars(self,dollars):
        if dollars >=0:
            self._cents = dollars * 100
    

bank_account = Currency(100)
print(bank_account.dollars) # this will call the getter method since there is no feet attribute in Height

bank_account.dollars = 200 # this will call the setter method since we are trying to set the value of the property
print(bank_account.dollars)

bank_account.dollars = -1 # this will not change the value of the property since the setter method will not allow it
print(bank_account.dollars)