from booking import book_ticket
from reservation import check_reservation
from cancellation import cancel_ticket

print("Welcome to online train ticket booking system!")
print("1. Online Ticket Booking")
print("2. Check Current Reservation")
print("3. Ticket Cancellation")
print("4. Exit")

while True:
    a = int(input("What you wish to do today: "))

    if a == 1:
        book_ticket()

    elif a == 2:
        check_reservation()

    elif a == 3:
        cancel_ticket()

    elif a == 4:
        print("Portal exit successful")
        print("Thank You!!")
        break

    else:
        print("Choice Invalid!")