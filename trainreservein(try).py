import faulthandler
import datetime

faulthandler.enable()
faulthandler.dump_traceback()

class Node:
    def __init__(self, seatno, acseat, num_ac_coaches=None, seats_per_coach=None, non_acseat=None, sleeper=None):
        self.seat_number = seatno
        self.acseat = acseat
        self.next = None
        self.prev = None
        self.status = "Available"
        self.price = None
        self.num_ac_coaches = num_ac_coaches
        self.nonac = non_acseat
        self.seats_per_coach = seats_per_coach
        self.sleeper = sleeper
        self.totalno_of_seats = num_ac_coaches * seats_per_coach + non_acseat + sleeper
        self.name = None

class TrainReserve:
    def __init__(self, num_ac_coaches=None, seats_per_coach=None, non_acseat=None, sleeper=None):
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

    def initiate_seats(self):
        try:
            if self.totalno_of_seats == 0:
                raise ValueError("Enter a valid total number of seats")
            elif self.totalno_of_seats >= 900 or self.totalno_of_seats < 0:
                raise ValueError("Total number of seats should be between 0 and 900")

            for i in range(1, self.totalno_of_seats + 1):
                ac_seat = i % 2 == 1  # Odd-numbered seats are AC
                sleeper_seat = i % 4 == 0  # Every fourth seat is Sleeper
                non_ac = i % 2 == 0  # Even numbers are non AC

                new_seat = Node(i, ac_seat)

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
                    else:
                        new_seat.price = 200
                        if self.head_nonac is None:
                            self.head_nonac = new_seat
                        else:
                            current_nonac = self.head_nonac
                            while current_nonac.next is not None:
                                current_nonac = current_nonac.next

                            new_seat.prev = current_nonac
                            current_nonac.next = new_seat

        except ValueError as e:
            print(f"Error: {e}")

    def display_the_available_seats(self):
        print("=== Available Seats ===")

        print("\n=== Available Non-AC Seats ===")
        current = self.head_nonac
        while current is not None:
            print(f"Seat Number: {current.seat_number}, Status: {current.status}, Price: {current.price}")
            current = current.next

        print("\n=== Available AC Seats ===")
        current_ac = self.head_ac
        while current_ac is not None:
            print(f"Seat Number: {current_ac.seat_number}, Status: {current_ac.status}, Price: {current_ac.price}")
            current_ac = current_ac.next

        print("\n=== Available Sleeper Seats ===")
        current_sleeper = self.head_sleeper
        while current_sleeper is not None:
            print(f"Seat Number: {current_sleeper.seat_number}, Status: {current_sleeper.status}, Price: {current_sleeper.price}")
            current_sleeper = current_sleeper.next

        print("\nCurrent Date and Time:")
        now = datetime.datetime.now()
        print(now.strftime("%A, %B %d, %Y %I:%M %p"))

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
                            print(f"AC Seat {current_ac.seat_number} is not available for reservation. It has already been reserved.")
                        break
                    current_ac = current_ac.next

                if not found:
                    print(f"AC Seat {seat_number} does not exist.")

        except ValueError as e:
            print(f"Error: {e}")

        now = datetime.datetime.now()
        print("\nCurrent Date and Time:")
        print(now.strftime("%A, %B %d, %Y %I:%M %p"))

    def reserveseatsfornonac(self):
        try:
            seatnumbers = list(map(int, input("Enter comma-separated Seat numbers to be reserved for Non-AC: ").split(',')))
            seatnumbers.sort()

            if any(num <= 0 or num > self.totalno_of_seats for num in seatnumbers):
                raise ValueError("Enter seat numbers within the valid range")

            for seat_number in seatnumbers:
                current_nonac = self.head_nonac
                found = False

                while current_nonac is not None:
                    if current_nonac.seat_number == seat_number:
                        found = True
                        if current_nonac.status == "Available":
                            current_nonac.status = "Reserved for Non-AC"
                            print(f"Non-AC Seat {current_nonac.seat_number} has been successfully reserved.")
                        else:
                            print(f"Non-AC Seat {current_nonac.seat_number} is not available for reservation. It has already been reserved.")
                        break
                    current_nonac = current_nonac.next

                if not found:
                    print(f"Non-AC Seat {seat_number} does not exist.")

        except ValueError as e:
            print(f"Error: {e}")

        now = datetime.datetime.now()
        print("\nCurrent Date and Time:")
        print(now.strftime("%A, %B %d, %Y %I:%M %p"))

    def reserveseatsforsleeper(self):
        try:
            seatnumbers = list(map(int, input("Enter comma-separated Seat numbers to be reserved for Sleeper: ").split(',')))
            seatnumbers.sort()

            if any(num <= 0 or num > self.totalno_of_seats for num in seatnumbers):
                raise ValueError("Enter seat numbers within the valid range")

            for seat_number in seatnumbers:
                current_sleeper = self.head_sleeper
                found = False

                while current_sleeper is not None:
                    if current_sleeper.seat_number == seat_number:
                        found = True
                        if current_sleeper.status == "Available":
                            current_sleeper.status = "Reserved for Sleeper"
                            print(f"Sleeper Seat {current_sleeper.seat_number} has been successfully reserved.")
                        else:
                            print(f"Sleeper Seat {current_sleeper.seat_number} is not available for reservation. It has already been reserved.")
                        break
                    current_sleeper = current_sleeper.next

                if not found:
                    print(f"Sleeper Seat {seat_number} does not exist.")

        except ValueError as e:
            print(f"Error: {e}")

        now = datetime.datetime.now()
        print("\nCurrent Date and Time:")
        print(now.strftime("%A, %B %d, %Y %I:%M %p"))

    def cancel_ac_seats(self):
        try:
            print("Canceling AC seats...")
            seatnumbers = list(map(int, input("Enter comma-separated Seat numbers to be canceled for AC: ").split(',')))
            seatnumbers.sort()

            if any(num <= 0 or num > self.totalno_of_seats for num in seatnumbers):
                raise ValueError("Enter seat numbers within the valid range")

            for seat_number in seatnumbers:
                current_ac = self.head_ac
                found = False

                while current_ac is not None:
                    if current_ac.seat_number == seat_number:
                        found = True
                        if current_ac.status == "Reserved for AC":
                            current_ac.status = "Available"
                            print(f"AC Seat {current_ac.seat_number} has been successfully canceled.")
                        else:
                            print(f"AC Seat {current_ac.seat_number} is not reserved yet, so it cannot be canceled.")
                        break
                    current_ac = current_ac.next

                if not found:
                    print(f"AC Seat {seat_number} does not exist.")

        except ValueError as e:
            print(f"Error: {e}")

        now = datetime.datetime.now()
        print("\nCurrent Date and Time:")
        print(now.strftime("%A, %B %d, %Y %I:%M %p"))

    def cancel_nonac_seats(self):
        try:
            print("Canceling Non-AC seats...")
            seatnumbers = list(map(int, input("Enter comma-separated Seat numbers to be canceled for Non-AC: ").split(',')))
            seatnumbers.sort()

            if any(num <= 0 or num > self.totalno_of_seats for num in seatnumbers):
                raise ValueError("Enter seat numbers within the valid range")

            for seat_number in seatnumbers:
                current_nonac = self.head_nonac
                found = False

                while current_nonac is not None:
                    if current_nonac.seat_number == seat_number:
                        found = True
                        if current_nonac.status == "Reserved for Non-AC":
                            current_nonac.status = "Available"
                            print(f"Non-AC Seat {current_nonac.seat_number} has been successfully canceled.")
                        else:
                            print(f"Non-AC Seat {current_nonac.seat_number} is not reserved yet, so it cannot be canceled.")
                        break
                    current_nonac = current_nonac.next

                if not found:
                    print(f"Non-AC Seat {seat_number} does not exist.")

        except ValueError as e:
            print(f"Error: {e}")

        now = datetime.datetime.now()
        print("\nCurrent Date and Time:")
        print(now.strftime("%A, %B %d, %Y %I:%M %p"))

    def cancel_sleeper_seats(self):
        try:
            print("Canceling Sleeper seats...")
            seatnumbers = list(map(int, input("Enter comma-separated Seat numbers to be canceled for Sleeper: ").split(',')))
            seatnumbers.sort()

            if any(num <= 0 or num > self.totalno_of_seats for num in seatnumbers):
                raise ValueError("Enter seat numbers within the valid range")

            for seat_number in seatnumbers:
                current_sleeper = self.head_sleeper
                found = False

                while current_sleeper is not None:
                    if current_sleeper.seat_number == seat_number:
                        found = True
                        if current_sleeper.status == "Reserved for Sleeper":
                            current_sleeper.status = "Available"
                            print(f"Sleeper Seat {current_sleeper.seat_number} has been successfully canceled.")
                        else:
                            print(f"Sleeper Seat {current_sleeper.seat_number} is not reserved yet, so it cannot be canceled.")
                        break
                    current_sleeper = current_sleeper.next

                if not found:
                    print(f"Sleeper Seat {seat_number} does not exist.")

        except ValueError as e:
            print(f"Error: {e}")

        now = datetime.datetime.now()
        print("\nCurrent Date and Time:")
        print(now.strftime("%A, %B %d, %Y %I:%M %p"))

    def updateseat(self, current_seat, seat_type):
        current_seat.status = "Reserved"
        current_seat.passenger_name = input(f"Enter the name of the passenger for {seat_type} seat {current_seat.seat_number}: ")
        print(f"{seat_type} seat {current_seat.seat_number} has been successfully updated.")

if __name__ == "__main__":
    num_ac_coaches = 5
    seats_per_coach = 20
    non_ac_seats = 30
    sleeper_seats = 10

    train = TrainReserve(num_ac_coaches, seats_per_coach, non_ac_seats, sleeper_seats)
    train.display_the_available_seats()
    train.reserveseatsforac()
    train.reserveseatsfornonac()
    train.reserveseatsforsleeper()
    train.cancel_ac_seats()
    train.cancel_nonac_seats()
    train.cancel_sleeper_seats()
    train.display_the_available_seats()
