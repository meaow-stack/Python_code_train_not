import faulthandler
import datetime


faulthandler.enable()
faulthandler.dump_traceback()


class Node:
    def __init__(self, seatno, acseat,num_ac_coaches = None, seats_per_coach = None, non_acseat = None, sleeper = None):
        self.seat_number = seatno
        self.acseat = acseat
        self.next = None
        self.prev = None
        self.status = None
        self.price = None
        self.num_ac_coaches = num_ac_coaches
        self.nonac = non_acseat
        self.seats_per_coach = seats_per_coach
        self.sleeper = sleeper
        self.totalno_of_seats = num_ac_coaches * seats_per_coach + non_acseat + sleeper
        self.name = None


class TrainReserve:
    def __init__(self, num_ac_coaches = None, seats_per_coach = None, non_acseat = None, sleeper = None,seatno = None, acseat):
        self.seat_number = seatno
        self.acseat = acseat
        self.num_ac_coaches = num_ac_coaches
        self.nonac = non_acseat
        self.seats_per_coach = seats_per_coach
        self.sleeper = sleeper
        self.totalno_of_seats = num_ac_coaches * seats_per_coach + non_acseat + sleeper
        self.name = None
        self.passenger = None
        self.head_ac = None
        self.head_nonac = None
        self.head_sleeper = None
        self.initiate_seats()
        self.display_the_available_seats()
        self.display_booked_seats()

    def initiate_seats(self):
        try:
            if self.totalno_of_seats == 0:
                raise ValueError("Enter a valid total number of seats")
            elif self.totalno_of_seats >= 900 or self.totalno_of_seats < 0:
                raise ValueError("Total number of seats should be between 0 and 900")

            for i in range(1, self.totalno_of_seats + 1):
                ac_seat = i % 2 == 1  # Odd-numbered seats are AC
                sleeper_seat = i % 4 == 0  # Every fourth seat is Sleeper
                non_ac = i % 2 == 0  # even numbers are non AC

                new_seat = TrainReserve(i, ac_seat)
                new_seat.status = "Available"

                #if sleeper_seat:
                    ##self.add_seat_to_list(new_seat, self.head_sleeper)
                ##elif is_ac_:
                   # self.add_seat_to_list(new_seat, self.head_ac)
                #else:
                    #self.add_seat_to_list(new_seat, self.head_non_ac)
                    
                if sleeper_seat:
                    new_seat.price = 400
                    if self.head_sleeper is None:
                        self.head_sleeper = new_seat
                    else:
                        current_sleeper = self.head_sleeper
                        while current_sleeper.next is not None:
                            current_sleeper = current_sleeper.next

                        new_seat.prev = current_sleeper
                        current_sleeper.next = new_seat
                        new_seat.next = self.head_sleeper
                        self.head_sleeper.prev = new_seat
                else:
                    if ac_seat:
                        new_seat.price = 1000
                        if self.head_ac is None:
                            self.head_ac = new_seat
                        else:
                            current_ac = self.head_ac
                            while current_ac.next is not None:
                                current_ac = current_ac.next

                            new_seat.prev = current_ac
                            current_ac.next = new_seat
                            new_seat.next = self.head_ac
                            self.head_ac.prev = new_seat
                    else:
                        if non_ac:
                            new_seat.price = 200
                            if self.head_nonac is None:
                                self.head_nonac = new_seat
                            else:
                                current_nonac = self.head_nonac
                                while current_nonac.next is not None:
                                    current_nonac = current_nonac.next

                                new_seat.prev = current_nonac
                                current_nonac.next = new_seat
                                new_seat.next = self.head_nonac
                                self.head_nonac.prev = new_seat

        except ValueError as e:
            print(f"Error: {e}")

    def display_the_available_seats(self,head_ac,head_non_ac,head_sleeper):
        print("=== Available Seats ===")
        print("=== Available Seats for NON AC")
        print("------------------------")
        current = self.head_nonac
        while current is not None:
            print(f"AC Seat Number: {current.seat_number}, Price: {current.price}")
            print(f"Seat Number: {current.seat_number}, AC: {current.acseat}, Status: {current.status}")
            current = current.next

        print("=== Available Seats for AC Seats")
        current_ac = self.head_ac
        while current_ac is not None:
            print("------------------------")

            print(f"AC Seat Number: {current_ac.seat_number}, Price: {current_ac.price}")
            print(f"Seat Number: {current_ac.seat_number}, AC: {current_ac.acseat}, Status: {current_ac.status}")
            current_ac = current_ac.next

        print("=== Available Seats for Sleeper seats")
        print("------------------------")
        current_sleeper = self.head_sleeper
        while current_sleeper is not None:
            print(f"AC Seat Number: {current_sleeper.seat_number}, Price: {current_sleeper.price}")
            print(f"Seat Number: {current_sleeper.seat_number}, AC: {current_sleeper.acseat}, Status: {current_sleeper.status}")
            current_sleeper = current_sleeper.next

        print("\nCurrent Date and Time:")
        x = datetime.datetime.now()
        print(x.year)
        print(x.strftime("%A"))

        print("\nCurrent Date and Time:")
        y = datetime.datetime.now()
        print(y)
        
    def reserveseatsforac(self):
        try:
            seatnumbers = list(map(int, input("Enter comma-separated Seat numbers to be reserved for AC: ").split(',')))
            seatnumbers.sort()

            if any(num <= 0 or num > self.totalno_of_seats for num in seatnumbers):
                raise ValueError("Enter seat numbers within the valid range")

            for seat_number in seatnumbers:
                current_ac = self.head_ac
                found = False

                while current_ac is not None:
                    if current_ac.seat_number == seat_number:
                        found = True
                        if current_ac.status == "Available":
                            current_ac.status = "Reserved for AC"
                            print(f"AC Seat {current_ac.seat_number} has been successfully reserved for AC.")
                        else:
                            print(f"AC Seat {current_ac.seat_number} is not available for reservation. It has already been reserved for AC.")
                            print(f"price of the seat {current_ac.price}")
                        break
                    current_ac = current_ac.next

                if not found:
                    print(f"AC Seat {seat_number} does not exist or has been reserved for AC.")

        except ValueError as e:
            print(f"Error: {e}")

        # Display current date and time
        now = datetime.datetime.now()
        print("\nCurrent Date and Time:")
        print(now.strftime("%A, %B %d, %Y %I:%M %p"))

        
    def reserveseatsfornonac(self):
        try:
            seatnumbers = list(map(int, input("Enter comma-separated Seat numbers to be reserved for AC: ").split(',')))
            seatnumbers.sort()

            if any(num <= 0 or num > self.totalno_of_seats for num in seatnumbers):
                raise ValueError("Enter seat numbers within the valid range")

            for seat_number in seatnumbers:
                current_nonac = self.head_ac
                found = False

                while current_nonac is not None:
                    if current_nonac.seat_number == seat_number:
                        found = True
                        if current_nonac.status == "Available":
                            current_nonac.status = "Reserved for AC"
                            print(f"AC Seat {current_nonac.seat_number} has been successfully reserved for AC.")
                            print(f"price of the seat {current_nonac.price}")
                        else:
                            print(f"AC Seat {current_nonac.seat_number} is not available for reservation. It has already been reserved for AC.")
                        break
                    current_nonac = current_nonac.next

                if not found:
                    print(f"AC Seat {seatnumbers} does not exist or has been reserved for AC.")

        except ValueError as e:
            print(f"Error: {e}")

        # Display current date and time
        now = datetime.datetime.now()
        print("\nCurrent Date and Time:")
        print(now.strftime("%A, %B %d, %Y %I:%M %p"))



    def reserveseatsforsleeper(self): 
        try:
            seatnumbers = list(map(int, input("Enter comma-separated Seat numbers to be reserved for AC: ").split(',')))
            seatnumbers.sort()

            if any(num <= 0 or num > self.totalno_of_seats for num in seatnumbers):
                raise ValueError("Enter seat numbers within the valid range")

            for seat_number in seatnumbers:
                current_sleeper= self.head_ac
                found = False

                while current_sleeper is not None:
                    if current_sleeper.seat_number == seat_number:
                        found = True
                        if current_sleeper.status == "Available":
                            current_sleeper.status = "Reserved for AC"
                            print(f"AC Seat {current_sleeper.seat_number} has been successfully reserved for AC.")
                            print(f"price of the seat {current_sleeper.price}")
                        else:
                            print(f"AC Seat {current_sleeper.seat_number} is not available for reservation. It has already been reserved for AC.")
                        break
                    current_sleeper = current_sleeper.next

                if not found:
                    print(f"AC Seat {seatnumbers} does not exist or has been reserved for AC.")

        except ValueError as e:
            print(f"Error: {e}")

        # Display current date and time
        now = datetime.datetime.now()
        print("\nCurrent Date and Time:")
        print(now.strftime("%A, %B,%d, %Y %I:%M %p"))
        

    def cancel_ac_seats(self): 
        try:
            print("  ")
            print("Canceling AC seats...")
            seatnumbers = list(map(int, input("Enter comma-separated Seat numbers to be canceled for AC: ").split(',')))
            seatnumbers.sort()

            if any(num <= 0 or num > self.totalno_of_seats for num in seatnumbers):
                raise ValueError("Enter seat numbers within the valid range")

            current_ac = self.head_ac
            while current_ac is not None:
                if current_ac.seat_number == seatnumbers:
                    if current_ac.status == "Reserved for AC":
                        current_ac.status = "Canceled, ready for reservation"
                        print(f"AC Seat {current_ac.seat_number} reservation has been canceled")

                    if current_ac.status == "Available":
                        
                        print(f"Seat number {current_ac.seat_number} is already available, you can't cancel it")
                        print(f"Seat number {current_ac.seat_number} price: {current_ac.price}")
                        
            current_ac = current_ac.next

        except ValueError as e:
            print(f"Error: {e}")

        x = datetime.datetime.now()
        print(x.year)
        print(x.strftime("%A"))

        y = datetime.datetime.now()
        print(y)

    def cancel_non_ac_seats(self):
        try:
            print("  ")
            print("Canceling the NON AC seats...")
            seatnumbers = list(map(int, input("Enter comma-separated Seat numbers to be canceled for Non-AC: ").split(',')))
            seatnumbers.sort()

            current_nonac = self.head_ac
            while current_nonac is not None:
                if current_nonac.seat_number == seatnumbers:
                    if current_nonac.status == "Reserved for AC":
                        current_nonac.status = "Canceled, ready for reservation"
                        print(f"AC Seat {current_nonac.seat_number} reservation has been canceled")

                    if current_nonac.status == "Available":
                        
                        print(f"Seat number {current_nonac.seat_number} is already available, you can't cancel it")
                        print(f"Seat number {current_nonac.seat_number} price: {current_nonac.price}")
                        
            current_nonac = current_nonac.next
            
        except ValueError as e:
            print(f"Error: {e}")

        x = datetime.datetime.now()
        print(x.year)
        print(x.strftime("%A"))

        y = datetime.datetime.now()
        print(y)


    def cancel_for_sleeper(self): 
        try:
            print("  ")
            print("Canceling the sleeper seats")
            seatnumbers = list(map(int, input("Enter comma-separated Seat numbers to be canceled for Non-AC: ").split(',')))
            seatnumbers.sort()

            if any(num <= 0 or num > self.totalno_of_seats for num in seatnumbers):
                raise ValueError("Enter seat numbers within the valid range")

            
            current_sleeper = self.head_ac
            while current_sleeper is not None:
                if current_sleeper.seat_number == seatnumbers:
                    if current_sleeper.status == "Reserved for AC":
                        current_sleeper.status = "Canceled, ready for reservation"
                        print(f"AC Seat {current_sleeper.seat_number} reservation has been canceled")

                    if current_sleeper.status == "Available":
                        
                        print(f"Seat number {current_sleeper.seat_number} is already available, you can't cancel it")
                        print(f"Seat number {current_sleeper.seat_number} price: {current_sleeper.price}")
                        
            current_sleeper = current_sleeper.next

        except ValueError as e:
              print(f"Error: {e}")

        x = datetime.datetime.now()
        print(x.year)
        print(x.strftime("%A"))

        y = datetime.datetime.now()
        print(y)

    
    def status(self):
        print("=== Current Seat Status ===")
        # Display status of all seats

        print("\nAC Seats:")
        current_ac = self.head_ac
        while current_ac is not None:
            print(f"AC Seat Number: {current_ac.seat_number}, Status: {current_ac.status}")
            current_ac = current_ac.next

        print("\n NON AC Seats:")
        current_nonac = self.head_nonac
        while current_nonac is not None:
            print(f"Non-AC Seat Number: {current_nonac.seat_number}, Status: {current_nonac.status}")
            current_nonac = current_nonac.next

        print("\n Sleeper Seats:")

        current_sleeper = self.head_sleeper
        while current_sleeper is not None:
            print(f"Sleeper Seat Number: {current_sleeper.seat_number}, Status: {current_sleeper.status}")
            current_sleeper = current_sleeper.next


        print("\nCurrent Date and Time:")

        x = datetime.datetime.now()
        print(x.year)
        print(x.strftime("%A"))

        y = datetime.datetime.now()
        print(y)

        def display_booked_seats(self):
            print("\n=== Booked Seats ===")
            print("------------------------")
        for seat_type in ["AC", "Non-AC", "Sleeper"]:
            current_seat = getattr(self, f"head_{seat_type.lower()}")
            print(f"Booked Seats for {seat_type}:")
            while current_seat is not None:
                if current_seat.status == f"Reserved for {seat_type}":
                    passenger = current_seat.passenger
                    print(f"Seat Number: {current_seat.seat_number}, Passenger: {passenger.name}, Age: {passenger.age}, Contact: {passenger.contact}")
                current_seat = current_seat.next

