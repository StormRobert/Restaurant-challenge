class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        
        Customer.customers.append(self)

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls.customers
    
customer1 = Customer("Storm", "Robert")
print(customer1.full_name())
    
class Restaurant:
    restaurants = []

    def __init__(self, name):
        self._name = name
        Restaurant.restaurants.append(self)

    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return cls.restaurants
  
