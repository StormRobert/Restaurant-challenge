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
    
    def resturants(self):
        return list(set(review.restaurant() for review in self._reviews))
    
    def add_reviews(self,restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self._reviews.append(new_review)

    @classmethod
    def all(cls):
        return cls.customers
    
customer1 = Customer("Storm", "Robert")
customer2 = Customer("Romero", "Doe" )
customer3 = Customer("ciara", "Rune")
print(customer1.full_name())
# print(Customer.customers)
    
class Restaurant:
    restaurants = []

    def __init__(self, name):
        self._name = name
        Restaurant.restaurants.append(self)

    def name(self):
        return self._name
    
    def reviews(self):
        return self._reviews

    def customers(self):
        return list(set(review.customer() for review in self._reviews))

    @classmethod
    def all(cls):
        return cls.restaurants
  
class Review:
 all_reviews = []
 def __init__(self, customer, restaurant, rating):
     self._customer = customer
     self._restaurant = restaurant
     self._rating = rating
     Review.all_reviews.append(self)
     restaurant.reviews().append(self)
     customer.add_reviews(restaurant, rating)

def customer(self):
    return self.customer
def restaurant(self):
    return self.restaurant
def rating(self):
    return self.rating

@classmethod
def all(cls):
    return cls.reviews



