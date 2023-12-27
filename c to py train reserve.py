class Node:
    def __init__(self, seatnumber, status):
        self.seatnumber = seatnumber
        self.status = status
        self.next = None
        self.prev = None

def initialize(head):
    seat = int(input("Enter the number of seats: "))
    if seat <= 0 or seat > 560:
        print("Invalid seat limit. Seat limit should be between 1 and 560.")
        return None
    temp = head
    for i in range(1, seat+1):
        new_node = Node(i, "Not Available" if i > 560 else "Available")
        if new_node is None:
            print("\nMemory not allocated")
            exit(0)
        new_node.next = None
        new_node.prev = None
        if head is None:
            head = new_node
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    print("Seats initialized successfully!")
    return head

def seatreserve(head):
    seat = int(input("Enter the seat number to reserve: "))
    current = head
    while current is not None:
        if current.seatnumber == seat:
            if current.status == "Available":
                current.status = "Reserved"
                print(f"The seat {seat} has been reserved successfully.")
                return head
            elif current.status == "Reserved":
                print(f"The seat {seat} is already reserved.")
                return head
            else:
                print(f"The seat {seat} is not available for reservation.")
                return head
        current = current.next
    print(f"Seat {seat} not found.")
    return head

def cancelReservation(head):
    seat = int(input("Enter the seat number to be canceled: "))
    current = head
    if head is None:
        print("No seats are currently reserved.")
        return head
    while current is not None:
        if current.seatnumber <= 0 or current.seatnumber > 560:
            print(f"| Error: Invalid seat number ({current.seatnumber}) found.|")
        if current.seatnumber == seat:
            if current.status == "Reserved":
                current.status = "Cancelled"
                print(f"The reservation for seat {seat} has been cancelled successfully.")
                return head
            elif current.status == "Available":
                print(f"Seat {seat} is not reserved.")
                return head
            else:
                print(f"The seat {seat} is not available for cancellation.")
                return head
        current = current.next
    print(f"Seat {seat} not found.")
    return head

def display(head):
    temp = head
    print("\t\tSeat Reservation System\n\n")
    print("-------------------------------")
    print("| Seat Number | Status       |")
    print("-------------------------------")
    if head is None:
        print("| No seats are currently reserved.|")
        return
    while temp is not None:
        if temp.seatnumber < 0 or temp.seatnumber > 560:
            print(f"| Error: Invalid seat number ({temp.seatnumber}) found.|")
        else:
            print(f"| Seat Number: {temp.seatnumber:<6d} | Status: {temp.status:<10s} |")
            temp = temp.next

head = None
choice = -1
while choice != 4:
    print("Initializing the number of seats")
    print("The number of seats are at a limit of 560")
    print("0. Initialise Seat")
    print("1. Reserve Seat")
    print("2. Cancel Reservation")
    print("3. Display Reservations")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 0:
        head = initialize(head)
    elif choice == 1:
        head = seatreserve(head)
    elif choice == 2:
        head = cancelReservation(head)
    elif choice == 3:
        display(head)
    elif choice == 4:
        print("Exiting program.")
    else:
        print("Invalid Choice. Try again.")

while head is not None:
    temp = head
    head = head.next
    del temp


