from abc import ABC, abstractmethod


class AbstractMovieBooking(ABC):
    def __init__(self, theatre_name, movie_name, ticket_price):
        self.theatre_name = theatre_name
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.tickets_sold = 0
        self.total_income = 0
        self.food_items = []
        self.drinks = []

    @abstractmethod
    def book_ticket(self, number_of_tickets):
        pass

    @abstractmethod
    def add_food(self, food_item, price):
        pass

    @abstractmethod
    def add_drink(self, drink, price):
        pass

    @abstractmethod
    def display_booking_info(self):
        pass


class MovieBooking(AbstractMovieBooking):
    def __init__(self, theatre_name, movie_name, ticket_price):
        super().__init__(theatre_name, movie_name, ticket_price)

    def book_ticket(self, number_of_tickets):
        self.tickets_sold += number_of_tickets
        income = number_of_tickets * self.ticket_price
        self.total_income += income
        print(
            f"{number_of_tickets} tickets booked for '{self.movie_name}' at {self.theatre_name}. Total income: {self.total_income:.2f}")

    def add_food(self, food_item, price):
        self.food_items.append((food_item, price))
        self.total_income += price
        print(f"Food item '{food_item}' added for {price:.2f}. Total income: {self.total_income:.2f}")

    def add_drink(self, drink, price):
        self.drinks.append((drink, price))
        self.total_income += price
        print(f"Drink '{drink}' added for {price:.2f}. Total income: {self.total_income:.2f}")

    def display_booking_info(self):
        print(f"Theatre: {self.theatre_name}")
        print(f"Movie: {self.movie_name}")
        print(f"Tickets Sold: {self.tickets_sold}")
        print(f"Total Income: {self.total_income:.2f}")
        print("Food Items: ", self.food_items)
        print("Drinks: ", self.drinks)


# Example usage
booking = MovieBooking("Cinema Hall", "Inception", 12.0)
booking.book_ticket(3)
booking.add_food("Popcorn", 5.0)
booking.add_drink("Cola", 3.0)
booking.display_booking_info()
