class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._reviews = []
        
        Customer.customers.append(self)

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"
    
    def restaurants(self):
        return list(set(review.restaurant() for review in self._reviews))
    
    def add_reviews(self,restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self._reviews.append(new_review)

    def num_reviews(self):
     return len(self._reviews)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.customers:
            if customer.full_name() == name:
                return customer

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.customers if customer.given_name() == given_name]

    @classmethod
    def all(cls):
        return cls.customers
    
# customer1 = Customer("Storm", "Robert")
# customer2 = Customer("Romero", "Doe" )
# customer3 = Customer("ciara", "Rune")
# print(customer1.full_name())
# print(Customer.customers)
    
class Restaurant:
    restaurants = []

    def __init__(self, name):
        self._name = name
        self._reviews = []
        Restaurant.restaurants.append(self)

    def name(self):
        return self._name
    
    def reviews(self):
        return self._reviews

    def customers(self):
        return list(set(review.customer() for review in self._reviews))
    
    def average_star_rating(self):
        if not self._reviews:
            return 0

        total_rating = sum(review.rating() for review in self._reviews)
        return total_rating / len(self._reviews)

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

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls.all_reviews
     

def customer(self):
    return self._customer

def restaurant(self):
    return self._restaurant

def rating(self):
    return self._rating

@classmethod
def all(cls):
    return cls.all_reviews

def main():
    customer1 = Customer("Storm", "Robert")
    customer2 = Customer("Khalif", "Kairo")
    customer3 = Customer("Bruce", "Wayne")

    restaurant1 = Restaurant("KFC")
    restaurant2 = Restaurant("CJ's")
    restaurant3 = Restaurant("Pizza Hut")

    review1 = Review(customer1, restaurant1, 3)
    review2 = Review(customer2, restaurant2, 4)
    review3 = Review(customer3, restaurant3, 5)

    
    print(customer1.full_name())  
    print(customer2.full_name())

    for review in Review.all():
     print(f"Review - Customer: {review.customer().full_name()}, Restaurant: {review.restaurant().name()}, Rating: {review.rating()}")

if __name__ == '__main__':
    main()

