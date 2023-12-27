import os
import logging

class TicketBookingSystem:
    def __init__(self):
        self.remaining_tickets_file = "remaining_tickets.txt"
        self.ticket_types = {"1AC": {"price": 600, "description": "1st AC"},
                             "Sleeper": {"price": 800, "description": "Sleeper"},
                             "2AC": {"price": 400, "description": "2nd Class AC"}}
        self.remaining_tickets = {}
        self.logger = self.setup_logger()

    def setup_logger(self):
        logging.basicConfig(filename='ticket_booking.log', level=logging.DEBUG)
        return logging.getLogger(__name__)

    def load_remaining_tickets(self):
        try:
            with open(self.remaining_tickets_file, "r") as file:
                for line in file:
                    ticket_type, count = line.strip().split(":")
                    self.remaining_tickets[ticket_type] = int(count)
        except FileNotFoundError:
            # Initialize with maximum available tickets
            self.remaining_tickets = {ticket: float('inf') for ticket in self.ticket_types}
        except Exception as e:
            self.logger.error(f"Error loading remaining tickets: {e}")

    def update_remaining_tickets(self):
        try:
            with open(self.remaining_tickets_file, "w") as file:
                for ticket_type, count in self.remaining_tickets.items():
                    file.write(f"{ticket_type}:{count}\n")
        except Exception as e:
            self.logger.error(f"Error updating remaining tickets: {e}")

    def display_remaining_tickets(self):
        print("=== Remaining Tickets ===")
        for ticket_type, count in self.remaining_tickets.items():
            print(f"{self.ticket_types[ticket_type]['description']} ({ticket_type}): {count} tickets remaining")

    def book_tickets(self, ticket_type, num_tickets):
        try:
            if ticket_type not in self.ticket_types:
                raise ValueError("Invalid ticket type.")

            if num_tickets <= 0:
                raise ValueError("Number of tickets should be greater than zero.")

            if num_tickets > self.remaining_tickets[ticket_type]:
                raise ValueError(f"Only {self.remaining_tickets[ticket_type]} tickets available for {ticket_type}.")

            cost_per_ticket = self.ticket_types[ticket_type]["price"]
            total_cost = cost_per_ticket * num_tickets

            print(f"\nBooking {num_tickets} tickets for {self.ticket_types[ticket_type]['description']}.")
            print(f"Cost per ticket: ${cost_per_ticket}")
            print(f"Total cost: ${total_cost}")

            confirm_booking = input("Confirm booking? (yes/no): ").lower()

            if confirm_booking == "yes":
                # Update remaining tickets
                self.remaining_tickets[ticket_type] -= num_tickets
                self.update_remaining_tickets()
                print("\nTickets booked successfully!")
                print(f"Thank you for booking with us. Enjoy your journey!\n")
            else:
                print("\nBooking canceled.")

        except ValueError as e:
            self.logger.error(f"Booking error: {e}")
            print(f"Error: {e}")

    def menu(self):
        self.load_remaining_tickets()

        while True:
            print("\n=== Ticket Booking Menu ===")
            print("1. Display Remaining Tickets")
            print("2. Book Tickets")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                self.display_remaining_tickets()
            elif choice == "2":
                ticket_type = input("Enter ticket type (1AC/Sleeper/2AC): ").upper()
                if ticket_type in self.ticket_types:
                    num_tickets = int(input("Enter the number of tickets: "))
                    self.book_tickets(ticket_type, num_tickets)
                else:
                    print("Invalid ticket type. Please enter 1AC, Sleeper, or 2AC.")
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    booking_system = TicketBookingSystem()
    booking_system.menu()