def menu(train_system):
    while True:
        print("\n1. Initialize the Seats")
        print("2. \n Reserve Seats for AC")
        print("3. \n Reserve Seats for Non-AC")
        print("4. \n Reserve Seats for Sleeper")
        print("5. \n Cancel AC Seats")
        print("6. \n Cancel Non-AC Seats")
        print("7. \n Cancel Sleeper Seats")
        print("8. \n Display Status")
        print("9. \n Display the Available Seats")
        print("10. \n  Display Booked Seats")
        print("11. \n Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            train_system.initiate_seats()
            break
        elif choice == "2":
            train_system.reserveseatsforac()
            break
        elif choice == "3":
            train_system.reserveseatsfornonac()
            break
        elif choice == "4":
            train_system.reserveseatsforsleeper()
            break
        elif choice == "5":
            train_system.cancel_ac_seats()
            break
        elif choice == "6":
            train_system.cancel_non_ac_seats()
            break
        elif choice == "7":
            train_system.cancel_for_sleeper()
            break
        elif choice == "8":
            train_system.status()
            break
        elif choice == "9":
            train_system.display_the_available_seats()
            break
        elif choice == "10":
            train_system.display_booked_seats()
            break
        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")
            

def main():
    try:
        num_ac_coaches = int(input("Enter the number of AC coaches: "))
        seats_per_coach = int(input("Enter the number of seats per AC coach: "))
        non_ac_seat = int(input("Enter the number of non-AC seats: "))
        sleeper = int(input("Enter the number of sleeper seats: "))

        train_system = TrainReserve(num_ac_coaches, seats_per_coach, non_ac_seat, sleeper)

        menu(train_system)

        if num_ac_coaches <= 0 or seats_per_coach <= 0 or non_ac_seat <= 0 or sleeper <= 0:
            raise ValueError("All inputs must be positive integers")


        x = datetime.datetime.now()
        print(x.year)
        print(x.strftime("%A"))

        y = datetime.datetime.now()
        print(y)
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()