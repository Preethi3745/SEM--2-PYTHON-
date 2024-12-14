import random

class Customer:
    def __init__(self, cus_id, name, phone):
        self.cus_id = cus_id
        self.name = name
        self.phone = phone

    @staticmethod
    def gen_rand_id():
        c_id = random.randint(1000, 9999)
        return f"TICK{c_id}"

    @staticmethod
    def verify_customer_id(cus_id):
        if cus_id[:4] == "TICK" and cus_id[4:].isdigit():
            print("Valid")
            return True
        else:
            print("Invalid")
            return False


class TicketBooking:
    def __init__(self):
        self.events = {
            "Concert": {"price": 1500, "seats": 500},
            "Drama": {"price": 100, "seats": 100},
            "Movie": {"price": 250, "seats": 200}
        }
        self.booked_tickets = []

    def view_events(self):
        print("\nAvailable Events:")
        for event, details in self.events.items():
            print(f"{event}: {details['price']} per ticket, {details['seats']} seats available")

    def book_tickets(self, event_name, quantity, customer):
        if event_name in self.events:
            event = self.events[event_name]
            if event["seats"] >= quantity:
                total_price = event["price"] * quantity
                event["seats"] -= quantity
                self.booked_tickets.append({
                    "customer_id": customer.cus_id,
                    "event": event_name,
                    "quantity": quantity,
                    "total_price": total_price
                })
                print(f"Tickets booked successfully! Total Price: {total_price}")
            else:
                print("Seats not available!")
        else:
            print("Event name not available")

    def view_tickets(self, customer):
        print("\n*TICKET INFORMATION*")
        customer_tickets = [t for t in self.booked_tickets if t["customer_id"] == customer.cus_id]
        if not customer_tickets:
            print("No tickets booked.")
        else:
            for ticket in customer_tickets:
                print(f"Event: {ticket['event']}, Quantity: {ticket['quantity']}, Total Cost: {ticket['total_price']}")


# Main Program
if __name__ == "__main__":
    book = TicketBooking()
    print("*Welcome to the Ticket Booking Application*")

    cus_id = input("Enter the Customer ID: ")
    if Customer.verify_customer_id(cus_id):
        name = input("Enter your Name: ")
        phone = input("Enter your Phone Number: ")
        customer = Customer(cus_id, name, phone)
    else:
        name = input("Enter your Name: ")
        phone = input("Enter your Phone Number: ")
        cus_id = Customer.gen_rand_id()
        customer = Customer(cus_id, name, phone)
        print(f"Your Customer ID is: {cus_id}")

    while True:
        print("\nBooking Info:")
        print("1. View Events")
        print("2. Book Tickets")
        print("3. View My Tickets")
        print("4. Exit")
        choice = int(input("Enter an option to continue: "))

        if choice == 1:
            book.view_events()
        elif choice == 2:
            event_name = input("Enter the Event Name: ")
            quantity = int(input("Enter the Number of Tickets: "))
            book.book_tickets(event_name, quantity, customer)
        elif choice == 3:
            book.view_tickets(customer)
        elif choice == 4:
            print("Thank you for using the Ticket Booking Application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
